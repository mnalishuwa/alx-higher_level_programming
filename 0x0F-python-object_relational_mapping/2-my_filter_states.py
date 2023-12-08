#!/usr/bin/python3

"""
lists all states with a name equal to state_name
"""

if __name__ == '__main__':

    """
    displays all values in the states which match state_name
    """
    import MySQLdb
    import sys

    username = sys.argv[1]
    password = sys.argv[2]
    database_name = sys.argv[3]
    state_name = sys.argv[4]
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
                     "WHERE name COLLATE utf8mb4_bin = " +
                     "'{}' ORDER BY id ASC".format(state_name))
    # COLLATE name to ensure case sensitivity during comparison
    query_rows = dbcursor.fetchall()
    for each_row in query_rows:
        print(each_row)
    dbcursor.close()
    dbconnection.close()
