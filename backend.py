import sqlite3

def connect():  
   con=sqlite3.connect("store.db")
   cur=con.cursor()
   cur.execute("create table  IF NOT EXISTS books_store(id integer primary key,title text,author text,year integer,isbn integer)")
   con.commit()
   con.close()


def insert(title,author,year,isbn):
    con=sqlite3.connect("store.db")
    cur=con.cursor()
    cur.execute("insert into books_store values(NULL,?,?,?,?)",(title,author,year,isbn))
    con.commit()
    con.close()

def view():
    con=sqlite3.connect("store.db")
    cur=con.cursor()
    cur.execute("select * from books_store")
    rows=cur.fetchall();
    con.close()
    return rows
    

def search(title="",author="",year="",isbn=""):
    con=sqlite3.connect("store.db")
    cur=con.cursor()
    cur.execute("select * from books_store where title=? or author=? or year=? or isbn=?",(title,author,year,isbn))
    rows=cur.fetchall();
    con.close()
    return rows





def delete(id):
    con=sqlite3.connect("store.db")
    cur=con.cursor()
    cur.execute("delete from books_store where id=?",(id,))
    con.commit()
    con.close()


def Update(id,title,author,year,isbn):
    con=sqlite3.connect("store.db")
    cur=con.cursor()
    cur.execute("update books_store  set title=?,author=?, year=?,isbn=? where id=?",(title,author,year,isbn,id))
    con.commit()
    con.close()

connect()


