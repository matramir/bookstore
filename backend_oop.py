import sqlite3
class Database:
    def __init__(self, db):
        self.conn=sqlite3.connect(db)
        self.cur=self.conn.cursor()
        self.cur.execute("CREATE TABLE IF NOT EXISTS  book (id INTEGER PRIMARY KEY, title TEXT, author TEXT, year INTEGER, isbn INTEGER)")
        self.conn.commit()

    def insert(title, author, year, isbn):
        self.cur.execute("INSERT INTO book VALUES(null,?,?,?,?)",(title, author, year, isbn))
        self.conn.commit()

    def view(self):
        self.cur.execute("SELECT * FROM book")
        rows = self.cur.fetchall()
        return rows

    def search(self, title="", author="", year="", isbn=""):
        self.cur.execute("SELECT * FROM book WHERE year=? OR author=? OR year=? OR isbn=?", (title, author, year, isbn))
        rows = self.cur.fetchall()
        return rows

    def delete(self, id):
        self.cur.execute("DELETE FROM book WHERE id=?",(id, ))
        self.conn.commit()

    def update(self, id, title, author, year, isbn):
        self.cur.execute("UPDATE book SET title=?, author=?, year=?, isbn=? WHERE id=?",(id, title, author, year, isbn))
        self.conn.commit()
        
    def __del__(self):
        self.conn.close()
