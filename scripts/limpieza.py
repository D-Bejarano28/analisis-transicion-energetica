import os
import pandas as pd
from sqlalchemy import create_engine
from dotenv import load_dotenv

load_dotenv()
engine = create_engine(f"postgresql://{os.getenv('DB_USER')}:{os.getenv('DB_PASSWORD')}@{os.getenv('DB_HOST')}:{os.getenv('DB_PORT')}/{os.getenv('DB_NAME')}")

def transformar_datos():
    try:
        #Leer los datos de la base
        df = pd.read_sql("SELECT * FROM energia_renovable_latam", engine)
        print(" Datos leídos desde PostgreSQL...")

        
        # Llenamos los nulos con 0 para no arruinar los cálculos
        df = df.fillna(0)

        
        # Calculamos el total de renovables sumando las fuentes
        df['total_solar_wind'] = df['solar_electricity'] + df['wind_electricity']
        
        # % de contribución solar respecto al total de renovables
        # Usamos una función para evitar división por cero
        df['pct_solar'] = (df['solar_electricity'] / df['renewables_electricity'].replace(0, 1)) * 100

        # Clasificación por "Era"
        # Esto ayudará a filtrar en Power BI de forma más humana
        df['periodo'] = df['year'].apply(lambda x: 'Pre-2015' if x < 2015 else 'Post-Acuerdo de Paris')

        #Guardar los datos ya "Pulidos" en una nueva tabla
        df.to_sql('bi_energia_limpia', engine, if_exists='replace', index=False)
        print(" ¡Datos transformados y guardados en 'bi_energia_limpia'!")

    except Exception as e:
        print(f" Error en la transformación: {e}")

if __name__ == "__main__":
    transformar_datos()