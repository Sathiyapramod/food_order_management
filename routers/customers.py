from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from dependencies import connect_to_db
from models.customers import Customers

customers_router = APIRouter(prefix="/users", tags=["Users"])


# GET
@customers_router.get("/")
def get_all_customers(dbs: Session = Depends(connect_to_db)):
    orders_list = dbs.query(Users).all()
    return orders_list


# !! ToDo

# GET by ID
# POST
# PUT
# DELETE
