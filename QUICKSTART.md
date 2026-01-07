# 🚀 Guía de Inicio Rápido

¡Bienvenido! Esta guía te ayudará a poner en marcha el proyecto en menos de 10 minutos.

## ⚡ Instalación Express

### Opción 1: Usando Git (Recomendado)

```bash
# 1. Clonar el repositorio
git clone https://github.com/tu-usuario/ETL_for_Fisheries_Engineers.git
cd ETL_for_Fisheries_Engineers

# 2. Crear y activar entorno virtual
python -m venv env

# Windows
env\Scripts\activate

# Linux/Mac
source env/bin/activate

# 3. Instalar dependencias
pip install -r requirements.txt

# 4. Generar datos de ejemplo
python test_project.py

# 5. Iniciar Jupyter
jupyter lab
```

### Opción 2: Descarga Directa

1. Descarga el proyecto como ZIP desde GitHub
2. Extrae el archivo
3. Abre terminal en la carpeta extraída
4. Sigue los pasos 2-5 de la Opción 1

## 📚 Tu Primera Sesión

### Paso 1: Verificar Instalación

Abre Python y ejecuta:

```python
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

print("✅ ¡Todo instalado correctamente!")
```

### Paso 2: Explorar los Datos

```python
# Cargar datos de ejemplo
import pandas as pd

df = pd.read_csv('data/raw/desembarques_pesqueros.csv')
print(df.head())
print(f"\nTotal de registros: {len(df)}")
```

### Paso 3: Tu Primera Transformación

```python
import sys
sys.path.append('src')

from processing import transform_landings_data

# Transformar datos
df_transformado = transform_landings_data(df)
print(df_transformado.columns)
```

## 🎯 Flujo de Trabajo Recomendado

```
1. Configuración Entorno (00) 
   ⬇️
2. Extracción Datos (01)
   ⬇️
3. Transformación (02)
   ⬇️
4. Carga (03)
   ⬇️
5. Visualización (04)
```

## ❓ Problemas Comunes

### "No module named 'pandas'"
**Solución**: Asegúrate de tener el entorno virtual activado y ejecuta:
```bash
pip install -r requirements.txt
```

### "Jupyter not found"
**Solución**: Instala Jupyter:
```bash
pip install jupyterlab
```

### "ModuleNotFoundError: No module named 'src'"
**Solución**: Asegúrate de ejecutar desde el directorio raíz del proyecto.

### Problemas con encoding en Windows
**Solución**: En tus scripts, usa:
```python
import sys
sys.stdout.reconfigure(encoding='utf-8')
```

## 📊 Datos de Ejemplo Generados

Al ejecutar `test_project.py`, se generan:

| Archivo | Registros | Descripción |
|---------|-----------|-------------|
| `desembarques_pesqueros.csv` | 2,880 | Capturas por puerto y especie |
| `datos_oceanograficos.csv` | 480 | Condiciones del mar por zona |
| `flota_pesquera.csv` | 200 | Características de embarcaciones |

## 🎓 Siguientes Pasos

Una vez que todo funcione:

1. ✅ Completa el Notebook 00 (Configuración)
2. ✅ Practica con el Notebook 01 (Extracción)
3. ✅ Experimenta con tus propios datos
4. ✅ Únete a la comunidad
5. ✅ Comparte tu progreso

## 💬 ¿Necesitas Ayuda?

- 📧 Email: fisheries.ai@comunidad.com
- 💬 Discord: [Próximamente]
- 🐙 Issues: [GitHub Issues](https://github.com/tu-usuario/ETL_for_Fisheries_Engineers/issues)

## 🎯 Checklist de Instalación

- [ ] Python 3.10+ instalado
- [ ] Entorno virtual creado
- [ ] Dependencias instaladas
- [ ] Datos de ejemplo generados
- [ ] Jupyter Lab funcionando
- [ ] Primer notebook abierto

## 🌟 Tips Finales

1. **Practica diariamente**: Aunque sea 30 minutos
2. **Toma notas**: En los propios notebooks
3. **Experimenta**: Modifica el código
4. **Pide ayuda**: La comunidad está aquí
5. **Comparte**: Tu aprendizaje inspira a otros

---

**¡Listo para comenzar! 🚢📊**

_Si esta guía te fue útil, ¡dale una ⭐ al proyecto!_
