from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'

    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    email = Column(String(250), nullable=False)
    picture = Column(String(250))

    @property
    def serialize(self):
       return {
           'name'         : self.name,
           'id'           : self.id,
           'email'        : self.email,
           'picture'      : self.picture,
       }

class Arrangement(Base):
    __tablename__ = 'arrangement'

    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    description = Column(String(250))
    base_price = Column(String(8), nullable=False)
    user_id = Column(Integer,ForeignKey('user.id'))

    @property
    def serialize(self):
       return {
           'name'         : self.name,
           'id'           : self.id,
           'description'  : self.description,
           'base_price'   : self.base_price,
           'user_id'      : self.user_id,
       }

class Flower(Base):
    __tablename__ = 'flower'


    name =Column(String(80), nullable = False)
    id = Column(Integer, primary_key = True)
    description = Column(String(250))
    price = Column(String(8))
    arrangement_id = Column(Integer,ForeignKey('arrangement.id'))
    arrangement = relationship(Arrangement)
    user_id = Column(Integer,ForeignKey('user.id'))


    @property
    def serialize(self):
       """Return object data in easily serializeable format"""
       return {
           'name'         : self.name,
           'description'         : self.description,
           'id'         : self.id,
           'price'         : self.price,
           'user_id'        : self.user_id,
       }



engine = create_engine('sqlite:///floralArrangements.db')


Base.metadata.create_all(engine)
