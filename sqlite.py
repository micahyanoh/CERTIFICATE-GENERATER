import sqlite3
conn=sqlite3.connect('students.db')
cur=conn.cursor()
def create_student():
    try:
        cur.execute("""CREATE TABLE students(
            adm_no TEXT,
            first_name TEXT,
            last_name TEXT, 
            email TEXT,
            phone TEXT, 
            CONSTRAINT Std_Details PRIMARY KEY(adm_no,email,phone)
            
            )""")
        conn.commit()
    except :
        pass
    #cur.execute("INSERT INTO students VALUES('Alfonce','Micah Yano','ogongoyanojnr@gmail.com')")
create_student()
#cur.execute("INSERT INTO students VALUES('Alfonce','Micah Yano','ogongoyanojnr@gmail.com')")

conn.commit()
conn.close()