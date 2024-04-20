# mcd_ML2
Proyecto final de la maestría en ciencia de datos de la universidad Panamericana para la asignatura de aprendizaje máquina II
Alumno: Adriana Leticia Martinez Estrada

# Documentación del Proyecto de Financiamiento de Vivienda

Este repositorio contiene los datasets, códigos y documentación del proyecto para la predicción de financiamiento de viviendas en la Ciudad de México, el cual ha sido desplegado como una API pública en Google Cloud Platform.

## Estructura del Repositorio
Data/

|- Diccionarios/

| |- diccionario_cnbv.csv

| |- diccionario_financiamiento.csv

|- Datasets/

| |- financiamientos_full_CDMX.csv

| |- cnbv_full_CDMX.csv



|Proyecto Final ML2 AM.ipynb

|API.ipynb

|Prueba modelo.ipynb

|Prueba API.ipynb

Output/

|- xgboost_model.pkl



## Data

La carpeta `Data` contiene tanto los conjuntos de datos utilizados (`Datasets`) como los diccionarios de datos correspondientes (`Diccionarios`) que explican cada columna presente en los datasets.

### Diccionarios

- `diccionario_cnbv.csv`: Describe las columnas presentes en el dataset proporcionado por la Comisión Nacional Bancaria y de Valores sobre financiamientos privados.
- `diccionario_financiamiento.csv`: Contiene la descripción de las columnas relacionadas con el financiamiento público de la vivienda.

### Datasets

- `financiamientos_full_CDMX.csv`: Conjunto de datos que incluye información detallada sobre los financiamientos públicos en la Ciudad de México.
- `cnbv_full_CDMX.csv`: Datos de créditos otorgados relacionados por instituciones privadas para la vivienda, recopilados por la CNBV.

Se incluyen todos los Jupyter Notebooks desarrollados durante el proyecto.

## Proyecto Final ML2 AM.ipynb

Este Jupyter Notebook desarrolla un clasificador utilizando el algoritmo XGBoost para predecir la aprobación de financiamientos para vivienda en la Ciudad de México. El modelo se basa en datos socioeconómicos, demográficos y características de la vivienda de los solicitantes.

### Descripción del Proceso

El proceso se divide en las siguientes etapas:

Carga de Datos y Análisis Exploratorio (EDA): Se cargan los datos desde archivos CSV y se realiza un análisis exploratorio para comprender su estructura y contenido.
Preprocesamiento: Se limpian y transforman los datos para prepararlos para el modelado.
Modelado con XGBoost: Se entrena el modelo XGBoost con los datos preparados.
Evaluación del Modelo: Se evalúa el rendimiento del modelo utilizando métricas de clasificación estándar.
Exportación del Modelo: Finalmente, se exporta el modelo entrenado para su implementación futura.
Estructura del Código

Importación de Librerías
Se importan las librerías necesarias para el análisis y modelado de datos.

Carga de Datos / Análisis Exploratorio de Datos (EDA)
En esta sección, se realiza un análisis exploratorio de datos (EDA) para comprender la estructura y características de los conjuntos de datos. Se utiliza Pandas para cargar los datos desde archivos CSV y se realizan diversas visualizaciones y estadísticas descriptivas para entender la distribución y relaciones entre las variables.

Preprocesamiento
Se realizan diversas operaciones de preprocesamiento en los datos, incluyendo la limpieza de valores nulos, la codificación de variables categóricas y la normalización de variables numéricas.

XGBoost para la Predicción de Financiamiento de Vivienda
Se entrena un modelo de clasificación utilizando el algoritmo XGBoost. Se dividen los datos en conjuntos de entrenamiento y prueba, se entrena el modelo y se evalúa su rendimiento utilizando métricas de clasificación.

Exportación del Modelo
Finalmente, se exporta el modelo entrenado como un archivo pickle para su uso futuro, así como su posterioir productivización en GCP.

## API.ipynb

Notebook de referencia con el código preliminar que se utilizó antes de implementar la API en el entorno de Google Cloud, en el se implementa una API utilizando Flask para predecir la aprobación de financiamientos para vivienda en la Ciudad de México. El modelo utilizado es un modelo de clasificación entrenado previamente y cargado al inicio de la aplicación.

### Descripción del Proceso

El proceso se describe en las siguientes etapas:

1. **Carga del Modelo:** Al inicio de la aplicación, se carga el modelo de clasificación previamente entrenado.
2. **Recepción de Solicitud POST:** La API espera recibir una solicitud POST con datos de entrada para la predicción.
3. **Predicción:** Utilizando los datos recibidos en la solicitud, se realiza una predicción utilizando el modelo cargado.
4. **Respuesta:** La predicción se devuelve como respuesta en formato JSON.

### Estructura del Código

### Importación de Librerías

Se importan las librerías necesarias para la implementación de la API, incluyendo Flask y joblib para la carga del modelo.

#####Carga del Modelo

El modelo de clasificación previamente entrenado se carga al inicio de la aplicación utilizando joblib.

##### Recepción de Solicitud POST

La API espera recibir una solicitud POST en la ruta '/predict'. Los datos de entrada para la predicción se obtienen del cuerpo de la solicitud en formato JSON.

##### Predicción

Utilizando los datos recibidos en la solicitud POST, se realiza una predicción utilizando el modelo cargado.

##### Respuesta

La predicción se devuelve como respuesta en formato JSON, incluyendo la clase predicha.

#### Uso de la API

La API puede ser utilizada enviando una solicitud POST a la ruta '/predict' con los datos de entrada en formato JSON. La respuesta de la API incluirá la clase predicha para los datos de entrada proporcionados.


## Prueba modelo.ipynb

Validación del modelo y pruebas de su funcionamiento antes de la importación al Google Cloud Storage.
### Descripción del Proceso

El proceso de prueba se describe en las siguientes etapas:

1. **Carga del Modelo:** Se carga el modelo de predicción de financiamiento de vivienda previamente entrenado.
2. **Generación de Datos de Prueba:** Se genera un conjunto de datos de prueba simulando un caso puntual de solicitud de financiamiento de vivienda.
3. **Codificación de Variables Categóricas:** Las variables categóricas en los datos de prueba se codifican utilizando LabelEncoder.
4. **Predicción:** Se realiza una predicción utilizando el modelo cargado y los datos de prueba generados.
5. **Resultado de la Predicción:** Se muestra la clase predicha y, si el modelo predice probabilidades, también se muestran las probabilidades de pertenecer a cada clase.

### Código

#### Carga del Modelo

Se carga el modelo de predicción de financiamiento de vivienda previamente entrenado desde el archivo 'xgboost_model.pkl'.

#### Generación de Datos de Prueba

Se genera un conjunto de datos de prueba en forma de un DataFrame de Pandas, simulando un caso puntual de solicitud de financiamiento de vivienda.

#### Codificación de Variables Categóricas

Las variables categóricas en los datos de prueba se codifican utilizando LabelEncoder para que puedan ser utilizadas por el modelo de predicción.

#### Predicción

Se realiza una predicción utilizando el modelo cargado y los datos de prueba generados.

#### Resultado de la Predicción

Se muestra la clase predicha para el caso puntual y, si el modelo predice probabilidades, también se muestran las probabilidades de pertenecer a cada clase.

## Prueba API.ipynb

Demostración de cómo consumir la API desplegada en Google Cloud Platform, con ejemplos de llamadas y respuestas.
### Descripción del Proceso

El proceso de prueba se describe en las siguientes etapas:

1. **Definición de la URL del Endpoint:** Se define la URL del endpoint de la Cloud Function donde está desplegada la API.
2. **Datos de Entrada:** Se definen los datos de entrada para la solicitud, que representan un caso puntual de solicitud de financiamiento de vivienda.
3. **Realización de la Solicitud:** Se realiza una solicitud POST al API utilizando los datos de entrada y los encabezados adecuados.
4. **Verificación de la Respuesta:** Se verifica si la solicitud fue exitosa y se muestra el resultado de la predicción en caso de éxito. En caso de falla, se muestra el mensaje de error.

### Código

### Definición de la URL del Endpoint

Se define la URL del endpoint de la Cloud Function donde está desplegada la API.

#### Datos de Entrada

Se definen los datos de entrada para la solicitud en forma de un diccionario de Python.

#### Realización de la Solicitud

Se realiza una solicitud POST al API utilizando la función `requests.post()` de la biblioteca `requests`, proporcionando los datos de entrada y los encabezados adecuados.

#### Verificación de la Respuesta

Se verifica si la solicitud fue exitosa comprobando el código de estado de la respuesta. Si la solicitud fue exitosa, se muestra el resultado de la predicción. En caso de falla, se muestra el mensaje de error.

## Uso de la API

[Descripción detallada de cómo usar la API, incluyendo endpoints, parámetros esperados, formatos de respuesta, etc.]

## Contribuciones y Soporte

[Información sobre cómo contribuir al proyecto, reportar problemas o buscar soporte.]


## Autores

- Adriana Leticia Martinez Estrada



