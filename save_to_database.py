#import torch
import mysql.connector
from datetime import datetime
import model
import random

def connect_to_database(image_path):

    conn = mysql.connector.connect(user='root', password='MYpassword.2024',
                              host='127.0.0.1',
                              database='sys')

    cursor = conn.cursor()

    current_time = datetime.now()
    formatted_datetime = current_time.strftime('%Y-%m-%d %H:%M:%S')
    print(formatted_datetime)

    pain_value = model.get_pain_value(image_path)
    #pain_value = random.randint(0,9)

    # Example value to insert (current time and a number)
    insert_values = (formatted_datetime, pain_value)

    sql = "INSERT INTO new_table (time_column, int_column) VALUES (%s, %s)"
    cursor.execute(sql, insert_values)

    cursor = conn.cursor()
    conn.commit()

    # Execute a SELECT query to retrieve the time value
    select_query = "SELECT * FROM new_table"
    cursor.execute(select_query)

    # Fetch and display all the results
    '''
    rows = cursor.fetchall()
    for row in rows:
        print(f"Time: {row[0]}, Pain value: {row[1]}")
    '''

    # Fetch and display the most recent result
    rows = cursor.fetchall()
    print(f"Time: {rows[-1][0]}, Pain value: {rows[-1][1]}")
    return int(rows[-1][1])
