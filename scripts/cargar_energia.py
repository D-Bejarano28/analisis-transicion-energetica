import os
import pandas as pd
from sqlalchemy import create_engine
from dotenv import load_dotenv

# 1. Configuración de conexión
load_dotenv()
engine = create_engine(f"postgresql://{os.getenv('DB_USER')}:{os.getenv('DB_PASSWORD')}@{os.getenv('DB_HOST')}:{os.getenv('DB_PORT')}/{os.getenv('DB_NAME')}")

# 2. URL del Dataset oficial (Energy Mix)
URL_DATA = "https://raw.githubusercontent.com/owid/energy-data/master/owid-energy-data.csv"

def run_etl():
    try:
        print("📥 Descargando datos de energía (esto puede tardar unos segundos)...")
        df = pd.read_csv(URL_DATA)
        
        # 3. Personalización (Para no ser igual al tutorial)
        # Vamos a filtrar solo datos desde el año 2000 y solo para países sudamericanos
        paises_latam = ['Argentina', 'Brazil', 'Chile', 'Colombia', 'Ecuador', 'Mexico', 'Peru', 'Uruguay', 'Venezuela']
        
        df_latam = df[(df['country'].isin(paises_latam)) & (df['year'] >= 2000)].copy()
        
        # 4. Limpieza básica: Seleccionamos columnas clave de renovables
        columnas_interes = [
            'country', 'year', 'population', 'gdp',
            'biofuel_electricity', 'hydro_electricity', 'solar_electricity', 
            'wind_electricity', 'renewables_electricity'
        ]
        df_final = df_latam[columnas_interes]
        
        print(f" Datos filtrados: {df_final.shape[0]} registros encontrados.")

        # 5. Carga a PostgreSQL
        df_final.to_sql('energia_renovable_latam', engine, if_exists='replace', index=False)
        print(" ¡Datos cargados exitosamente en la tabla 'energia_renovable_latam'!")

    except Exception as e:
        print(f" Error en el proceso: {e}")

if __name__ == "__main__":
    run_etl()