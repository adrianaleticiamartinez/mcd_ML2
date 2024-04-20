from flask import jsonify, abort, request
from google.cloud import storage
from sklearn.preprocessing import LabelEncoder
import joblib
import os
import pandas as pd

# Función para descargar el modelo desde Google Cloud Storage
def download_model():
    print("Descargando el modelo desde Cloud Storage...")
    # Crea una instancia del cliente de Cloud Storage
    storage_client = storage.Client()
    
    # Nombre del bucket y del archivo en Cloud Storage
    BUCKET_NAME = 'modelo_ml2'
    MODEL_FILE = 'xgboost_model.pkl'
    
    # Ruta local donde se almacenará temporalmente el archivo
    LOCAL_MODEL_FILE = '/tmp/model.pkl'
    
    # Descarga el archivo del modelo desde Cloud Storage
    bucket = storage_client.bucket(BUCKET_NAME)
    blob = bucket.blob(MODEL_FILE)
    blob.download_to_filename(LOCAL_MODEL_FILE)

# Función para cargar el modelo
def load_model():
    # Verifica si el archivo del modelo ya está presente localmente
    if not os.path.exists('/tmp/model.pkl'):
        download_model()
    # Carga el modelo desde el archivo
    return joblib.load('/tmp/model.pkl')

# Cargar el modelo una vez al inicio
model = load_model()

# La función principal que maneja la solicitud HTTP
def predict(request):
    """Función que responde a cualquier solicitud HTTP.
    Args:
        request (flask.Request): Objeto de solicitud HTTP.
    Returns:
        Texto de respuesta o cualquier conjunto de valores que puedan convertirse en un
        objeto de respuesta utilizando `make_response`.
    """
    if not request.json:
        abort(400, "El cuerpo de la solicitud debe ser un JSON.")

    # Obtener los datos de entrada de la solicitud JSON
    request_json = request.get_json()

    # Extraer los datos necesarios para la predicción
    features = ['cve_mun', 'intermediario_financiero', 'sexo', 'edad_rango', 'ingresos_rango', 'vivienda_valor', 'acciones']
    input_data = pd.DataFrame([request_json])

    # Codificar variables categóricas
    input_data_encoded = input_data.copy()  # Hacemos una copia para no modificar los datos originales
    categorical_vars = input_data_encoded.select_dtypes(include=['object']).columns
    for col in categorical_vars:
        input_data_encoded[col] = input_data_encoded[col].astype('category').cat.codes

    # Realizar la predicción utilizando el modelo cargado
    prediction = model.predict(input_data_encoded)

    # Devolver los resultados de la predicción como respuesta
    prediction_result = {'prediction': int(prediction[0])}  # Convertir la predicción a un entero
    print(f"La predicción para el caso puntual es: {prediction_result}")

    return jsonify(prediction_result)
