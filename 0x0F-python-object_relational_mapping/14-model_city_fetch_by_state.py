#!/usr/bin/python3

"""
Script Module fetches all cities from database
"""

if __name__ == "__main__":
    """
    Import required packages and query the cities table
    """
    from model_city import City
    from model_state import Base, State
    from sqlalchemy import create_engine
    from sqlalchemy.orm import sessionmaker
    import sys
    from urllib.parse import quote_plus

    username = sys.argv[1]
    password = quote_plus(sys.argv[2])
    dbname = sys.argv[3]
    portnumber = 3306

    dbengine = create_engine("mysql+mysqldb://" +
                             "{}:{}@localhost:{}/{}".
                             format(username,
                                    password,
                                    portnumber,
                                    dbname),
                             pool_pre_ping=True)
    Base.metadata.create_all(dbengine)
    
    Session = sessionmaker(bind=dbengine)
    session = Session()

    for city, state in (
            session.query(City, State).
            filter(City.state_id == State.id).
            order_by(City.id).all()
            ):
        print(f"{state.name}: ({city.id}) {city.name}")
