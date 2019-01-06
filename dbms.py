import sqlite3 as lite
con = lite.connect('user.db')
with con:
    cur = con.cursor()
    cur.execute("drop table usr1")
    cur.execute("create table usr1(roll INT,Name TEXT,marks INT)")
    cur.execute("insert into usr1 values(1,'akhilaa',67)")
    cur.execute("insert into usr1 values(2,'mariet',34)")
    cur.execute("insert into usr1 values(3,'gopikaa',68)")

with con:
    cur = con.cursor()
    cur.execute("select * from usr1")
    rows = cur.fetchall()
    for row in rows:
        print(row)
    print("records with marks>60")
    cur.execute("select * from usr1 where marks>60")
    rows = cur.fetchall()
    for row in rows:
        print(row)
    
