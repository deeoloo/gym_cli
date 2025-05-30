from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

Base = declarative_base()
engine = create_engine('sqlite:///app/db/gym.db')
Session = sessionmaker(bind=engine, expire_on_commit=False)