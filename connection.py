import sqlite3
def Database():
    global conn,cursor
    conn=sqlite3.connect('students.db')
    cursor=conn.cursor()
    