import psycopg2

def create_table():
    conn=psycopg2.connect("dbname='database1' user='postgres' password='heslo' host='localhost' port='5432'")
    cur=conn.cursor()
    cur.execute('CREATE TABLE IF NOT EXISTS store (item TEXT, quantity INTEGER, price REAL)')
    conn.commit()
    conn.close()

def insert(item,quantity,price):
    conn=psycopg2.connect("dbname='database1' user='postgres' password='heslo' host='localhost' port='5432'")
    cur=conn.cursor()
    cur.execute("INSERT INTO store VALUES (%s,%s,%s)", (item,quantity,price))
    conn.commit()
    conn.close()

def view():
    conn=psycopg2.connect("dbname='database1' user='postgres' password='heslo' host='localhost' port='5432'")
    cur=conn.cursor()
    cur.execute('select * from store')
    rows=cur.fetchall()
    conn.close()
    return rows

def delete(item):
    conn=psycopg2.connect("dbname='database1' user='postgres' password='heslo' host='localhost' port='5432'")
    cur=conn.cursor()
    cur.execute('delete from store where item=%s',(item,))
    conn.commit()
    conn.close()

def update(quantity,price,item):
    conn=psycopg2.connect("dbname='database1' user='postgres' password='heslo' host='localhost' port='5432'")
    cur=conn.cursor()
    cur.execute('update store set quantity=%s, price=%s where item=%s',(quantity,price,item))
    conn.commit()
    conn.close()
#insert('Orange',10,15)
#create_table()
#update(11,6,'water Glass')
#insert('Coffee Cup',10,5)
#delete('Orange')
update(20,15.0,'Apple')
print(view())
