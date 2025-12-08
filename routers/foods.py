from fastapi import APIRouter, Depends

# schema
from schemas.foods import Foods_schema
from dependencies import connect_to_db
from sqlalchemy.orm import Session

# database models
from models.foods import Foods


food_router = APIRouter(prefix="/foods", tags=["Foods"])


# GET
@food_router.get("/")
def get_all_foods(dbs: Session = Depends(connect_to_db)):
    all_foods = dbs.query(Foods).all()
    return all_foods


# GET {id}
@food_router.get("/{id}")
def get_food_by_id(id: int, dbs: Session = Depends(connect_to_db)):
    particular_food = dbs.query(Foods).filter(Foods.id == id).first()
    if not particular_food:
        return {"message": "Invalid Id"}
    return particular_food


# POST
@food_router.post("/")
def create_food(new_food: Foods_schema, dbs: Session = Depends(connect_to_db)):

    some_food_name = new_food.food_name
    some_price = new_food.price
    some_qty = new_food.qty
    something_avl = new_food.availability
    # food new model
    new_entry = Foods(
        food_name=some_food_name,
        price=some_price,
        qty=some_qty,
        availability=something_avl,
    )

    # adding the row
    dbs.add(new_entry)
    # committing the row
    dbs.commit()
    # refresh the table
    dbs.refresh(new_entry)
    return new_entry


# PUT
@food_router.put("/{id}")
def update_food_by_id(
    latest_food: Foods_schema, id: int, dbs: Session = Depends(connect_to_db)
):
    some_food_name = latest_food.food_name
    some_price = latest_food.price
    some_qty = latest_food.qty
    something_avl = latest_food.availability

    # update action
    particular_food = dbs.query(Foods).filter(Foods.id == id).first()
    if not particular_food:
        return {"message": "you have entered invalid id"}
    particular_food.food_name = some_food_name
    particular_food.price = some_price
    particular_food.qty = some_qty
    particular_food.availability = availability
    # r
    return {"message": "updated successfully"}


# DELETE
@food_router.delete("/{id}")
def delete_food_by_id(id: int):
    return {"message": "deleted successfully"}
