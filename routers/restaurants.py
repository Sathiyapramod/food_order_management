from fastapi import APIRouter, Depends, status
from schemas.restaurants import Restaurants_schema
from models.restaurants import Restaurants
from sqlalchemy.orm import Session
from dependencies import connect_to_db

restaurant_router = APIRouter(prefix="/restaurants", tags=["Restaurants"])


@restaurant_router.get("/", status_code=status.HTTP_200_OK)
def get_all_restaurants(dbs: Session = Depends(connect_to_db)):
    restaurants = dbs.query(Restaurants).all()
    return restaurants


@restaurant_router.get("/{id}", status_code=status.HTTP_200_OK)
def get_restaurant_by_id(id: int, dbs: Session = Depends(connect_to_db)):
    find_rest = dbs.query(Restaurants).filter(Restaurants.id == id).first()
    if not find_rest:
        return {"message": "invalid id"}
    return find_rest


@restaurant_router.post("/", status_code=status.HTTP_200_OK)
def create_restaurant(
    new_rest: Restaurants_schema, dbs: Session = Depends(connect_to_db)
):
    valid_entry = Restaurants(
        rest_name=new_rest.rest_name,
        location=new_rest.location,
        contact_person=new_rest.contact_person,
        phone=new_rest.phone,
    )
    # adding ops
    dbs.add(valid_entry)
    # committing ops
    dbs.commit()
    # refresh table
    dbs.refresh(valid_entry)
    return valid_entry


@restaurant_router.put("/{id}", status_code=status.HTTP_200_OK)
def update_restaurant_by_id(
    latest_rest: Restaurants_schema, id: int, dbs: Session = Depends(connect_to_db)
):
    find_rest = dbs.query(Restaurants).filter(Restaurants.id == id).first()
    if not find_rest:
        return {"message": "invalid id"}
    else:
        # updating ops
        find_rest.rest_name = latest_rest.rest_name
        find_rest.location = latest_rest.location
        find_rest.contact_person = latest_rest.contact_person
        find_rest.phone = latest_rest.phone

        # committing ops
        dbs.commit()
        # refresh table
        dbs.refresh(find_rest)
        return {"message": "updated restaurant successfully"}


@restaurant_router.delete("/{id}", status_code=status.HTTP_200_OK)
def delete_restaurant_by_id(id: int, dbs: Session = Depends(connect_to_db)):
    find_rest = dbs.query(Restaurants).filter(Restaurants.id == id).first()
    if not find_rest:
        return {"message": "invalid id"}
    dbs.delete(find_rest)
    return {"message": "deleted restaurant successfully"}
