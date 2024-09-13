import boto3
import joblib

# determinando o a aplicação AWS utilizada
s3 = boto3.client('s3')
#Passando os dados para download do modelo
s3.download_file('your-bucket-name', 'path-to-model', '/tmp/model.pkl')
#caregando o modelo
model = joblib.load('/tmp/model.pkl')

