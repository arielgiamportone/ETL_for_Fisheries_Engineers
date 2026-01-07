# Changelog

Todos los cambios notables en este proyecto serán documentados en este archivo.

El formato está basado en [Keep a Changelog](https://keepachangelog.com/es-ES/1.0.0/),
y este proyecto adhiere a [Versionado Semántico](https://semver.org/lang/es/).

## [1.0.0] - 2026-01-07

### ✨ Añadido
- Estructura inicial del proyecto ETL para datos pesqueros
- 5 Notebooks Jupyter interactivos y didácticos:
  - 00: Configuración del Entorno
  - 01: Extracción de Datos
  - 02: Transformación de Datos
  - 03: Carga de Datos
  - 04: Visualización Exploratoria
- Módulo `data_utils.py` con funciones de extracción y generación de datos
- Módulo `processing.py` con funciones de transformación
- Generación automática de datos de ejemplo:
  - Desembarques pesqueros (2,880 registros)
  - Datos oceanográficos (480 registros)
  - Información de flota (200 embarcaciones)
- Script de prueba `test_project.py`
- Documentación completa en README.md
- Guía de contribución (CONTRIBUTING.md)

### 🔧 Configuración
- Archivo `requirements.txt` con todas las dependencias
- Archivo `.gitignore` configurado para Python y Jupyter
- Estructura de carpetas `data/raw/` y `data/processed/`
- Entorno virtual Python 3.13

### 📚 Dependencias
- pandas >= 2.0.0
- numpy >= 1.24.0
- matplotlib >= 3.7.0
- seaborn >= 0.12.0
- plotly >= 5.18.0
- requests >= 2.31.0
- sqlalchemy >= 2.0.0
- openpyxl >= 3.1.0
- networkx >= 3.1

### 🎯 Características
- Metáforas pesqueras para facilitar el aprendizaje
- Datos realistas con estacionalidad y tendencias
- Código modular y reutilizable
- Soporte para exportación a CSV, Excel y SQLite
- Visualizaciones con matplotlib, seaborn y plotly

---

## [Próximas Versiones]

### 🔮 En Desarrollo (v1.1.0)
- [ ] Integración con APIs reales de datos pesqueros
- [ ] Dashboard interactivo con Plotly Dash
- [ ] Análisis de series temporales
- [ ] Modelos de predicción básicos

### 💭 Planificado (v1.2.0)
- [ ] Análisis espacial con GeoPandas
- [ ] Integración con PostGIS
- [ ] Notebooks de Machine Learning aplicado
- [ ] Conexión con sensores IoT

### 🌟 Futuro (v2.0.0)
- [ ] Pipeline automatizado con Apache Airflow
- [ ] Procesamiento Big Data con PySpark
- [ ] Deep Learning para clasificación de especies
- [ ] API REST para servir modelos

---

## Formato de Cambios

### Tipos de Cambios
- `✨ Añadido` - para nuevas funcionalidades
- `🔧 Cambiado` - para cambios en funcionalidad existente
- `⚠️ Deprecado` - para funcionalidades que serán removidas
- `🗑️ Eliminado` - para funcionalidades eliminadas
- `🐛 Corregido` - para corrección de bugs
- `🔒 Seguridad` - en caso de vulnerabilidades

---

**Última actualización**: 7 de Enero, 2026
