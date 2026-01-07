# Bitácora del Explorador de Datos Pesqueros: Un Viaje ETL
 Didactic guide to introduce Fisheries Engineers to ETL data process

## Objetivos
 Embárcate en una travesía por el océano de los datos pesqueros. Esta bitácora te guiará paso a paso, desde la recolección de datos crudos (como redes llenas de peces diversos) hasta la obtención de información pulida y lista para entender mejor nuestras pesquerías y tomar decisiones informadas.

## Contenido
- Extracción (E): Zarpamos hacia distintos caladeros digitales (APIs, archivos CSV) para lanzar nuestras redes y capturar los datos brutos sobre desembarques, el estado del océano y las características de nuestra flota.

- Transformación (T): De vuelta en el muelle (nuestro entorno de análisis), es hora de clasificar la captura. Separaremos las especies (estandarizar datos), mediremos los ejemplares (convertir unidades), quitaremos impurezas (limpiar errores y nulos) y combinaremos información de diferentes redes (unir tablas) para obtener una visión completa.

- Carga (L): Una vez procesada, nuestra valiosa información está lista para ser almacenada y presentada. La guardaremos en formatos eficientes (CSV, Parquet) y en una base de datos organizada (SQL), como si preparáramos el pescado para el mercado o el laboratorio.





.
├── .gitignore             # Archivos a ignorar por Git (logs, datos sensibles, etc.)
├── README.md              # La portada de nuestra bitácora: introducción, objetivos, cómo usarlo.
├── requirements.txt       # Lista de bibliotecas Python necesarias (pandas, numpy, etc.)
├── data/                  # Carpeta para los datos
│   ├── raw/               # Datos originales (como los descargados o generados)
│   │   ├── desembarques_pesqueros.csv
│   │   ├── datos_oceanograficos.csv
│   │   └── flota_pesquera.csv
│   └── processed/         # Datos limpios y transformados, listos para el análisis
│       ├── desembarques_transformados.csv
│       ├── datos_enriquecidos.csv
│       └── pesquerias.db  # Base de datos SQLite generada
├── notebooks/             # Los capítulos de nuestra bitácora (Cuadernos Jupyter)
│   ├── 00_Configuracion_Entorno.ipynb
│   ├── 01_Extraccion_Tesoros_Datos.ipynb  # Antes: Extracción
│   ├── 02_Transformacion_Pulido_Gemas.ipynb # Antes: Transformación
│   ├── 03_Carga_Exhibicion_Hallazgos.ipynb # Antes: Carga y Análisis Preliminar
│   └── (Opcional) 04_Visualizacion_Exploratoria.ipynb
└── src/                   # Código reutilizable (nuestras herramientas de exploración)
    ├── __init__.py
    ├── data_utils.py      # Funciones para obtener y generar datos
    └── processing.py      # Funciones para limpiar, transformar y enriquecer datos
