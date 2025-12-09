from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from dependencies import connect_to_db
from models.orders import Orders

orders_router = APIRouter(prefix="/orders", tags=["Orders"])

# GET 
@orders_router.get("/")
def get_all_orders(dbs: Session = Depends(connect_to_db)):
    orders_list = dbs.query(Orders).all()
    return orders_list

# !! ToDo

# GET by ID
# POST 
# PUT 
# DELETE