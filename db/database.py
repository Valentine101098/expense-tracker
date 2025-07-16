from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models.expense import Base


#create an engine
engine = create_engine('sqlite:///expenses.db')

#create the tables
Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)