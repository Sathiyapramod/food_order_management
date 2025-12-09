from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from db.database import Base


class Customers(Base):
    __tablename__ = "customers"

    id = Column(Integer, primary_key=True)
    cust_name = Column(String)
    contact_no = Column(String)
    email = Column(String)
    location = Column(String)
    orders = relationship("Orders", back_populates="Customers")
