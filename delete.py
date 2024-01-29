import mysql.connector
import random
from datetime import datetime

conn = mysql.connector.connect(user='root', password='MYpassword.2024',
                              host='127.0.0.1',
                              database='sys')

cursor = conn.cursor()

delete_query = f'DELETE FROM new_table'
cursor.execute(delete_query)

print("Finished deleting...")

cursor = conn.cursor()
conn.commit()