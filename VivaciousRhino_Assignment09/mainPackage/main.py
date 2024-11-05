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

    # Step One
query_string = "SELECT ProductID, [UPC-A ], Description, ManufacturerID, BrandID FROM tProduct"
print(query_string)

    # Step Two
results = cursor.execute(query_string).fetchall()
random_row = random.choice(results)
print(random_row)
manufacturer_id = random_row[3]
brand_id = random_row[4]
print("Manufacturer ID = " + str(manufacturer_id) + " Brand ID = " + str(brand_id))

    # Step Three