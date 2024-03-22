#!/usr/bin/python3

"""
lists all cities from the database
Uses Prepared statements to avoid SQL injections
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
    host_name = 'localhost'
    port_number = 3306

    dbconnection = MySQLdb.connect(host=host_name,
                                   port=port_number,
                                   user=username,
                                   passwd=password,
                                   db=database_name,
                                   charset='utf8')
    sql_query = ("SELECT cities.id, cities.name, states.name " +
                 "FROM cities LEFT JOIN states " +
                 "ON cities.state_id = states.id " +
                 "ORDER BY id ASC")

    dbcursor = dbconnection.cursor()
    dbcursor.execute(sql_query)
    query_rows = dbcursor.fetchall()
    for each_row in query_rows:
        print(each_row)

    dbcursor.close()
    dbconnection.close()
