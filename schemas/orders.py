from pydantic import BaseModel


class OrderSchema(BaseModel):
    user_id: int
    rest_id: int
    total_amount: int
