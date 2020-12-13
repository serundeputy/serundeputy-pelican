# Migrate the data from the Backdrop serundeputy-api
import datetime
import mysql.connector
import sys

conn = mysql.connector.connect(
    user = 'backdrop',
    password = 'backdrop',
    host = '127.0.0.1',
    database = 'backdrop',
    port = '32819'
)

cursor = conn.cursor()
cursor.execute(
    """select * from node where status = 1 and (type = 'page' or type ='article')"""
)
data = cursor.fetchall()

def get_body(datum):
    entity_id = datum[0]
    cursor.execute(
        """select body_value from field_data_body where entity_id = %s""",
        (entity_id,)
    )
    body = cursor.fetchall()

    return body[0][0]

original_stdout = sys.stdout
for datum in data:
    name = datum[4]
    url_name = name.replace("{", "")
    url_name = url_name.replace("}", "")
    url_name = url_name.strip()
    url_name = url_name.replace(" ", "-")
    body = get_body(datum).replace(r'\r','')
    date = datum[7]
    print(datum)
    print(body)
    file_object = open('content/blog/' + url_name + '.md', 'x')
    sys.stdout = file_object
    print("Title: " + name)
    print("Date: " + datetime.datetime.fromtimestamp(date).strftime('%Y-%m-%d'))
    print("Category: blog")
    print("\n")
    print(body)
    file_object.close()
    sys.stdout = original_stdout

conn.close()


