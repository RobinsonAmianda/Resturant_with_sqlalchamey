from sqlalchemy import create_engine,Column,String,Integer,ForeignKey
from sqlalchemy.orm import Session,declarative_base,relationship

engine = create_engine("sqlite:///Customers.db")
Base = declarative_base()

class Review(base):
    __tablename__ = "review"
    id = Column(Integer,primary_key = True)
    review_made = Column(String)

class Restaurant(Base):
    __tablename__ = "restaurant"
    id = Column(Integer,primary_key = True)
    name = Column(String)

class Customer(Base):
    __tablename__ = "customer"
    id = Column(Integer,primary_key = True)
    first_name = Column(String)
    last_name = Column(String)
    review_id = Column(Integer,ForeignKey =(review.id))
    restaurant.id = Column(Integer,ForeignKey =(restaurant.id))

    #Relating the tables
    review = relationship("Review",back_populates = "Customer")
    restaurant = relationship("Restaurants",back_populates = "Restaurants")

    #Creating the tables
    Base.metadata.create_all(engine)
    session = Session(engine)