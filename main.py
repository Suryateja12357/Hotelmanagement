from fastapi import FastAPI
import models
import models.User_model
import models.Room_model
import models.Booking_model
from router import User_router,Room_router,Booking_router
from utilities.database import engine
app=FastAPI()
models.User_model.Base.metadata.create_all(bind=engine)
models.Room_model.Base.metadata.create_all(bind=engine)
models.Booking_model.Base.metadata.create_all(bind=engine)
app.include_router(User_router.router)
app.include_router(Room_router.router)
app.include_router(Booking_router.router)