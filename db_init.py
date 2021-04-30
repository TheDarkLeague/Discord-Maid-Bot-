import sqlite3

conn = sqlite3.connect('player.db')
print('Opened database successfully')

conn.execute('''
CREATE TABLE PLAYER
(
       ID INT PRIMARY KEY     NOT NULL,
       PLAYERNAME     TEXT    NOT NULL,
       TYPE           TEXT    NOT NULL,
       LEVEL          INT     NOT NULL,
       ENERGON        INT     NOT NULL,
       GOLD           INT     NOT NULL
);
       ''')

conn.execute('''
CREATE TABLE PLAYERWEAPON
(
       ID INT PRIMARY KEY     NOT NULL,
       WEAPONID       INT     NOT NULL,
       WEAPONNAME     TEXT    NOT NULL,
       WEAPONTYPE     TEXT    NOT NULL,
       PLAYERID       INT     NOT NULL     REFERENCES PLAYER(ID) ON DELETE CASCADE
);
       ''')

print('Table created successfully')

conn.close()