'''
import boto3
import joblib

# determinando o a aplicação AWS utilizada
s3 = boto3.client('s3')
#Passando os dados para download do modelo
s3.download_file('your-bucket-name', 'path-to-model', '/tmp/model.pkl')
#caregando o modelo
model = joblib.load('/tmp/model.pkl')
'''

import boto3
import joblib
import os
import xgboost as xgb
from src.config.config import BUCKET, SUBPASTA_MODELO, MODEL_FILE_NAME

def load_model():
    modelo_carregado = xgb.Booster()
    modelo_carregado.load_model('src/projeto/projeto/modelos/hotel/xgboost/output/xgboost-2024-09-13-16-09-04-431/output/model/xgboost-model')


'''
def load_model():
    # Configurar o cliente do S3
    s3 = boto3.client(
        's3',
        aws_access_key_id=os.getenv('AWS_ACCESS_KEY_ID'),
        aws_secret_access_key=os.getenv('AWS_SECRET_ACCESS_KEY'),
        region_name=os.getenv('AWS_REGION')
    )
    
    # Definir o caminho completo do modelo no S3
    model_s3_path = f"{SUBPASTA_MODELO}/{MODEL_FILE_NAME}"
    
    # Baixar o modelo do bucket do S3
    with open(MODEL_FILE_NAME, 'wb') as f:
        s3.download_file(BUCKET, model_s3_path, f)
    
    # Carregar o modelo usando joblib
    model = joblib.load(MODEL_FILE_NAME)
    return model
'''