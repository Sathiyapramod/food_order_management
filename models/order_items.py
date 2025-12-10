from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship
from db.database import Base


class OrderItems(Base):
    __tablename__ = "order_items"

    id = Column(Integer, primary_key=True)
    quantity = Column(Integer)
    
    # foreign keys 
    order_id = Column(Integer,ForeignKey("orders.order_id"))
    food_id = Column(Integer, ForeignKey("foods.id"))
    # relationship
    some_variable = relationship("Orders")
    some_food = relationship("Foods")