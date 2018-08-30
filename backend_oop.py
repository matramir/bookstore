import sqlite3
class Database:
    def __init__(self, db):
        conn=sqlite3.connect(db)
        cur=conn.cursor()
        cur.execute("CREATE TABLE IF NOT EXISTS  book (id INTEGER PRIMARY KEY, title TEXT, author TEXT, year INTEGER, isbn INTEGER)")
        conn.commit()
        conn.close()

    def insert(title, author, year, isbn):
        conn=sqlite3.connect("books.db")
        cur=conn.cursor()
        cur.execute("INSERT INTO book VALUES(null,?,?,?,?)",(title, author, year, isbn))
        conn.commit()
        conn.close()

    def view(self):
        conn=sqlite3.connect("books.db")
        cur=conn.cursor()
        cur.execute("SELECT * FROM book")
        rows = cur.fetchall()
        conn.close()
        return rows

    def search(self, title="", author="", year="", isbn=""):
        conn=sqlite3.connect("books.db")
        cur=conn.cursor()
        cur.execute("SELECT * FROM book WHERE year=? OR author=? OR year=? OR isbn=?", (title, author, year, isbn))
        rows = cur.fetchall()
        conn.close()
        return rows

    def delete(self, id):
        conn=sqlite3.connect("books.db")
        cur=conn.cursor()
        cur.execute("DELETE FROM book WHERE id=?",(id, ))
        conn.commit()
        conn.close()

    def update(self, id, title, author, year, isbn):
        conn=sqlite3.connect("books.db")
        cur=conn.cursor()
        cur.execute("UPDATE book SET title=?, author=?, year=?, isbn=? WHERE id=?",(id, title, author, year, isbn))
        conn.commit()
        conn.close()
