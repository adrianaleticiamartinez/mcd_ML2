# mcd_ML2
Proyecto final de la maestría en ciencia de datos de la universidad Panamericana para la asignatura de aprendizaje máquina II

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

Code/

|- Proyecto Final ML2 AM.ipynb

|- API.ipynb

|- Prueba modelo.ipynb

|- Prueba API.ipynb



## Data

La carpeta `Data` contiene tanto los conjuntos de datos utilizados (`Datasets`) como los diccionarios de datos correspondientes (`Diccionarios`) que explican cada columna presente en los datasets.

### Diccionarios

- `diccionario_cnbv.csv`: Describe las columnas presentes en el dataset proporcionado por la Comisión Nacional Bancaria y de Valores.
- `diccionario_financiamiento.csv`: Contiene la descripción de las columnas relacionadas con el financiamiento de la vivienda.

### Datasets

- `financiamientos_full_CDMX.csv`: Conjunto de datos que incluye información detallada sobre los financiamientos en la Ciudad de México.
- `cnbv_full_CDMX.csv`: Datos de créditos otorgados relacionados con la vivienda recopilados por la CNBV.

## Code

La carpeta `Code` incluye todos los Jupyter Notebooks desarrollados durante el proyecto.

### Proyecto Final ML2 AM.ipynb

Descripción del proceso seguido en el notebook principal:

1. **Carga de Datos**: Importación y primera inspección de los datos.
2. **Preprocesamiento**: Limpieza y preparación de los datos para el modelado.
3. **Modelado con XGBoost**: Entrenamiento del modelo predictivo utilizando XGBoost.
4. **Evaluación del Modelo**: Evaluación del modelo con métricas estándar de clasificación.
5. **Exportación del Modelo**: Procedimiento para exportar el modelo para su despliegue.

### API.ipynb

Notebook de referencia con el código preliminar que se utilizó antes de implementar la API en el entorno de Google Cloud.

### Prueba modelo.ipynb

Validación del modelo y pruebas de su funcionamiento antes de la importación al Google Cloud Storage.

### Prueba API.ipynb

Demostración de cómo consumir la API desplegada en Google Cloud Platform, con ejemplos de llamadas y respuestas.

## Uso de la API

[Descripción detallada de cómo usar la API, incluyendo endpoints, parámetros esperados, formatos de respuesta, etc.]

## Contribuciones y Soporte

[Información sobre cómo contribuir al proyecto, reportar problemas o buscar soporte.]


## Autores

- Adriana Leticia Martinez Estrada



