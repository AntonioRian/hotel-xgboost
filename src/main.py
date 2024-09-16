from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import numpy as np
import xgboost as xgb
import boto3
import os
import tarfile
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv(), override=True)

bucket = "projeto-hotel"
model_path = "modelos/hotel/xgboost/output/xgboost-2024-09-16-01-43-41-445/output/model.tar.gz"

def load_model():
    # Baixar e extrair o modelo do S3
    session = boto3.Session(
        aws_access_key_id=os.getenv('AWS_ACCESS_KEY_ID'), 
        aws_secret_access_key=os.getenv('AWS_SECRET_ACCESS_KEY'),
        region_name=os.getenv('AWS_REGION'),
        aws_session_token=os.getenv('AWS_SESSION_TOKEN')
    )
    s3 = session.client('s3')
    s3.download_file(bucket, model_path, './src/model.tar.gz')

    # Extrair o arquivo .tar.gz
    with tarfile.open('./src/model.tar.gz', 'r:gz') as tar:
        tar.extractall(path='./src')
    
    # Verifique e carregue o modelo extraído
    model_file = './src/xgboost-model'  # Certifique-se de que o arquivo existe aqui
    model_xgb = xgb.Booster()
    model_xgb.load_model(model_file)
    
    return model_xgb

app = FastAPI()

# Carregar o modelo ao iniciar o app
model = load_model()

# Definir o formato de entrada
class InferenceRequest(BaseModel):
    no_of_adults: int
    no_of_children: int
    no_of_weekend_nights: int
    no_of_weekd_nights: int
    type_of_meal_plan: str
    required_car_parking_space: int
    room_type_reserved: str
    lead_time: int
    arrival_year: int
    arrival_month: int
    arrival_date: int
    market_segment_type: str
    repeated_guest: int
    no_of_previous_cancellations: int
    no_of_previous_bookings_not_canceled: int
    no_of_special_requests: int

class InferenceResponse(BaseModel):
    result: float

@app.post("/api/v1/inference", response_model=InferenceResponse)
async def make_inference(data: InferenceRequest):
    try:
        # Organizar os dados de entrada na ordem correta esperada pelo modelo
        input_data = np.array([[
            data.no_of_adults,
            data.no_of_children,
            data.no_of_weekend_nights,
            data.no_of_weekd_nights,
            data.type_of_meal_plan,
            data.required_car_parking_space,
            data.room_type_reserved,
            data.lead_time,
            data.arrival_year,
            data.arrival_month,
            data.arrival_date,
            data.market_segment_type,
            data.repeated_guest,
            data.no_of_previous_cancellations,
            data.no_of_previous_bookings_not_canceled,
            data.no_of_special_requests
        ]])

        # Criar o DMatrix para o XGBoost
        dmatrix = xgb.DMatrix(input_data)

        # Fazer a previsão
        results = model.predict(dmatrix)

        return InferenceResponse(result=float(results[0]))
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Erro na inferência: {str(e)}")
