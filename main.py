from fastapi import FastAPI
from db.database import Base, engine
# routers -> foods router import
# step-1
from routers.foods import food_router
from routers.restaurants import restaurant_router

Base.metadata.create_all(bind=engine)

app = FastAPI()
# step -2
# decorator function
@app.get("/")
def read_root():
    return {"Hello": "World"}

app.include_router(food_router)
app.include_router(restaurant_router)