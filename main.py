from db.user_db import UserInDB, update_user, get_user
from db.hotel_db import Rooms, get_rooms, print_rooms
from models.user_models import UserIn, UserOut
from models.Room_model import RoomIn

from db.adicionales_db import Alimentacion, get_alimentacion, print_alimentacion
from models.adicionales_model import AlimentacionIn


import datetime
import uvicorn
from fastapi import FastAPI
from fastapi import HTTPException
from fastapi.middleware.cors import CORSMiddleware

api = FastAPI()

origins = [
    "http://localhost.tiangolo.com", "https://localhost.tiangolo.com",
    "http://localhost", "http://localhost:8080", "https://reserva-hoteles-g1m3-16.herokuapp.com"
]

api.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@api.get("/")
async def root():
    return {"Mensaje": "Bienvenido a la pagina de reserva de habitaciones !"}

@api.post("/user/auth/")
async def auth_user(user_in: UserIn):
    user_in_db = get_user(user_in.username)
    if user_in_db == "guest":
        return {"No Autenticado": "Ha ingresado como guest"}
        
    else:
        if user_in_db == None:
            raise HTTPException(status_code=404, detail="El usuario no existe")

        if user_in_db.password != user_in.password:
            return {"No Autenticado": "Ha ingresado la contraseña incorrecta"}
        return {"Autenticado": "Ha ingresado con el usuario " + user_in_db.username}

@api.get("/user/RewardPoints/{username}")
async def get_balance(username: str):
    user_in_db = get_user(username)
    if user_in_db == None:
        raise HTTPException(status_code=404, detail="El usuario no existe")
    user_out = UserOut(**user_in_db.dict())
    
    return user_out

@api.post("/search/")
async def searchRoomsAvailable(RoomIn: RoomIn):
    habitacionesDisponibles = get_rooms(RoomIn)

    if not habitacionesDisponibles:
        raise HTTPException(status_code=404, detail="No hay habitaciones disponibles para su seleccion")
    
    else:
        listado = print_rooms(habitacionesDisponibles)
    return listado

@api.get("/food/")
async def getBreakfastPrice():
    #alimentacion_in_db = get_alimentacion(tipo)

    #if alimentacion_in_db == None:
    #   raise HTTPException(status_code=404, detail="No existe esa comida")

    #return alimentacion_in_db
    return print_alimentacion()
