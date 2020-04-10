# SET SQL_SAFE_UPDATES = 0;

import mysql.connector

config = {
    'user'    : 'root',
    'password': '12e',
    'host'    : '192.168.56.101',
    'database': 'white_collar'
}

cnx = mysql.connector.connect(**config)
query = ''

file_names = ['create_setup.sql', 'insert_setup.sql']
# file_names = ['create_setup.sql']
# file_names = ['insert_setup.sql']
for file_name in file_names:
    with open(file_name, 'r') as page:
        query += " ".join(page.readlines())
        
cursor = cnx.cursor()
cursor.execute(query)
cursor.close()
cnx.close()

# myresult = cursor.fetchall()
# print(myresult)