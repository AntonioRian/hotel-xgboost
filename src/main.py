from fastapi import FastAPI, HTTPException
from src.conexão_modelo.modelo import load_model
from pydantic import BaseModel

app = FastAPI()

# Carregar o modelo ao iniciar o app
model = load_model()

# Definir o formato de entrada
class InferenceRequest(BaseModel):
    no_of_adults: int
    no_of_children: int
    type_of_meal_plan: str
    required_car_parking_space: int
    room_type_reserved: str
    lead_time: int
    arrival_month: int
    arrival_date: int
    market_segment_type: str
    repeated_guest: int

@app.post("/api/v1/inference")
async def make_inference(data: InferenceRequest):
    try:
        # Organizar os dados de entrada para o modelo
        input_data = [[
            data.no_of_adults,
            data.no_of_children,
            data.type_of_meal_plan,
            data.required_car_parking_space,
            data.room_type_reserved,
            data.lead_time,
            data.arrival_month,
            data.arrival_date,
            data.market_segment_type,
            data.repeated_guest
        ]]
        # Realizar a inferência
        result = model.predict(input_data)
        return {"result": result[0]}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error making inference: {str(e)}")

'''
from typing import Union

from fastapi import FastAPI

from modelo import model

app = FastAPI()

# rascunho do método post para a APi
@app.post("/api/v1/inference")
async def resutado_previsao(request_data):
    #dados para a previsão  do modelo
    resultado = model.predict([input_data])[0]
    #retona o resultado previsto
    return { "result": resultado }
    

@app.get("/")
async def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
async def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}"""
'''