from sqlalchemy import creating_engine,Column,String,Integer,ForeignKey
from sqlalchemy.orm import Session,declarative_base,relationship

engine = creating_engine("sqlite:///Restaurant.db")
Base = declarative_base

class Review(Base):
    __tablename__ = "reviews"
    id = Column(Integer,primary_key = True)
    name = Column(String)

class Customer(Base):
    __tablename__ = "customers"
    id = Column(Integer,primary_key = True)
    first_name = Column(String)
    last_name = Column(Integer)

class Restaurant(Base):
    __tablename__ = "restaurants"
    id = Column(Integer,primary_key = True)
    name = Column(String)
    price = Column(Integer)
    review_id = Column(Integer,ForeignKey("review.id"))
    customer_id = Column(Integer,ForeignKey("customer.id"))

    #Relating the tables.
    reviews = relationship("Reviews",back_populate = "Restaurant")
    customers = relationship("Customers",back_populate = "Restaurant")

    #creating tables
    Base.metadata.create_all(engine)
    session = Session(engine)