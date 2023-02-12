import os
import sqlite3


database = 'database.sqlite'



input1 = input('Do you want to run migration for bot database? Y/[n]: ')
if input1 == 'y':
    if os.path.exists(database):
        os.remove(database)
        print('[-] Database already exists. Deleting it.')

    conn = sqlite3.connect(database)
    print('[+] Database opened successfully.')

    conn.execute('''CREATE TABLE users
            (UserId       INTEGER PRIMARY KEY,
            username      STRING  NOT NULL,
            date          STRING  NOT NULL
            );''')

    print('[+] Table users created successfully.')



    conn.execute('''CREATE TABLE stats
        (instagram INT DEFAULT 0,
        twitter  INT DEFAULT 0,
        tiktok  INT DEFAULT 0,
        snapchat INT DEFAULT 0
        );''')

    conn.execute('INSERT INTO stats VALUES(0,0,0,0)')
    conn.commit()

    print('[+] Table Stats created successfully.')

    conn.close()
