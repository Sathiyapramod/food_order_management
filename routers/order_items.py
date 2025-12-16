from fastapi import APIRouter, Depends, status
from schemas.order_items import OrderItemSchema
from sqlalchemy import select, text
from sqlalchemy.orm import Session
from dependencies import connect_to_db
from models.order_items import OrderItems
from models.foods import Foods

order_items_router = APIRouter(prefix="/order_items", tags=["Order Items"])


@order_items_router.get("/{order_id}", status_code=status.HTTP_200_OK)
def get_all_order_items(order_id: int, dbs: Session = Depends(connect_to_db)):
    raw_query = f"""SELECT 
    order_items.id, 
    foods.food_name, 
    foods.price, 
    order_items.quantity
        FROM order_items
        JOIN foods
        ON foods.id = order_items.food_id
        WHERE order_items.order_id = {order_id}
        ;"""

    all_items = dbs.execute(text(raw_query))
    result = []

    for id, food_name, price, qty in all_items:
        temp = {"id": id, "food_name": food_name, "price": price, "qty": qty}
        result.append(temp)
    return result


@order_items_router.post("/", status_code=status.HTTP_200_OK)
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


@order_items_router.get("/{id}", status_code=status.HTTP_200_OK)
def get_order_items_by_id(id: int, dbs: Session = Depends(connect_to_db)):
    find_order_items = dbs.query(OrderItems).filter(OrderItems.id == id).first()
    if not find_order_items:
        return {"message": f"invalid order items id - {id}"}
    return find_order_items
