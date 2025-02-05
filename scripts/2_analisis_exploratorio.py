import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Cargar datos
empleados_df = pd.read_csv('../datos/empleados.csv')
encuestas_df = pd.read_csv('../datos/encuestas_satisfaccion.csv')
rotacion_df = pd.read_csv('../datos/registros_rotacion.csv')

print("Datos cargados exitosamente")

# Verificar columnas disponibles en encuestas_df
print("Columnas en encuestas_df:", encuestas_df.columns)

# Análisis exploratorio
print("Análisis exploratorio de empleados")
print(empleados_df.describe())

print("Análisis exploratorio de encuestas de satisfacción")
print(encuestas_df.describe())

print("Análisis exploratorio de registros de rotación")
print(rotacion_df.describe())

# Visualización
print("Generando gráficos...")

# Gráfico de distribución de salarios con media y mediana
plt.figure(figsize=(10, 6))
sns.histplot(empleados_df['Salario'], kde=True)
plt.axvline(empleados_df['Salario'].mean(), color='r', linestyle='--', label='Media')
plt.axvline(empleados_df['Salario'].median(), color='g', linestyle='-', label='Mediana')
plt.title('Distribución de Salarios')
plt.xlabel('Salario')
plt.ylabel('Frecuencia')
plt.legend()
plt.show(block=True)  # Bloquea hasta que se cierre la ventana del gráfico

# Verificar si la columna 'Departamento' está presente antes de generar el gráfico
if 'Departamento' in encuestas_df.columns:
    # Gráfico de cajas de satisfacción laboral por departamento con conteo de empleados por departamento
    plt.figure(figsize=(12, 8))
    sns.boxplot(x='Puntaje', y='Departamento', data=encuestas_df, order=encuestas_df['Departamento'].value_counts().index)
    plt.title('Satisfacción Laboral por Departamento')
    plt.xlabel('Puntaje de Satisfacción')
    plt.ylabel('Departamento')

    # Añadir conteo de empleados por departamento
    dept_counts = encuestas_df['Departamento'].value_counts()
    for i, count in enumerate(dept_counts):
        plt.text(encuestas_df['Puntaje'].max() + 0.1, i, f'{count} empleados', verticalalignment='center')

    plt.show(block=True)  # Bloquea hasta que se cierre la ventana del gráfico
else:
    print("La columna 'Departamento' no está presente en encuestas_df")

# Gráfico de barras de rotación de empleados por año
rotacion_df['AñoSalida'] = pd.to_datetime(rotacion_df['FechaSalida']).dt.year
plt.figure(figsize=(10, 6))
sns.countplot(x='AñoSalida', data=rotacion_df, palette='viridis')
plt.title('Rotación de Empleados por Año')
plt.xlabel('Año de Salida')
plt.ylabel('Cantidad de Empleados')
plt.show(block=True)  # Bloquea hasta que se cierre la ventana del gráfico

print("Gráficos generados exitosamente")
