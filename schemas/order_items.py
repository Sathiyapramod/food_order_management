from pydantic import BaseModel


class OrderItemSchema(BaseModel):
    quantity: int
    order_id: int
    food_id: int
