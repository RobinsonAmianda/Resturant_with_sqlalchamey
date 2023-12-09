from sqlalchemy import create_engine,Column,String,Integer,ForeignKey
from sqlalchemy.orm import declarative_base,Session,relationship


engine = create_engine("sqlite:///Reviews.db")
Base = declarative_base()


class Restaurant(Base):
    __tablename__ = "restaurant"
    id = Column(Integer,primary_key = True)
    name = Column(String)
    price = Column(Integer)
    star_ratings = Column(Integer)

# Example for the Restaurant.   
    """R1 = Restaurant(name = "Doha",price = 45)
    session.add(R1)
    session.commit()
R1 = session.query(Restaurant).all()
print("Restaurant ID:", R1.id)
print("Restaurant Name:", R1.name)
print("Restaurant Price:$", R1.price)"""

class Customer(Base):
    __tablename__ = "customer"
    id = Column(Integer,primary_key = True)
    first_name = Column(String)
    last_name = Column(String)

    #Example of customer
    """c1 = Customer(first_name  ="Robinson",last_name ="Okusala")
    session.add(c1)
    session.commit()
    c1 = session.query(Customer).first()
    print("Customer id:",c1.id)
    print("Customer first_name:",c1.first_name)
    print("Customer last_name:",c1.last_name)"""  


class Review(Base):
    __tablename__ = "review"
    id = Column(Integer,primary_key = True)
    review_left = Column(String)
    restaurant_id = Column(Integer, ForeignKey('restaurant.id'))
    customer_id = Column(Integer,ForeignKey("customer.id"))

    #Relating the tables
    restaurant = relationship("Restaurant", back_populates="review")
    customer = relationship("Customer",back_populates="review")

#Creating tables
Base.metadata.create_all(engine)
session = Session(engine)

def Review_full_review(self):
    return self.restaurant.name self.first_name + self.last_name self.star_ratings  
