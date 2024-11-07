# Name: Aidan Friday
# email:  fridayaj@mail.uc.edu
# Assignment Number: Assignment 09
# Due Date: 11/7/24
# Course #/Section: IS4010-001
# Semester/Year: Fall 2024
# Brief Description of the assignment: Collabing as a team to pull code and create queries.

# Brief Description of what this module does: This module connects to databse from prompt. 
# Citations: Bill Nicholson
# Anything else that's relevant: none


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
