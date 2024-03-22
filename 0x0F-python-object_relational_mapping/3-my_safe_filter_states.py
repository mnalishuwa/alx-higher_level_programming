#!/usr/bin/python3

"""
lists all states with a name equal to state_name
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
    state_name = sys.argv[4]
    host_name = 'localhost'
    port_number = 3306

    dbconnection = MySQLdb.connect(host=host_name,
                                   port=port_number,
                                   user=username,
                                   passwd=password,
                                   db=database_name,
                                   charset='utf8')
    sql_query = "SELECT * FROM states WHERE name = %s"

    dbcursor = dbconnection.cursor()
    # use parameterized queries to treat args as params
    # to help prevent sql injects, can also use prepared
    # queries if supported by connector or API
    dbcursor.execute(sql_query, (state_name,))
    query_rows = dbcursor.fetchall()
    for each_row in query_rows:
        print(each_row)

    dbcursor.close()
    dbconnection.close()
