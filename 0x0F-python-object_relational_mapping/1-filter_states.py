#!/usr/bin/python3
"""
lists all states with a name starting with N
"""

if __name__ == '__main__':

    """
    lists all states with a name starting with N
    """
    import MySQLdb
    import sys

    username = sys.argv[1]
    password = sys.argv[2]
    database_name = sys.argv[3]
    host_name = 'localhost'
    port_number = 3306

    dbconnection = MySQLdb.connect(host=host_name,
                                   port=port_number,
                                   user=username,
                                   passwd=password,
                                   db=database_name,
                                   charset='utf8')
    dbcursor = dbconnection.cursor()
    dbcursor.execute("SELECT * FROM states " +
                     "WHERE name COLLATE utf8mb4_bin " +
                     "LIKE 'N%' ORDER BY id ASC")
    query_rows = dbcursor.fetchall()
    for each_row in query_rows:
        print(each_row)
    dbcursor.close()
    dbconnection.close()
