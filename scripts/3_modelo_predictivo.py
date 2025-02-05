import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.svm import SVC
from sklearn.metrics import classification_report, accuracy_score
import matplotlib.pyplot as plt
import os

# Cargar datos
empleados_df = pd.read_csv('../datos/empleados.csv')
rotacion_df = pd.read_csv('../datos/registros_rotacion.csv')

print("Datos cargados exitosamente")

# Verificar que todos los empleados en rotacion_df están en empleados_df
rotacion_df = rotacion_df[rotacion_df['EmpleadoID'].isin(empleados_df['ID'])]

# Preprocesamiento de datos
print("Preprocesando datos...")

# Codificar variables categóricas
label_encoder = LabelEncoder()
empleados_df['Departamento'] = label_encoder.fit_transform(empleados_df['Departamento'])

# Crear variable objetivo (y) y características (X)
X = empleados_df[['Salario', 'Departamento']]
rotacion_df['Rotacion'] = rotacion_df['FechaSalida'].apply(lambda x: 1 if pd.notnull(x) else 0)
y = rotacion_df.set_index('EmpleadoID').reindex(empleados_df['ID']).fillna(0)['Rotacion']

# Escalar características
scaler = StandardScaler()
X = scaler.fit_transform(X)

# Dividir datos en entrenamiento y prueba
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Entrenar y evaluar múltiples modelos
modelos = {
    'RandomForest': RandomForestClassifier(),
    'LogisticRegression': LogisticRegression(),
    'SVM': SVC()
}

resultados = {}

for nombre, modelo in modelos.items():
    modelo.fit(X_train, y_train)
    y_pred = modelo.predict(X_test)
    accuracy = accuracy_score(y_test, y_pred) * 100  # Convertir precisión a porcentaje
    resultados[nombre] = {
        'accuracy': accuracy,
        'report': classification_report(y_test, y_pred, output_dict=True, zero_division=0)
    }

# Generar informe de recomendaciones basado en los resultados
informe = []

for nombre, resultado in resultados.items():
    informe.append(f"**Modelo: {nombre}**")
    informe.append(f"**Precisión: {resultado['accuracy']:.2f}%**")
    informe.append("**Reporte de clasificación:**")
    informe.append("")

    # Formatear el reporte de clasificación
    report = resultado['report']
    informe.append(f"| Clase | Precisión (%) | Recall (%) | F1-Score | Soporte |")
    informe.append(f"|-------|----------------|------------|----------|---------|")
    for clase, metrics in report.items():
        if isinstance(metrics, dict):
            informe.append(f"| {clase} | {metrics['precision'] * 100:.2f} | {metrics['recall'] * 100:.2f} | {metrics['f1-score']:.2f} | {metrics['support']} |")

    informe.append("")

    # Simplificar términos para los empresarios
    informe.append("**Explicación simplificada:**")
    informe.append(f"- La precisión del modelo {nombre} es {resultado['accuracy']:.2f}%, lo que significa que predice correctamente el {resultado['accuracy']:.2f}% de las veces.")
    informe.append("- Cuando se menciona 'Precisión', se refiere a la exactitud del modelo al predecir la rotación de empleados.")
    informe.append("- 'Recall' indica qué tan bien el modelo identifica a los empleados que efectivamente rotan.")
    informe.append("- 'F1-Score' es una combinación de la precisión y el recall.")
    informe.append("- 'Soporte' es la cantidad de empleados que pertenecen a cada categoría (0 = no rotan, 1 = rotan).")
    informe.append("-" * 40)

# Crear el directorio si no existe
os.makedirs('../informes', exist_ok=True)

# Guardar informe en un archivo de texto
with open('../informes/informe_recomendaciones.txt', 'w') as file:
    file.write("\n".join(informe))

print("Modelos entrenados y evaluados exitosamente")
print("Informe de recomendaciones generado y guardado en '../informes/informe_recomendaciones.txt'")

# Visualización de la importancia de las características para el modelo RandomForest
importances = modelos['RandomForest'].feature_importances_ * 100  # Convertir importancia a porcentaje
features = ['Salario', 'Departamento']

plt.figure(figsize=(10, 6))
plt.bar(features, importances, color=['blue', 'green'])
plt.title('Importancia de las Características en la Predicción de Rotación', fontsize=16)
plt.xlabel('Características', fontsize=14)
plt.ylabel('Importancia (%)', fontsize=14)  # Mostrar en porcentaje
plt.xticks(fontsize=12)
plt.yticks(fontsize=12)
plt.grid(axis='y', linestyle='--', alpha=0.7)

# Anotaciones
for i, v in enumerate(importances):
    plt.text(i, v + 1, f"{v:.2f}%", color='black', ha='center', fontsize=12)  # Mostrar en porcentaje

plt.show()

# Análisis y recomendaciones basadas en la importancia de las características
analisis_recomendaciones = """
Análisis de Importancia de Características:
- **Salario**: Tiene una importancia del {:.2f}% en la predicción de rotación. Esto sugiere que el salario es un factor significativo en la decisión de los empleados de permanecer o dejar la empresa.
- **Departamento**: Tiene una importancia del {:.2f}%. Esto indica que el departamento en el que trabaja un empleado también influye en la rotación, aunque en menor medida que el salario.

Recomendaciones:
1. **Revisión de Salarios**: Considerar ajustes salariales para retener a los empleados, especialmente en departamentos con alta rotación.
2. **Mejoras en Departamentos**: Implementar programas de desarrollo y satisfacción laboral en departamentos con mayor rotación.
""".format(importances[0], importances[1])  # Convertir importancia a porcentaje

# Guardar análisis y recomendaciones en el informe
with open('../informes/informe_recomendaciones.txt', 'a') as file:
    file.write("\n\nAnálisis y Recomendaciones:\n")
    file.write(analisis_recomendaciones)

print("Análisis y recomendaciones añadidos al informe.")
