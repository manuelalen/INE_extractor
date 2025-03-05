import requests
import pandas as pd
from sqlalchemy import create_engine
from dotenv import load_dotenv
import os

# 1️⃣ Cargar el archivo .env
dotenv_path = r'C:\Users\manue\OneDrive\Documentos\Data Analytics\.env'
load_dotenv(dotenv_path)

# 2️⃣ Obtener las credenciales del entorno
usuario = os.getenv('MYSQL_USER')
contraseña = os.getenv('MYSQL_PASSWORD')
host = os.getenv('MYSQL_HOST')
base_datos = os.getenv('MYSQL_DB')

# 3️⃣ Crear la conexión después de definir las variables
engine = create_engine(f"mysql+pymysql://{usuario}:{contraseña}@{host}/{base_datos}")

# URL de la API del INE
url = "https://servicios.ine.es/wstempus/js/ES/DATOS_TABLA/24900"

# Petición a la API
response = requests.get(url)
data = response.json()

# Procesar datos
datos = []
for serie in data:
    nombre = serie['Nombre'].replace('Base 2006. Anual.', '').strip()
    partes = [parte.strip() for parte in nombre.split('.') if parte.strip()]
    
    while len(partes) < 4:
        partes.append(None)
    
    for registro in serie['Data']:
        fila = {
            'indice': partes[0],
            'dato': partes[1],
            'tipo_dato': partes[2],
            'descripcion': partes[3],
            'anyo': registro['Anyo'],
            'valor': registro['Valor'],
            'secreto': registro['Secreto']
        }
        datos.append(fila)

# Crear DataFrame
df = pd.DataFrame(datos)

# Insertar en MySQL (crea la tabla si no existe)
df.to_sql('ine_gastos_medios_anuales', con=engine, if_exists='replace', index=False)

print("✅ Datos insertados correctamente en la tabla 'ine_gastos_medios_anuales'")


