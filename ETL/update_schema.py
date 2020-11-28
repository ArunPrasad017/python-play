import logging
import pyodbc
class UpdateSchema:
    def __init__(self,table_name,changed_columns,current_schema):
        self.table_name = table_name
        self.temp_table_name = 'temp_{}'.format(table_name)
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
            db_pwd  = self.connection_cfg["pwd"]
            db_server = self.connection_cfg["server"]
            db_name = self.connection_cfg["name"]
            conn = pyodbc.connect(user=db_user,password=db_pwd, database=db_name)
            return conn
        except Exception as e:
            logging.error("Exception occured in connection with source database")
            raise(e)

    def create_final_schema(self):
        sql_param = tuple()

        for key,value in self.current_schema.items():
            param = str(key+' '+value)
            sql_param+=(param,)
        # adding newly changed columns 
        for key,value in self.changed_columns.items():
            param = str(key+' '+value+' DEFAULT Unknown')
            sql_param+=(param,)
        sql_command = "CREATE TABLE {0} {1}".format(self.temp_table_name,str(sql_param))
        return sql_command
    
    def create_temp_table(self):
        try:
            sql_command = create_final_schema()
            conn=self.connect_to_dest()
            cur=conn.cursor()
            cur.execute(cur.mogrify(sql_command))
        except:
            logging.error("Error in creating temporary table")
            conn.rollback()
            cur.close()
            conn.close()
            raise Exception
        finally:
            conn.commit()
    
    def sync_table_data():
        

    
    def update_schema(self):
        # Step1: create the new schema as a string variable with a temp table
        # Step2: establish connections
        # Step3: run the sql to create temp table
        # Step4: sync data from source to newly created temp table
        # Step5: Once synced rename old table and newly updated table with right name 
        # Step6: Commit the transcation and move forward with further steps

