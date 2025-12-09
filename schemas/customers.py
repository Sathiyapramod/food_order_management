from pydantic import BaseModel


class CustomerSchema(BaseModel):
    cust_name: str
    contact_no: str
    email: str
    location: str
