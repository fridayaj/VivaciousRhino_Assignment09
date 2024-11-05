# main.py
import random
import pyodbc

from connectionPackage.connection import *
try:
    conn = connection()
    cursor = conn.cursor()

except Exception as e:
    # I'd like to know more
    print("Error accessing database")
    print(e)
    exit() # give up

query_string = "SELECT ProductID, [UPC-A ], Description, ManufacturerID, BrandID FROM tProduct"
print(query_string)
results = cursor.execute(query_string)
print(results)
for row in results.fetchall():
    print(row[2])

