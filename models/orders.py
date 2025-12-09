from sqlalchemy import Column, Integer
from sqlalchemy.orm import relationship
from db.database import Base


class Orders(Base):

    __tablename__ = "orders"

    order_id = Column(Integer, primary_key=True)
    customer = relationship("Customers", back_populates="orders")
