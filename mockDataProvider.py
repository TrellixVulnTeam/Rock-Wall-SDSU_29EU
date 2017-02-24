import datetime
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from databaseDefinition import *
 
engine = create_engine('sqlite:///RockWallDatabase.db', echo=True)
 
# create a Session
Session = sessionmaker(bind=engine)
session = Session()
 
user = User("employee@gmail.com","employee", "employee")
session.add(user)
 
user = User("admin@gmail.com","administrator", "administrator")
session.add(user)
 
user = User("master@gmail.com","master", "master")
session.add(user)
 
# commit the record the database
session.commit()
 
session.commit()