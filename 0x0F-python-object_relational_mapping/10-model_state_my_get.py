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
    from sqlalchemy.orm import sessionmaker
    import sys
    from urllib.parse import quote_plus

    username = sys.argv[1]
    password = quote_plus(sys.argv[2])
    db_name = sys.argv[3]
    portnumber = 3306
    statename = sys.argv[4]

    # Refactor to handle connection errors
    dbengine = create_engine("mysql+mysqldb://" +
                             "{}:{}@localhost:{}/{}"
                             .format(username,
                                     password,
                                     portnumber,
                                     db_name),
                             pool_pre_ping=True)

    Session = sessionmaker(bind=dbengine)
    session = Session()

    state = session.query(State).\
        filter(State.name == statename).order_by(State.id).first()

    if state:
        print("{:d}".format(state.id))
    else:
        print("Not found")

    session.close()
