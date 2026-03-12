import os
from sqlalchemy import create_engine
from dotenv import load_dotenv
import pandas as pd

# 1. Cargar variables del archivo .env
load_dotenv()

user = os.getenv('DB_USER')
password = os.getenv('DB_PASSWORD')
host = os.getenv('DB_HOST')
port = os.getenv('DB_PORT')
db = os.getenv('DB_NAME')

# 2. Crear la URL de conexión (Point to port 5433)
connection_url = f"postgresql://{user}:{password}@{host}:{port}/{db}"

try:
    # 3. Intentar conectar
    engine = create_engine(connection_url)
    with engine.connect() as conn:
        print("✅ ¡Conexión exitosa entre Python y PostgreSQL en Docker!")
        
    # 4. Crear un mini DataFrame de prueba
    df_test = pd.DataFrame({'status': ['Conectado'], 'proyecto': ['Energía Ambiental']})
    
    # 5. Subirlo a la DB para probar escritura
    df_test.to_sql('test_table', engine, if_exists='replace', index=False)
    print("✅ Tabla de prueba creada correctamente en pgAdmin.")

except Exception as e:
    print(f"❌ Error al conectar: {e}")