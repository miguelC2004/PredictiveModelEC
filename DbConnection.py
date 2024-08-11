import mysql.connector

def GetConnection():
    return mysql.connector.connect(
        host='localhost',
        user='root',
        password='',
        database='ecommerceconceptual'
    )
