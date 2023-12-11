#!/usr/bin/python3


"""
model_state_fetch_all - module uses python ORM to connect to database and
select all states

"""


if __name__ == "__main__":
    """
    Fetch all states from named database
    """
    from model_state import State
    from sqlalchemy import create_engine
    from sqlalchemy.orm import sessionmaker, Query
    import sys
    from urllib.parse import quote_plus

    username = sys.argv[1]
    password = quote_plus(sys.argv[2])
    db_name = sys.argv[3]
    portnumber = 3306

    dbengine = create_engine("mysql+mysqldb://" +
                             "{}:{}@localhost:{}/{}"
                             .format(username,
                                     password,
                                     portnumber,
                                     db_name),
                             pool_pre_ping=True)
    # Base.metadata.create_all(dbengine)
    Session = sessionmaker(bind=dbengine)
    session = Session()

    new_state = State("Louisiana")
    session.add(new_state)
    session.commit()

    session.close()
