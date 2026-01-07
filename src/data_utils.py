"""
Utilidades para la obtención y generación de datos pesqueros
"""
import pandas as pd
import numpy as np
import os
from datetime import datetime

def get_data(url, filename, force_download=False):
    """
    Descarga datos desde una URL o carga desde local si ya existen
    """
    if os.path.exists(filename) and not force_download:
        print(f"Cargando datos desde archivo local: {filename}")
        try:
            return pd.read_csv(filename)
        except Exception as e:
            print(f"Error al cargar desde local {filename}: {e}. Intentando generar datos de ejemplo.")
            return generate_sample_data(filename) # Asegurarse que generate_sample_data esté definida antes o importada
    else:
        print(f"Intentando descargar datos desde: {url}")
        # Crear directorio si no existe
        os.makedirs(os.path.dirname(filename), exist_ok=True)

        # Descargar datos
        try:
            response = requests.get(url, timeout=10) # Añadir timeout
            response.raise_for_status()  # Verificar si la descarga fue exitosa

            # Guardar datos en archivo local
            with open(filename, 'wb') as f:
                f.write(response.content)
            print(f"Datos descargados y guardados en: {filename}")

            # Cargar datos en DataFrame
            return pd.read_csv(filename)
        except requests.exceptions.RequestException as e:
            print(f"Error al descargar datos desde {url}: {e}")
            print("Generando datos de ejemplo...")
            return generate_sample_data(filename)
        except Exception as e: # Capturar otros posibles errores al leer el CSV
             print(f"Error inesperado al procesar {url} o {filename}: {e}")
             print("Generando datos de ejemplo...")
             return generate_sample_data(filename)

def generate_sample_data(filename):
    """
    Genera datos de ejemplo para desembarques pesqueros
    """
    # Crear datos de ejemplo para desembarques
    np.random.seed(42)

    # Definir puertos, especies y años
    puertos = ['Mar del Plata', 'Puerto Madryn', 'Ushuaia', 'Rawson', 'Comodoro Rivadavia']
    especies = ['Merluza', 'Calamar', 'Langostino', 'Corvina', 'Anchoíta', 'Caballa']
    años = range(2015, 2023)
    meses = range(1, 13)

    # Crear registros
    registros = []
    for año in años:
        for mes in meses:
            for puerto in puertos:
                for especie in especies:
                    # Simular estacionalidad y tendencias
                    base_captura = np.random.gamma(5, 20)  # Distribución gamma para capturas

                    # Factores estacionales por especie
                    if especie == 'Langostino' and mes in [10, 11, 12, 1, 2]:
                        factor_estacional = 2.5  # Temporada alta
                    elif especie == 'Calamar' and mes in [1, 2, 3, 4]:
                        factor_estacional = 3.0  # Temporada alta
                    elif especie == 'Merluza':
                        factor_estacional = 1.0 + 0.3 * np.sin(mes/12 * 2 * np.pi)  # Ciclo anual
                    else:
                        factor_estacional = 1.0

                    # Tendencia a largo plazo (algunas especies aumentan, otras disminuyen)
                    if especie in ['Merluza', 'Corvina']:
                        factor_tendencia = 1.0 - 0.03 * (año - 2015)  # Disminución gradual
                    elif especie in ['Langostino']:
                        factor_tendencia = 1.0 + 0.05 * (año - 2015)  # Aumento gradual
                    else:
                        factor_tendencia = 1.0

                    # Calcular captura final
                    captura = max(0, base_captura * factor_estacional * factor_tendencia)

                    # Valor económico (precio por kg)
                    if especie == 'Langostino':
                        precio_kg = np.random.normal(15, 2)
                    elif especie == 'Calamar':
                        precio_kg = np.random.normal(8, 1)
                    elif especie == 'Merluza':
                        precio_kg = np.random.normal(5, 0.5)
                    else:
                        precio_kg = np.random.normal(6, 1)

                    # Valor total
                    valor = captura * precio_kg

                    # Añadir registro
                    registros.append({
                        'fecha': f"{año}-{mes:02d}-01",
                        'puerto': puerto,
                        'especie': especie,
                        'captura_ton': round(captura, 2),
                        'precio_kg_usd': round(precio_kg, 2),
                        'valor_total_usd': round(valor, 2)
                    })

    # Crear DataFrame
    df = pd.DataFrame(registros)

    # Guardar en archivo
    os.makedirs(os.path.dirname(filename), exist_ok=True)
    df.to_csv(filename, index=False)

    return df

def generate_ocean_data(filename):
    """
    Genera datos oceanográficos de ejemplo
    """
    # Crear datos de ejemplo para desembarques
    np.random.seed(42)

    # Definir puertos, especies y años
    puertos = ['Mar del Plata', 'Puerto Madryn', 'Ushuaia', 'Rawson', 'Comodoro Rivadavia']
    especies = ['Merluza', 'Calamar', 'Langostino', 'Corvina', 'Anchoíta', 'Caballa']
    años = range(2015, 2023)
    meses = range(1, 13)

    # Crear registros
    registros = []
    for año in años:
        for mes in meses:
            for puerto in puertos:
                for especie in especies:
                    # Simular estacionalidad y tendencias
                    base_captura = np.random.gamma(5, 20)  # Distribución gamma para capturas

                    # Factores estacionales por especie
                    if especie == 'Langostino' and mes in [10, 11, 12, 1, 2]:
                        factor_estacional = 2.5  # Temporada alta
                    elif especie == 'Calamar' and mes in [1, 2, 3, 4]:
                        factor_estacional = 3.0  # Temporada alta
                    elif especie == 'Merluza':
                        factor_estacional = 1.0 + 0.3 * np.sin(mes/12 * 2 * np.pi)  # Ciclo anual
                    else:
                        factor_estacional = 1.0

                    # Tendencia a largo plazo (algunas especies aumentan, otras disminuyen)
                    if especie in ['Merluza', 'Corvina']:
                        factor_tendencia = 1.0 - 0.03 * (año - 2015)  # Disminución gradual
                    elif especie in ['Langostino']:
                        factor_tendencia = 1.0 + 0.05 * (año - 2015)  # Aumento gradual
                    else:
                        factor_tendencia = 1.0

                    # Calcular captura final
                    captura = max(0, base_captura * factor_estacional * factor_tendencia)

                    # Valor económico (precio por kg)
                    if especie == 'Langostino':
                        precio_kg = np.random.normal(15, 2)
                    elif especie == 'Calamar':
                        precio_kg = np.random.normal(8, 1)
                    elif especie == 'Merluza':
                        precio_kg = np.random.normal(5, 0.5)
                    else:
                        precio_kg = np.random.normal(6, 1)

                    # Valor total
                    valor = captura * precio_kg

                    # Añadir registro
                    registros.append({
                        'fecha': f"{año}-{mes:02d}-01",
                        'puerto': puerto,
                        'especie': especie,
                        'captura_ton': round(captura, 2),
                        'precio_kg_usd': round(precio_kg, 2),
                        'valor_total_usd': round(valor, 2)
                    })

    # Crear DataFrame
    df = pd.DataFrame(registros)

    # Guardar en archivo
    os.makedirs(os.path.dirname(filename), exist_ok=True)
    df.to_csv(filename, index=False)

    return df

def generate_fleet_data(filename):
    """
    Genera datos de flota pesquera de ejemplo
    """
    # Crear datos de ejemplo para desembarques
    np.random.seed(42)

    # Definir puertos, especies y años
    puertos = ['Mar del Plata', 'Puerto Madryn', 'Ushuaia', 'Rawson', 'Comodoro Rivadavia']
    especies = ['Merluza', 'Calamar', 'Langostino', 'Corvina', 'Anchoíta', 'Caballa']
    años = range(2015, 2023)
    meses = range(1, 13)

    # Crear registros
    registros = []
    for año in años:
        for mes in meses:
            for puerto in puertos:
                for especie in especies:
                    # Simular estacionalidad y tendencias
                    base_captura = np.random.gamma(5, 20)  # Distribución gamma para capturas

                    # Factores estacionales por especie
                    if especie == 'Langostino' and mes in [10, 11, 12, 1, 2]:
                        factor_estacional = 2.5  # Temporada alta
                    elif especie == 'Calamar' and mes in [1, 2, 3, 4]:
                        factor_estacional = 3.0  # Temporada alta
                    elif especie == 'Merluza':
                        factor_estacional = 1.0 + 0.3 * np.sin(mes/12 * 2 * np.pi)  # Ciclo anual
                    else:
                        factor_estacional = 1.0

                    # Tendencia a largo plazo (algunas especies aumentan, otras disminuyen)
                    if especie in ['Merluza', 'Corvina']:
                        factor_tendencia = 1.0 - 0.03 * (año - 2015)  # Disminución gradual
                    elif especie in ['Langostino']:
                        factor_tendencia = 1.0 + 0.05 * (año - 2015)  # Aumento gradual
                    else:
                        factor_tendencia = 1.0

                    # Calcular captura final
                    captura = max(0, base_captura * factor_estacional * factor_tendencia)

                    # Valor económico (precio por kg)
                    if especie == 'Langostino':
                        precio_kg = np.random.normal(15, 2)
                    elif especie == 'Calamar':
                        precio_kg = np.random.normal(8, 1)
                    elif especie == 'Merluza':
                        precio_kg = np.random.normal(5, 0.5)
                    else:
                        precio_kg = np.random.normal(6, 1)

                    # Valor total
                    valor = captura * precio_kg

                    # Añadir registro
                    registros.append({
                        'fecha': f"{año}-{mes:02d}-01",
                        'puerto': puerto,
                        'especie': especie,
                        'captura_ton': round(captura, 2),
                        'precio_kg_usd': round(precio_kg, 2),
                        'valor_total_usd': round(valor, 2)
                    })

    # Crear DataFrame
    df = pd.DataFrame(registros)

    # Guardar en archivo
    os.makedirs(os.path.dirname(filename), exist_ok=True)
    df.to_csv(filename, index=False)

    return df