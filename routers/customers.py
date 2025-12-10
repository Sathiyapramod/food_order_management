from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from dependencies import connect_to_db
from models.customers import Customers
from schemas.customers import CustomerSchema

customers_router = APIRouter(prefix="/users", tags=["Users"])


# GET
@customers_router.get("/")
def get_all_customers(dbs: Session = Depends(connect_to_db)):
    orders_list = dbs.query(Customers).all()
    return orders_list


# POST
@customers_router.post("/")
def create_customer(new_user: CustomerSchema, dbs: Session = Depends(connect_to_db)):
    new_entry = Customers(
        cust_name=new_user.cust_name,
        contact_no=new_user.contact_no,
        email=new_user.email,
        location=new_user.location,
    )
    # create a new user
    dbs.add(new_entry)
    # committing
    dbs.commit()
    # refresh the table
    dbs.refresh(new_entry)
    return {"message": "new user created"}


# !! ToDo


# GET by ID
@customers_router.get("/{id}")
def get_customer_by_id(id: int, dbs: Session = Depends(connect_to_db)):
    find_customer = dbs.query(Customers).filter(Customers.id == id).first()
    if not find_customer:
        return {"message": f"invalid customer id - {id}"}
    return find_customer


# PUT
# DELETE
