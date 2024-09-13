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
    

""""
@app.get("/")
async def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
async def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}"""