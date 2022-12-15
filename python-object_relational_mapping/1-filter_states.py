#!/usr/bin/python3
"""filter states"""


import MySQLdb
from sys import argv

if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost", port=3306, user=argv[0], passwd=argv[1], db=argv[2])
    cursor = db.cursor()
    cursor.executre("SELECT * FROM states WHERE name LIKE 'N%' ORDER BY id ASC")
    my_list = cursor.fetchall()
    for j in my_list:
        if j[0][0] == 'N':
            print(j)
    cursor.close()
    db.close()
