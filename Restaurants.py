from sqalchemy import create_engine,Column,String,Integer,ForeignKey
from sqlalchemy.orm import Session,declarative_base,relationship

engine = creating_engine("sqlite:///Restaurants.db")
Base = declarative_base

class Review(Base):
    __tablename__ = "review"
    id = Column(Integer,primary_key = True)
    review_left  = Column(String)

class Customer(Base):
    __tablename__ = "customer"
    id = Column(Integer,primary_key = True)
    first_name = Column(String)
    last_name = Column(Integer)

class Restaurant(Base):
    __tablename__ = "restaurant"
    id = Column(Integer,primary_key = True)
    name = Column(String)
    price = Column(Integer)
    star_ratings = Column(Integer)
    review_left = Column(Integer,ForeignKey("review_left"))
    customer_first_name = Column(Integer,ForeignKey("customer_first_name"))

    #Relating the tables.
    reviews = relationship("Reviews",back_populate = "Restaurant")
    customers = relationship("Customers",back_populate = "Restaurant")

    #creating tables
    Base.metadata.create_all(engine)
    session = Session(engine)

    def Restaurant_reviews(self):
        return self.review_left
    def Restaurant_customers(self):
        return self.customer
    def Restaurant_fanciest(self):
        for price in restaurants:
            highest_price = max(restaurant.price)
        return highest_price
    def Restaurant_all_reviews(self):
       for review in reviews:
        return {self.restaurant.name} {self.first_name + self.last_name} {self.star_ratings} 









    

    