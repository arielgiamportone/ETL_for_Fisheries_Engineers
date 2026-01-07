"""
Utilidades para la obtención y generación de datos pesqueros
"""
import pandas as pd
import numpy as np
import requests
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
    # Crear datos de ejemplo para condiciones oceanográficas
    np.random.seed(43)
    
    # Definir zonas y años
    zonas = ['Norte', 'Centro-Norte', 'Centro', 'Centro-Sur', 'Sur']
    años = range(2015, 2023)
    meses = range(1, 13)
    
    # Crear registros
    registros = []
    for año in años:
        for mes in meses:
            for zona in zonas:
                # Base de temperatura según zona (de norte a sur)
                if zona == 'Norte':
                    base_temp = 18
                elif zona == 'Centro-Norte':
                    base_temp = 16
                elif zona == 'Centro':
                    base_temp = 14
                elif zona == 'Centro-Sur':
                    base_temp = 12
                else:  # Sur
                    base_temp = 8
                
                # Variación estacional
                temp_estacional = 4 * np.sin((mes-1)/12 * 2 * np.pi)
                
                # Temperatura final con ruido
                temperatura = base_temp + temp_estacional + np.random.normal(0, 0.5)
                
                # Salinidad (PSU)
                if zona in ['Norte', 'Centro-Norte']:
                    salinidad = np.random.normal(34.5, 0.3)
                else:
                    salinidad = np.random.normal(33.8, 0.2)
                
                # Oxígeno disuelto (ml/l) - inversamente relacionado con temperatura
                oxigeno = np.random.normal(8 - temperatura/4, 0.2)
                
                # Clorofila (mg/m³) - mayor en primavera
                if mes in [9, 10, 11]:  # Primavera
                    clorofila = np.random.gamma(3, 0.5)
                else:
                    clorofila = np.random.gamma(1, 0.5)
                
                # Añadir registro
                registros.append({
                    'fecha': f"{año}-{mes:02d}-15",
                    'zona': zona,
                    'temperatura_c': round(temperatura, 2),
                    'salinidad_psu': round(salinidad, 2),
                    'oxigeno_ml_l': round(oxigeno, 2),
                    'clorofila_mg_m3': round(clorofila, 2)
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
    # Crear datos de ejemplo para flota pesquera
    np.random.seed(44)
    
    # Definir tipos de embarcaciones
    tipos = ['Fresquero Costero', 'Fresquero de Altura', 'Congelador Arrastrero', 'Congelador Tangonero', 'Potero']
    puertos_base = ['Mar del Plata', 'Puerto Madryn', 'Ushuaia', 'Rawson', 'Comodoro Rivadavia']
    
    # Crear registros
    registros = []
    
    # Generar 200 embarcaciones
    for i in range(1, 201):
        # Asignar tipo
        tipo = np.random.choice(tipos)
        
        # Características según tipo
        if tipo == 'Fresquero Costero':
            eslora = np.random.uniform(10, 20)
            potencia = np.random.uniform(200, 400)
            capacidad = np.random.uniform(10, 30)
            tripulacion = np.random.randint(5, 12)
            año_construccion = np.random.randint(1980, 2010)
        elif tipo == 'Fresquero de Altura':
            eslora = np.random.uniform(25, 35)
            potencia = np.random.uniform(500, 800)
            capacidad = np.random.uniform(40, 80)
            tripulacion = np.random.randint(15, 25)
            año_construccion = np.random.randint(1985, 2015)
        elif tipo == 'Congelador Arrastrero':
            eslora = np.random.uniform(40, 60)
            potencia = np.random.uniform(1000, 1800)
            capacidad = np.random.uniform(100, 300)
            tripulacion = np.random.randint(30, 50)
            año_construccion = np.random.randint(1990, 2018)
        elif tipo == 'Congelador Tangonero':
            eslora = np.random.uniform(35, 55)
            potencia = np.random.uniform(900, 1600)
            capacidad = np.random.uniform(80, 250)
            tripulacion = np.random.randint(25, 45)
            año_construccion = np.random.randint(1990, 2018)
        else:  # Potero
            eslora = np.random.uniform(50, 70)
            potencia = np.random.uniform(1200, 2000)
            capacidad = np.random.uniform(200, 400)
            tripulacion = np.random.randint(40, 60)
            año_construccion = np.random.randint(1995, 2020)
        
        # Puerto base
        puerto_base = np.random.choice(puertos_base)
        
        # Especies objetivo según tipo
        if tipo == 'Fresquero Costero':
            especies_objetivo = np.random.choice(['Corvina, Pescadilla', 'Anchoíta, Caballa', 'Variado Costero'])
        elif tipo == 'Fresquero de Altura':
            especies_objetivo = np.random.choice(['Merluza, Abadejo', 'Merluza, Rayas', 'Variado de Altura'])
        elif tipo == 'Congelador Arrastrero':
            especies_objetivo = np.random.choice(['Merluza, Calamar', 'Merluza, Abadejo, Rayas', 'Polaca, Merluza de Cola'])
        elif tipo == 'Congelador Tangonero':
            especies_objetivo = 'Langostino'
        else:  # Potero
            especies_objetivo = 'Calamar'
        
        # Añadir registro
        registros.append({
            'id_buque': f"B{i:03d}",
            'nombre': f"PESQUERO {i}",
            'tipo': tipo,
            'eslora_m': round(eslora, 1),
            'potencia_hp': int(potencia),
            'capacidad_bodega_m3': round(capacidad, 1),
            'tripulacion': tripulacion,
            'año_construccion': año_construccion,
            'puerto_base': puerto_base,
            'especies_objetivo': especies_objetivo
        })
    
    # Crear DataFrame
    df = pd.DataFrame(registros)
    
    # Guardar en archivo
    os.makedirs(os.path.dirname(filename), exist_ok=True)
    df.to_csv(filename, index=False)
    
    return df