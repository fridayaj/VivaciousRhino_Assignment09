# Name: Greyson Barber
# email:  barbergn@mail.uc.edu
# Assignment Number: Assignment 09
# Due Date: 11/7/24
# Course #/Section: IS4010-001
# Semester/Year: Fall 2024
# Brief Description of the assignment: Collabing as a team to pull code and create queries.

# Brief Description of what this module does: This module extracts data froma database and produces results as required. 
# Citations: none
# Anything else that's relevant: none

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
product_id = random_row[0]
print("Manufacturer ID = " + str(manufacturer_id) + " Brand ID = " + str(brand_id))


manufacturer_query = f"SELECT Manufacturer FROM tManufacturer WHERE ManufacturerID = {manufacturer_id}" 
manufacturer_name = cursor.execute(manufacturer_query).fetchone()[0] 


brand_query = f"SELECT Brand FROM tBrand WHERE BrandID = {brand_id}" 
brand_name = cursor.execute(brand_query).fetchone()[0]


 


