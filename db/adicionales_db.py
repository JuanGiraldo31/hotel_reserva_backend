from typing import Dict
from pydantic import BaseModel

class Alimentacion(BaseModel):
    Tipo: str
    PriceCOP: int
    isAvailable: bool

database_alimentacion = Dict[str, Alimentacion]
database_alimentacion = {"Desayuno1": Alimentacion(**{"Tipo":"Desayuno Americano",
                        "PriceCOP": 40000,
                        "isAvailable": True}),

                        "Desayuno2": Alimentacion(**{"Tipo":"Desayuno Típico Colombiano",
                        "PriceCOP": 50000,
                        "isAvailable": False}),

                        "Almuerzo1": Alimentacion(**{"Tipo":"Almuerzo Tipo Buffet",
                        "PriceCOP": 60000,
                        "isAvailable": True}),

                        "Almuerzo2": Alimentacion(**{"Tipo":"Almuerzo Tipo Normal",
                        "PriceCOP": 40000,
                        "isAvailable": False}),

                        "Cena1": Alimentacion(**{"Tipo":"Cena Tipo Coctel",
                        "PriceCOP": 80000,
                        "isAvailable": False}),

                        "Cena2": Alimentacion(**{"Tipo":"Cena Tipo Coctel2",
                        "PriceCOP": 65000,
                        "isAvailable": True}),
                    }

def get_alimentacion(comida: str):
    lista = []
    cont = 1

    for comidas in database_alimentacion:
        try:
            lista.append(database_alimentacion[comida + str(cont)])
            cont += 1
        except:
            pass

    return lista

def print_alimentacion():
    lista = []
    for Alimentacion in database_alimentacion:
        lista.append(database_alimentacion[Alimentacion])
    return lista
