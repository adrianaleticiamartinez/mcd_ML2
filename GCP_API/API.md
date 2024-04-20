# main.py (Código API)

Esta API implementada en Google Cloud Functions permite realizar predicciones sobre la aprobación de financiamiento de vivienda en la Ciudad de México utilizando un modelo de aprendizaje automático basado en XGBoost.

## Descripción del Proceso

El proceso de predicción consta de los siguientes pasos:

1. **Descarga del Modelo:** La función descarga el modelo entrenado desde Google Cloud Storage al inicio de la ejecución para su posterior uso.
2. **Carga del Modelo:** El modelo descargado se carga en memoria y se utiliza para realizar predicciones sobre los datos de entrada.
3. **Predicción:** Cuando se recibe una solicitud HTTP POST, se extraen los datos de entrada del cuerpo de la solicitud, se preprocesan y se realiza la predicción utilizando el modelo cargado.
4. **Respuesta:** La predicción resultante se devuelve como respuesta en formato JSON.

## Métodos

### Método POST `/predict`

Este método permite realizar una predicción sobre los datos de entrada proporcionados en el cuerpo de la solicitud.

#### Parámetros de Entrada

El cuerpo de la solicitud debe ser un objeto JSON con los siguientes campos:

- `cve_mun`: Clave municipal del solicitante (tipo: float).
- `intermediario_financiero`: Identificador del intermediario financiero (tipo: int).
- `sexo`: Género del solicitante (tipo: float).
- `edad_rango`: Rango de edad del solicitante (tipo: float).
- `ingresos_rango`: Rango de ingresos del solicitante (tipo: float).
- `vivienda_valor`: Valor de la vivienda (tipo: float).
- `acciones`: Acciones (tipo: int).

#### Respuesta

La respuesta de la API será un objeto JSON con un campo `prediction`, que indica la predicción realizada por el modelo. El valor de `prediction` será un entero que representa la clase predicha (0 para no aprobado, 1 para aprobado).

## Implementación

La API está implementada en Python utilizando Flask para manejar las solicitudes HTTP y la biblioteca joblib para cargar el modelo entrenado. Los datos de entrada se preprocesan antes de realizar la predicción utilizando pandas y scikit-learn.
