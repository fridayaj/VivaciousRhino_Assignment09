# connection.py

import pyodbc

def connection():
    """
    Connect to database
    @return connection object: the open connection
    """
    try:
        conn = pyodbc.connect('Driver={SQL Server};'
                              'Server=lcb-sql.uccob.uc.edu\\nicholdw;'
                              'Database=GroceryStoreSimulator;'
                              'uid=IS4010Login;'
                              'pwd=P@ssword2;')
    except:
        conn = None

    return conn
