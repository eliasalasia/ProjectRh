import pandas as pd
from sqlalchemy import create_engine

# Configuración de conexión a la base de datos
DATABASE_URL = "mssql+pyodbc://sa:tutor_elias@localhost/RecursosHumanos?driver=ODBC+Driver+17+for+SQL+Server"
engine = create_engine(DATABASE_URL)

print("Conexión a la base de datos exitosa")

# Consultar datos y guardarlos como CSV
empleados_df = pd.read_sql("SELECT * FROM Empleados", engine)
encuestas_df = pd.read_sql("SELECT * FROM EncuestasSatisfaccion", engine)
rotacion_df = pd.read_sql("SELECT * FROM RegistrosRotacion", engine)

print("Datos extraídos exitosamente")

empleados_df.to_csv('../datos/empleados.csv', index=False)
encuestas_df.to_csv('../datos/encuestas_satisfaccion.csv', index=False)
rotacion_df.to_csv('../datos/registros_rotacion.csv', index=False)

print("Datos guardados en archivos CSV exitosamente")
