from sqlalchemy import create_engine, Column, String, Integer, ForeignKey
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy.ext.declarative import declarative_base


engine = create_engine("sqlite:///test.db", echo=False)
Session = sessionmaker(bind=engine)
session = Session()
Base = declarative_base()


class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    phone = relationship("PhoneNumbers", back_populates='users')


class PhoneNumbers(Base):
    __tablename__ = 'phones'

    id = Column(Integer, primary_key=True)
    phone_number = Column(String, nullable=False)
    user_id = Column(Integer, ForeignKey("users.id"))   
    users = relationship("User", back_populates='phone')


Base.metadata.create_all(engine)
