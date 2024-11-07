# Name: Greyson Barber | Kyle Hsu
# email:  barbergn@mail.uc.edu | hsukt@mail.uc.edu
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

query_string = "SELECT ProductID, [UPC-A ], Description, ManufacturerID, BrandID FROM tProduct"

results = cursor.execute(query_string).fetchall()
random_row = random.choice(results)
manufacturer_id = random_row[3]
brand_id = random_row[4]
product_id = random_row[0]
description = random_row[2]


manufacturer_query = f"SELECT Manufacturer FROM tManufacturer WHERE ManufacturerID = {manufacturer_id}" 
manufacturer_name = cursor.execute(manufacturer_query).fetchone()[0] 


brand_query = f"SELECT Brand FROM tBrand WHERE BrandID = {brand_id}" 
brand_name = cursor.execute(brand_query).fetchone()[0]

items_sold_query = f"""
            SELECT TOP (100) PERCENT SUM(dbo.tTransactionDetail.QtyOfProduct) AS NumberOfItemsSold
            FROM dbo.tTransactionDetail
            INNER JOIN dbo.tTransaction ON dbo.tTransactionDetail.TransactionID = dbo.tTransaction.TransactionID
            WHERE (dbo.tTransaction.TransactionTypeID = 1) AND (dbo.tTransactionDetail.ProductID = {product_id})
        """
number_of_items_sold = cursor.execute(items_sold_query).fetchone()[0] or 0  # Default to 0 if result is None

sentence = (
            f"The product '{description}', made by {manufacturer_name} and branded by {brand_name}, "
            f"has sold a total of {number_of_items_sold} units."
            )
        
print(sentence)



 


