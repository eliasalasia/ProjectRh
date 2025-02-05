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
sns.histplot(empleados_df['Salario'], kde=True, color='skyblue', edgecolor='black')
plt.axvline(empleados_df['Salario'].mean(), color='red', linestyle='--', linewidth=2, label='Alta')
plt.axvline(empleados_df['Salario'].median(), color='green', linestyle='-', linewidth=2, label='Media')
plt.title('Distribución de Salarios', fontsize=16)
plt.xlabel('Salario', fontsize=14)
plt.ylabel('Frecuencia', fontsize=14)
plt.legend(title='Estadísticos', fontsize=12)
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.show(block=True)  # Bloquea hasta que se cierre la ventana del gráfico

# Verificar si la columna 'Departamento' está presente antes de generar el gráfico
if 'Departamento' in encuestas_df.columns:
    # Gráfico de cajas de satisfacción laboral por departamento con conteo de empleados por departamento
    plt.figure(figsize=(12, 8))
    sns.boxplot(x='Puntaje', y='Departamento', data=encuestas_df, order=encuestas_df['Departamento'].value_counts().index, palette='coolwarm')
    plt.title('Satisfacción Laboral por Departamento', fontsize=16)
    plt.xlabel('Puntaje de Satisfacción', fontsize=14)
    plt.ylabel('Departamento', fontsize=14)

    # Añadir conteo de empleados por departamento
    dept_counts = encuestas_df['Departamento'].value_counts()
    for i, count in enumerate(dept_counts):
        plt.text(encuestas_df['Puntaje'].max() + 0.1, i, f'{count} empleados', verticalalignment='center', fontsize=12, color='black')

    plt.grid(axis='x', linestyle='--', alpha=0.7)
    plt.show(block=True)  # Bloquea hasta que se cierre la ventana del gráfico
else:
    print("La columna 'Departamento' no está presente en encuestas_df")

# Gráfico de barras de rotación de empleados por año
rotacion_df['AñoSalida'] = pd.to_datetime(rotacion_df['FechaSalida']).dt.year
plt.figure(figsize=(10, 6))
sns.countplot(x='AñoSalida', data=rotacion_df, palette='viridis', edgecolor='black')
plt.title('Rotación de Empleados por Año', fontsize=16)
plt.xlabel('Año de Salida', fontsize=14)
plt.ylabel('Cantidad de Empleados', fontsize=14)
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.show(block=True)  # Bloquea hasta que se cierre la ventana del gráfico

print("Gráficos generados exitosamente")
