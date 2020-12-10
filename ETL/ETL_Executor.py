from ETL.update_schema import UpdateSchema
from ETL.schema_validator import CheckSchema
from configparser import ConfigParser


class ETL_Executor:
    def __init__(self, config, env, connector_config):
        self.config = ConfigParser(config)
        self.connector = ConfigParser(connector_config)
        self.env = env

    def update_schema(self, table, changed_columns_list):
        update_schema = UpdateSchema(table, changed_columns_list)
        update_schema.create_table()
        update_schema.load_to_auxillary()
        update_schema.initiate_rename()

    def check_schema(self, config):
        for table in config:
            schema_validator = CheckSchema(table, self.connector)
            is_changed = schema_validator.is_schema_changed()
            if is_changed:
                changed_columns_list, curr_schema = schema_validator.changed_columns
                update_schema(table, changed_columns_list, curr_schema, self.connector)

    def execute_etl_operations(self):
        """
        Execute the final functions required to load into the final schema of the tables
        """
        pass


def main():
    # assuming this above config file is a temp file which contains
    # the tables for which we track schema changes and perform the
    # steps needed to update the final table in any environment
    config = "--config_file--"
    connector_config = "connection_details_config"

    # environment considered as production environment for this run
    # - this can be runtime param to be obtained later from the
    # invoked instance of script
    env = "production"

    etl_executor = ETL_Executor(config, env, connector_config)
    etl_executor.execute()
