import sqlite3


def fetusdeletus():
    with sqlite3.connect("guestbook_database0.db") as connection:
    
        c = connection.cursor
        c.execute(items)
        results = c.fetchall()
        dela = "DELETE FROM Guestbook (ID) values (?);"
        bruh = int(input("who u wanna delete"))
        c.execute(dela)
        tuple_insert = (Names)
        for dela in results:
            print(dela)

def addusadidas():
    with sqlite3.connect("guestbook_database0.db") as connection:
        c = connection.cursor
        names = input("what do u wanna be called\n")
        comment = input("what u wanna say hoe\n")

        output = ("INSERT INTO Guestbook (Names, Comments)  values(?,?);")
        tuple_insert = (names, comment)
        c.execute(output,tuple_insert)


with sqlite3.connect("guestbook_database0.db") as connection:
    while True:
        c = connection.cursor()
        items = "SELECT ID, Names, Comments FROM Guestbook"
        c.execute(items)
        results = c.fetchall()
        for items in results:
            print(items)

        x = input("Watchu want bruh\n")
        if x == ("add"):
            addusadidas()
        elif x == ("remove"):
            fetusdeletus()        