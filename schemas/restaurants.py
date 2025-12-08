from pydantic import BaseModel


class Restaurants_schema(BaseModel):
    rest_name: str
    contact_person: str
    location: str
    phone: str
