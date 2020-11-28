import pyodbc
import logging
import traceback

class CheckSchema:
    def __init__(self,table,connection_cfg):
        self.table = table
        self.connection_cfg = connection_cfg
        self.source_conn = self.connect_to_source()
        self.dest_conn = self.connect_to_destination()
        self.changed_columns_list = {}
    
    def connect_to_source(self):
        try:
            db_user = self.connection_cfg["src_user"]
            db_pwd  = self.connection_cfg["pwd"]
            db_server = self.connection_cfg["server"]
            db_name = self.connection_cfg["name"]
            conn = pyodbc.connect(user=db_user,password=db_pwd, database=db_name)
            return conn
        except Exception as e:
            logging.error("Exception occured in connection with source database")
            raise(e)
    
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

    def get_source_schema(self):
        try:
            dict_source_table={}
            cur = self.source_conn.cursor()
            sql_query = construct_query(self.table)
            cur.execute(sql_query)
            records = cur.fetchall()
            for row in records:
                key = row[0]
                dict_source_table[key] = row[1]
            cur.close()
            return dict_source_table
        except Exception as e:
            logging.error("Exception occurred while executing SQl query: %s" % traceback.format_exc())
            raise (e)

    def get_dest_schema(self):
        try:
            dict_dest_table={}
            cur = self.dest_conn.cursor()
            sql_query = construct_query(self.table)
            cur.execute(sql_query)
            records = cur.fetchall()
            for row in records:
                key = row[0]
                dict_dest_table[key] = row[1]
            cur.close()
            return dict_dest_table
        except Exception as e:
            logging.error("Exception occurred while executing SQl query: %s" % traceback.format_exc())
            raise (e)
    
    def is_schema_changed(self):
        source_table_dict = get_source_schema()
        dest_table_dict = get_dest_schema()
        for k,v in source_table_dict.items():
            # check if the key or new column name is available in the destination table
            # if not present then return False. 
            if k not in dest_table_dict and v!=dest_table_dict[k]:
                self.changed_columns_list[k]=v
        if len(self.changed_columns_list)>0:
            return False
        return True
    
    def changed_columns(self):
        curr_schema = get_dest_schema
        return (self.changed_columns,curr_schema)

    def construct_query(self,table):
        query = "SELECT COLUMN_NAME,TYPE_NAME FROM INFORMATION_SCHEMA.COLUMNS WHERE TABLE_NAME = {0}".format(self.table)
        return query