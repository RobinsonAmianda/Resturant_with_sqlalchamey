from sqlalchemy import create_engine,Column,String,Integer,ForeignKey
from sqlalchemy.orm import Session,declarative_base,relationship

engine = create_engine("sqlite:///Customers.db")
Base = declarative_base()

class Review(base):
    __tablename__ = "review"
    id = Column(Integer,primary_key = True)
    review_left = Column(String)

class Restaurant(Base):
    __tablename__ = "restaurant"
    id = Column(Integer,primary_key = True)
    name = Column(String)
    star_ratings = Column(Integer) 

class Customer(Base):
    __tablename__ = "customer"
    id = Column(Integer,primary_key = True)
    first_name = Column(String)
    last_name = Column(String)
    review_left = Column(Integer,ForeignKey(review_left))
    restaurant_name = Column(Integer,ForeignKey(restaurant_name))

    #Relating the tables
    review = relationship("Review",back_populates = "Customer")
    restaurant = relationship("Restaurants",back_populates = "Restaurants")

    #Creating the tables
    Base.metadata.create_all(engine)
    session = Session(engine)

    def Customer_reviews(self):
        return self.review_left
    def Customer_restaurants(self):
        return self.restaurant
    def Customer_full_name(self):
        return self.first_name + self.last_name
    def Customer_favorite_restaurant(self):
        return max(self.star_ratings)
    def Customer_add_review(self,restaurant, rating):
        new_review = (self.restaurant = restaurant,self.rating = rating)
        return restaurant.review.append(new_review)
    def Customer_delete_reviews(self,restaurant):
        for review in reviews:
            review.clear()











    