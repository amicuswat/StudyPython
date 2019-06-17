import psycopg2

dbname = "dbname='database1' user='postgres' password='root' host='localhost' port='5432'"

def create_table():
    connection = psycopg2.connect(dbname)
    cur = connection.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS store (item TEXT, quantity INTEGER, price REAL)")
    connection.commit()
    connection.close()

def insert(item, quantity, price):
    connection = psycopg2.connect(dbname)
    cur = connection.cursor()
    cur.execute("INSERT INTO store VALUES (%s, %s, %s)", (item, quantity, price))
    connection.commit()
    connection.close()

def view():
    connection = psycopg2.connect(dbname)
    cur = connection.cursor()
    cur.execute("SELECT * FROM store")
    rows = cur.fetchall()
    connection.close()
    return rows

def delete(item):
    connection = psycopg2.connect(dbname)
    cur = connection.cursor()
    cur.execute("DELETE FROM store WHERE item=%s",(item,))
    connection.commit()
    connection.close()

def update(quantity, item):
    connection = psycopg2.connect(dbname)
    cur = connection.cursor()
    cur.execute("UPDATE store SET quantity=%s WHERE item=%s",(quantity, item,))
    connection.commit()
    connection.close()

create_table()
#insert("Suger1", 12, 2.25)
for row in view():
    print(row)
print('=' * 10)
update(4, "Milk")
for row in view():
    print(row)
