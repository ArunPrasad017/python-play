"""
Question: Based on the above employee table structure, explain how you would write a 
          python function to read data from the above employee data and output it into a dictionary
----------------------------------------------------------------------------------------------------------------
Sample Output(Assumed):
    Based on the assumption from the question there are two methods done and attempted 
    a. function - func_generate_employee_list_of_dict()
    Returns a List of dictionaries - [
                                {'EMPLOYEE_ID': 'ByoreQAB', 'TITLE':'VP', 'DEPARTMENT':'AD','ACTIVE':TRUE},
                                {'EMPLOYEE_ID': 'ByoreQAB', 'TITLE':'RSD','DEPARTMENT':'AD','ACTIVE':TRUE},
                                {'EMPLOYEE_ID': 'CSDymQAH', 'TITLE':'VP', 'DEPARTMENT':'Services','ACTIVE':TRUE}
                            ]
    b. Returns a dictionary of the form - 
                            {
                                EMPLOYEE_ID:['ByoreQAB','ByoreQAB','CSDymQAH'],
                                TITLE:['VP','RSD','AD']
                            }
----------------------------------------------------------------------------------------------------------------
# Assumptions,steps and decisions taken regarding the below code for function
1. The source of data is from a database table that supports the odbc connector functionality (using pyodbc)
2. We don't have the connection details so we are assuming that "CONNECTION_STRING" below just includes the information for connection
3. Assuming the database is up and create a connection works without a failure - we then move to run the actual query required to extract the data
    (this is read from a config to support any runtime variables). Using separate function for the connection
4. Records are retrieved through the cursor and then the header is retrieved using the cursor description as a list
5. Due to the columns and their names being obtained at runtime from the above step it will remove any issues seen due to change in schema later
6. func_generate_employee_list_of_dict -  in this function we use zip function to help us create the dictionaries by simeltaneously traversing 
                                          through column list array and the tuple
7. func_generate_employee_dict - in this function we first obtain the tuple and unpack it using the column_name through the zip function to
                                 traverse through the column list and row (tuple) from the query output
"""

import pyodbc
from collections import defaultdict
def connect_to_db(connection_string):
    """returns the necessary cursor and connector from DB after connection  
    Args:
        connection_string ([type]): connection string params

    Raises:
        Exception: if connection fails raise an exception

    Returns:
        cursor: DB cursor
        conn: DB connection 
    """
    try:
        conn=pyodbc.connect(connection_string)
    except Exception as e:
        raise Exception('Connection Failed')
    cursor = conn.cursor()
    return cursor,conn

def func_generate_employee_list_of_dict(connection_string,sql_query):
    """[summary]

    Args:
        connection_string ([type]): connection string object
        sql_query ([type]): [description]

    Returns:
        [type]: [description]
    """
    # connection to DB
    cursor,conn = connect_to_db(connection_string)
    # execute the query that is passed to the function
    cursor.execute(sql_query)
    # results list will contain the list of dictionaries obtained from output
    # and columns list will contain the headers
    results,columns_list= [], []
    for column in cursor.description:
        columns_list.append(column[0])
    
    # retrieve all records from cursor and start adding as separate dictionary items 
    records = cursor.fetchall()
    
    # iterate and create individual dictionaries based on the number of items returned from the query on DB
    for row in records:
        results.append(dict(zip(columns_list,row)))

    # close any DB connections which are open at the end of the method
    conn.close()
    return results

def func_generate_employee_dict(connection_string,sql_query):
    """

    Args:
        connection_string ([type]): connection string object
        sql_query ([type]): [description]

    Returns:
        dict: dictionary with results of key as the column names and values as the corresponding column values in separate rows
    """
    res = defaultdict(list)
    # connection to DB
    cursor,conn = connect_to_db(connection_string)
    # execute the query that is passed to the function
    cursor.execute(sql_query)
    columns_list = []
    for column in cursor.description:
        columns_list.append(column[0])
    records = cursor.fetchall()
    for row in records:
        for key,value in zip(columns_list,row):
            res[key].append(value)
    conn.close()
    return res

def main():
    sql_query = "select * from employee"
    connection_string = "CONNECTION_STRING_PARAMS"
    res_list_of_dict = func_generate_employee_list_of_dict(connection_string,sql_query)
    res_dict = func_generate_employee_dict(connection_string,sql_query)

if __name__ == "__main__":
    main()

"""
Solution to the programs from DB
# solution 2
# SELECT e1.*
# from employee e1
# left join employee e2
# on e1.employee_id = e2.employee_id
# and e1.effective_date<e2.effective_date
# where e2.effective_date is null 

# solution 1
# -- as per the details provided in question 1 employee profile change = 1 entry in the effective date column under the same employee group
# select e.employee_id, count(effective_date) as cnt_profile_change
# from employee e
# GROUP by e.employee_id
# having count(effective_date)>=2
"""