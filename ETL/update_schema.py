import logging
import pyodbc
import datetime


class UpdateSchema:
    def __init__(self, table_name, changed_columns, current_schema):
        self.table_name = table_name
        self.temp_table_name = "temp_{}".format(table_name)
        self.changed_columns = changed_columns
        self.current_schema = current_schema
        self.connection_cfg = connection_cfg

    def connect_to_dest(self):
        """[summary]

        Returns:
            [type]: [description]
        """
        # ideally both the source and destination connection should be the same method
        # which will support connection to two different sources
        try:
            db_user = self.connection_cfg["user"]
            db_pwd = self.connection_cfg["pwd"]
            db_server = self.connection_cfg["server"]
            db_name = self.connection_cfg["name"]
            conn = pyodbc.connect(user=db_user, password=db_pwd, database=db_name)
            return conn
        except Exception as e:
            logging.error("Exception occured in connection with source database")
            raise (e)

    def create_final_schema(self):
        sql_param = tuple()

        for key, value in self.current_schema.items():
            param = str(key + " " + value)
            sql_param += (param,)
        # adding newly changed columns
        for key, value in self.changed_columns.items():
            param = str(key + " " + value + " DEFAULT Unknown")
            sql_param += (param,)
        sql_command = "CREATE TABLE {0} {1}".format(
            self.temp_table_name, str(sql_param)
        )
        return sql_command

    def create_temp_table(self, sql_command):
        try:
            conn = self.connect_to_dest()
            cur = conn.cursor()
            cur.execute(cur.mogrify(sql_command))
        except:
            logging.error("Error in creating temporary table")
            conn.rollback()
            cur.close()
            conn.close()
            raise Exception
        finally:
            conn.commit()
            conn.close()

    def sync_table_data(self):
        try:
            insert_sql_query = "INSERT INTO {0} SELECT * FROM {1} WHERE 1=1".format(
                self.temp_table_name, self.table_name
            )
            conn = self.connect_to_dest()
            cur = conn.cursor()
            cur.execute(cur.mogrify(insert_sql_query))
        except Exception as e:
            logging.error("Error in inserting data to the temporary table")
            conn.rollback()
            cur.close()
            conn.close()
            raise Exception
        finally:
            conn.close()

    def rename_final_table(self):
        logging.info("renaming final table")
        try:
            curr_time = datetime.datetime.now()
            rename_query = "RENAME TABLE {0} to {1}, {2} to {3}".format(
                self.table_name,
                (self.table_name + "_" + curr_time.strftime("%m-%d-%Y"),),
                self.temp_table_name,
                self.table_name,
            )
            conn = self.connect_to_dest()
            cur = conn.cursor()
            cur.execute(rename_query)

        except Exception as e:
            logging.error("Query for renaming the final table has failed")
            conn.rollback()
            cur.close()
            conn.close()
            raise Exception(e)

        finally:
            conn.commit()
            conn.close()

    def update_schema(self):
        # Step1: create the new schema as a string variable with a temp table
        # Step2: establish connections
        # Step3: run the sql to create temp table
        # Step4: sync data from source to newly created temp table
        # Step5: Once synced rename old table and newly updated table with right name
        # Step6: Commit the transcation and move forward with further steps
        sql_cmd = create_final_schema()
        create_temp_table(sql_cmd)
        sync_table_data()
        rename_final_table()
