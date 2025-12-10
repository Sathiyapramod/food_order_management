from fastapi import APIRouter, Depends
from schemas.order_items import OrderItemSchema
from sqlalchemy.orm import Session
from dependencies import connect_to_db
from models.order_items import OrderItems
from models.foods import Foods

order_items_router = APIRouter(prefix="/order_items", tags=["Order Items"])


@order_items_router.get("/")
def get_all_order_items(dbs: Session = Depends(connect_to_db)):
    all_items = dbs.query(OrderItems, Foods).join(Foods).all()
    result = []
    for order_items, foods in all_items:
        temp = {
            "id": order_items.id,
            "quantity": order_items.quantity,
            "food_name": foods.food_name,
            "price": foods.price,
        }
        result.append(temp)
    return result


@order_items_router.post("/")
def create_an_order_item(
    new_dish: OrderItemSchema, dbs: Session = Depends(connect_to_db)
):
    entry = OrderItems(
        quantity=new_dish.quantity, order_id=new_dish.order_id, food_id=new_dish.food_id
    )

    # insert row
    dbs.add(entry)
    dbs.commit()
    dbs.refresh(entry)
    return {"message": "new dish added"}


@order_items_router.get("/{id}")
def get_order_items_by_id(id: int, dbs: Session = Depends(connect_to_db)):
    find_order_items = dbs.query(OrderItems).filter(OrderItems.id == id).first()
    if not find_order_items:
        return {"message": f"invalid order items id - {id}"}
    return find_order_items
