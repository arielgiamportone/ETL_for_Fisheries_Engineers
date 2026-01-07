"""
Funciones para procesamiento y transformación de datos pesqueros
"""
import pandas as pd
import numpy as np
from datetime import datetime


def transform_landings_data(df):
    """
    Transforma y limpia datos de desembarques
    
    Args:
        df: DataFrame con datos de desembarques
        
    Returns:
        DataFrame transformado
    """
    df = df.copy()
    
    # Convertir fecha a datetime
    df['fecha'] = pd.to_datetime(df['fecha'])
    
    # Extraer año y mes
    df['año'] = df['fecha'].dt.year
    df['mes'] = df['fecha'].dt.month
    
    # Normalizar nombres a mayúsculas
    df['puerto'] = df['puerto'].str.upper()
    df['especie'] = df['especie'].str.upper()
    
    # Crear columna de temporada
    condiciones = [
        (df['mes'] >= 3) & (df['mes'] <= 5),
        (df['mes'] >= 6) & (df['mes'] <= 8),
        (df['mes'] >= 9) & (df['mes'] <= 11),
        (df['mes'] == 12) | (df['mes'] <= 2)
    ]
    temporadas = ['Otoño', 'Invierno', 'Primavera', 'Verano']
    df['temporada'] = np.select(condiciones, temporadas, default='Desconocido')
    
    return df


def transform_ocean_data(df):
    """
    Transforma y limpia datos oceanográficos
    
    Args:
        df: DataFrame con datos oceanográficos
        
    Returns:
        DataFrame transformado
    """
    df = df.copy()
    
    # Convertir fecha a datetime
    df['fecha'] = pd.to_datetime(df['fecha'])
    
    # Extraer año y mes
    df['año'] = df['fecha'].dt.year
    df['mes'] = df['fecha'].dt.month
    
    # Normalizar nombres de zonas
    df['zona'] = df['zona'].str.upper()
    
    # Crear columna de temporada
    condiciones = [
        (df['mes'] >= 3) & (df['mes'] <= 5),
        (df['mes'] >= 6) & (df['mes'] <= 8),
        (df['mes'] >= 9) & (df['mes'] <= 11),
        (df['mes'] == 12) | (df['mes'] <= 2)
    ]
    temporadas = ['Otoño', 'Invierno', 'Primavera', 'Verano']
    df['temporada'] = np.select(condiciones, temporadas, default='Desconocido')
    
    # Crear categorías de productividad basadas en clorofila
    df['productividad'] = pd.cut(
        df['clorofila_mg_m3'],
        bins=[0, 1, 2, 5, float('inf')],
        labels=['Baja', 'Media', 'Alta', 'Muy Alta']
    )
    
    return df


def transform_fleet_data(df):
    """
    Transforma y limpia datos de flota
    
    Args:
        df: DataFrame con datos de flota
        
    Returns:
        DataFrame transformado
    """
    df = df.copy()
    
    # Normalizar puerto base
    df['puerto_base'] = df['puerto_base'].str.upper()
    
    # Calcular antigüedad de las embarcaciones
    año_actual = datetime.now().year
    df['antigüedad'] = año_actual - df['año_construccion']
    
    # Categorizar por tamaño
    df['categoria_tamaño'] = pd.cut(
        df['eslora_m'],
        bins=[0, 20, 35, 50, float('inf')],
        labels=['Pequeño', 'Mediano', 'Grande', 'Muy Grande']
    )
    
    # Categorizar por antigüedad
    df['categoria_antigüedad'] = pd.cut(
        df['antigüedad'],
        bins=[0, 10, 20, 30, float('inf')],
        labels=['Nueva', 'Media', 'Antigua', 'Muy Antigua']
    )
    
    # Crear columna de eficiencia (relación capacidad/potencia)
    df['eficiencia'] = df['capacidad_bodega_m3'] / df['potencia_hp']
    
    return df


def enrich_data(df_landings, df_ocean, df_fleet):
    """
    Combina y enriquece los datos de diferentes fuentes
    
    Args:
        df_landings: DataFrame con datos de desembarques
        df_ocean: DataFrame con datos oceanográficos
        df_fleet: DataFrame con datos de flota
        
    Returns:
        DataFrame enriquecido
    """
    # Mapeo de puertos a zonas oceanográficas
    mapeo_puerto_zona = {
        'MAR DEL PLATA': 'CENTRO',
        'PUERTO MADRYN': 'CENTRO-SUR',
        'USHUAIA': 'SUR',
        'RAWSON': 'CENTRO-SUR',
        'COMODORO RIVADAVIA': 'CENTRO-SUR'
    }
    
    # Aplicar mapeo a desembarques
    df_landings = df_landings.copy()
    df_landings['zona_oceanografica'] = df_landings['puerto'].map(mapeo_puerto_zona)
    
    # Crear un DataFrame con datos oceanográficos mensuales por zona
    df_ocean_mensual = df_ocean.groupby(['año', 'mes', 'zona']).agg({
        'temperatura_c': 'mean',
        'salinidad_psu': 'mean',
        'oxigeno_ml_l': 'mean',
        'clorofila_mg_m3': 'mean',
        'productividad': lambda x: x.mode()[0] if not x.mode().empty else None
    }).reset_index()
    
    # Unir datos de desembarques con datos oceanográficos
    df_enriched = pd.merge(
        df_landings,
        df_ocean_mensual,
        how='left',
        left_on=['año', 'mes', 'zona_oceanografica'],
        right_on=['año', 'mes', 'zona']
    )
    
    # Eliminar columna redundante
    if 'zona' in df_enriched.columns:
        df_enriched = df_enriched.drop('zona', axis=1)
    
    return df_enriched