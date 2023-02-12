import sqlite3
import secrets
from datetime import datetime


class dbQuery():
    def __init__(self, db):
        self.db = db

    #: Add the user into the database if not registered
    def setUser(self, userId,username):
        chatType = 'users' 
        con = sqlite3.connect(self.db)
        cur = con.cursor()

        isRegistered = cur.execute(f'SELECT * FROM users WHERE userId={userId}').fetchone()
        con.commit()

        isRegistered = True if isRegistered else False

        if not isRegistered:       
            cur.execute(f"Insert into users (userId,username,date) values ({userId} ,\"{username}\", \"{datetime.today().strftime('%d/%m/%Y, %H:%M:%S')}\")")
            con.commit()

        return isRegistered



    #: Get all the registered users
    def getAllUsers(self):
        con = sqlite3.connect(self.db)
        con.row_factory = lambda cursor, row: row[0]
        cur = con.cursor()

        users = cur.execute(f'SELECT userId FROM users').fetchall()
        con.commit()

        return users if users else None

    #: Get all the users with date
    def getAllUsersDate(self):
        con = sqlite3.connect(self.db)
        cur = con.cursor()

        users = cur.execute(f'SELECT * FROM users').fetchall()
        con.commit()
        return users if users else None


    #: Increase stats count
    def increaseCounter(self, type):
        con = sqlite3.connect(self.db)
        cur = con.cursor()

        cur.execute(f'UPDATE stats SET {type}={type}+1')
        con.commit()


#: Return query as dictionary
# https://stackoverflow.com/a/3300514/13987868
def dict_factory(cursor, row):
    d = {}
    for idx, col in enumerate(cursor.description):
        d[col[0]] = row[idx]

    return d
