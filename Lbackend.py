import sqlite3

def connect():
    conn = sqlite3.connect('library.db')
    cur = conn.cursor()

    cur.execute("CREATE TABLE IF NOT EXISTS BOOK_T(Id INTEGER PRIMARY KEY, Title TEXT NOT NULL , Author TEXT NOT NULL, Year INTEGER, ISBN INTEGER NOT NULL)")

    conn.commit()
    conn.close()

def insert(title,auth,year,isbn):
    conn = sqlite3.connect('library.db')
    cur = conn.cursor()
    
    cur.execute("INSERT INTO BOOK_T VALUES(NULL,?,?,?,?)",(title,auth,year,isbn))
    conn.commit()
    conn.close()

def delete(id):
    conn = sqlite3.connect('library.db')
    cur = conn.cursor()

    cur.execute("DELETE FROM BOOK_T WHERE Id =? ",(id,))
    conn.commit()
    conn.close()

def view():
    conn = sqlite3.connect('library.db')
    cur = conn.cursor()

    cur.execute("SELECT * FROM BOOK_T")
    rows = cur.fetchall()
    conn.commit()
    conn.close()

    return rows

def update(id,title,auth,year,isbn):
    conn = sqlite3.connect('library.db')
    cur = conn.cursor()

    cur.execute("UPDATE BOOK_T SET Title=?,Author=?,Year=?,ISBN =? WHERE Id=?",(title,auth,year,isbn,id))
    conn.commit()
    conn.close()

def search(title,auth,year,isbn):
    conn = sqlite3.connect('library.db')
    cur = conn.cursor()

    cur.execute("SELECT * FROM BOOK_T WHERE Title=? OR Author=? OR Year=? OR ISBN =?",(title,auth,year,isbn))
    rows = cur.fetchall()
    conn.commit()
    conn.close()

    if len(rows)>0:
        return rows
    else:
        return 0





#insert('Heavens','Sabrina Williams',2010,93821)
#insert('Judgement','Sabrina John',2013,36274)
#insert('Brooklyn','Dandy Sony',2007,17544)
#insert('Summer Saga','Anaya Willis',2000,11234)
#insert('Dark Tide','Angelina Smith',2011,15251)
#delete('','',1998,'')
#update(9,'The Sunrise','Henry Johns',2019,92835)
connect()
print(view())