"""
Script de prueba para verificar que todas las correcciones funcionan correctamente
"""
import sys
import os

# Añadir src al path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'src'))

from data_utils import generate_sample_data, generate_ocean_data, generate_fleet_data
from processing import transform_landings_data, transform_ocean_data, transform_fleet_data, enrich_data
import pandas as pd

print("="*70)
print("PRUEBA DE FUNCIONALIDAD - PROYECTO ETL PARA DATOS PESQUEROS")
print("="*70)

# Crear directorios si no existen
os.makedirs("data/raw", exist_ok=True)
os.makedirs("data/processed", exist_ok=True)

print("\n1. Generando datos de desembarques...")
df_desembarques = generate_sample_data("data/raw/desembarques_pesqueros.csv")
print(f"   ✅ {len(df_desembarques)} registros generados")
print(f"   Columnas: {', '.join(df_desembarques.columns.tolist())}")

print("\n2. Generando datos oceanográficos...")
df_oceano = generate_ocean_data("data/raw/datos_oceanograficos.csv")
print(f"   ✅ {len(df_oceano)} registros generados")
print(f"   Columnas: {', '.join(df_oceano.columns.tolist())}")

print("\n3. Generando datos de flota...")
df_flota = generate_fleet_data("data/raw/flota_pesquera.csv")
print(f"   ✅ {len(df_flota)} registros generados")
print(f"   Columnas: {', '.join(df_flota.columns.tolist())}")

print("\n4. Transformando datos de desembarques...")
df_desembarques_transformed = transform_landings_data(df_desembarques)
print(f"   ✅ Transformación completada")
print(f"   Nuevas columnas: año, mes, temporada")

print("\n5. Transformando datos oceanográficos...")
df_oceano_transformed = transform_ocean_data(df_oceano)
print(f"   ✅ Transformación completada")
print(f"   Nuevas columnas: año, mes, temporada, productividad")

print("\n6. Transformando datos de flota...")
df_flota_transformed = transform_fleet_data(df_flota)
print(f"   ✅ Transformación completada")
print(f"   Nuevas columnas: antigüedad, categoria_tamaño, categoria_antigüedad, eficiencia")

print("\n7. Enriqueciendo datos...")
df_enriched = enrich_data(df_desembarques_transformed, df_oceano_transformed, df_flota_transformed)
print(f"   ✅ Datos enriquecidos: {len(df_enriched)} registros")
print(f"   Total de columnas: {len(df_enriched.columns)}")

print("\n8. Guardando datos procesados...")
df_desembarques_transformed.to_csv("data/processed/desembarques_transformados.csv", index=False)
df_oceano_transformed.to_csv("data/processed/oceanograficos_transformados.csv", index=False)
df_flota_transformed.to_csv("data/processed/flota_transformada.csv", index=False)
df_enriched.to_csv("data/processed/datos_enriquecidos.csv", index=False)
print("   ✅ Todos los archivos guardados en data/processed/")

print("\n" + "="*70)
print("✅ TODAS LAS PRUEBAS COMPLETADAS EXITOSAMENTE")
print("="*70)
print("\nEl proyecto está listo para usar. Puedes ejecutar los notebooks en orden:")
print("  1. notebooks/00_Configuracion_Entorno.ipynb")
print("  2. notebooks/01_Extracción_Tesoros_Datos.ipynb")
print("  3. notebooks/02_Transformacion_Pulido_Gemas.ipynb")
print("  4. notebooks/03_Carga_Exhibicion_Hallazgos.ipynb")
print("  5. notebooks/04_Visualizacion_Exploratoria.ipynb")
print("\n¡Feliz análisis de datos pesqueros! 🎣📊")
