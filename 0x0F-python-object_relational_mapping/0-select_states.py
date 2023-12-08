#!/usr/bin/python3

"""
Script connects to database and runs query
"""

if __name__ == '__main__':
    """
    Connect to Database and select all from states table
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
    dbcursor.execute("SELECT * FROM states ORDER BY id ASC")
    query_rows = dbcursor.fetchall()
    for each_row in query_rows:
        print(each_row)
    dbcursor.close()
    dbconnection.close()
    # Consider refactoring to use pagination to handle cases
    # where the results dataset is large, see snippet below
    # batch_size = 1000
    # while True:
    #     rows = cursor.fetchmany(batch_size)
    #     if not rows:
    #         break
    #     for row in rows:
    #         # Process the row
