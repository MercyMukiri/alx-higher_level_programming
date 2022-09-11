#!/usr/bin/python3
"""This script takes in arguments and displays all values
in the states table of hbtn_0e_0_usa where name matches the argument.
But this time, the script is safe from MySQL injections"""

import MySQLdb
from sys import argv


if __name__ == "__main__":
    conn = MySQLdb.connect(host="localhost", port=3306, user=argv[1],
                           passwd=argv[2], db=argv[3], charset="utf8")
    cur = conn.cursor()
    cur.execute("SELECT * FROM states WHERE BINARY name = %s ORDER BY id ASC",
                (argv[4],))
    rows = cur.fetchall()

    for row in rows:
        print(row)

    cur.close()
    conn.close()
