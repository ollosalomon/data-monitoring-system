from fastapi import FastAPI, UploadFile, File
from minio import Minio
from prometheus_client import Counter, generate_latest, CONTENT_TYPE_LATEST, start_http_server
import os
import csv
import random
import time
import shutil

app = FastAPI()

# Initialiser le client MinIO
minio_client = Minio(
    "minio:9000",
    access_key=os.getenv("MINIO_ROOT_USER"),
    secret_key=os.getenv("MINIO_ROOT_PASSWORD"),
    secure=False
)

# Créer un bucket MinIO s'il n'existe pas
bucket_name = "csv-bucket"
if not minio_client.bucket_exists(bucket_name):
    minio_client.make_bucket(bucket_name)

# Métrique Prometheus
METRIC_REQUESTS = Counter('requests_total', 'Nombre total de requêtes reçues')

# Démarrer le serveur Prometheus pour exposer les métriques sur le port 8001
start_http_server(8001)

# Route pour les métriques Prometheus
@app.get("/metrics")
def metrics():
    return generate_latest(), 200, {'Content-Type': CONTENT_TYPE_LATEST}

@app.get("/")
def read_root():
    METRIC_REQUESTS.inc()
    return {"message": "Hello, World!"}

@app.post("/upload/")
async def upload_csv(file: UploadFile = File(...)):
    METRIC_REQUESTS.inc()
    file_name = file.filename  # Nom du fichier envoyé

    # Sauvegarde temporaire du fichier
    with open(file_name, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    # Upload vers MinIO
    with open(file_name, "rb") as file_data:
        minio_client.put_object(
            bucket_name, 
            file_name, 
            file_data, 
            os.stat(file_name).st_size
        )
    
    os.remove(file_name)  # Supprime le fichier localement après l'upload
    return {"message": f"{file_name} uploaded and stored in MinIO successfully."}
