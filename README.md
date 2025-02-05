# Proyecto de Análisis y Predicción de Rotación de Empleados

Este proyecto realiza un análisis de datos de empleados, encuestas de satisfacción y registros de rotación de personal. Además, implementa un modelo predictivo para identificar posibles rotaciones de empleados.

## Estructura del Proyecto

```
.
├── datos/                     # Archivos CSV extraídos de la base de datos
├── informes/                  # Informes generados a partir del análisis
├── scripts/                   # Código fuente
│   ├── 1_extraccion_datos.py  # Extracción de datos desde la base de datos SQL Server
│   ├── 2_analisis_datos.py    # Análisis exploratorio de los datos extraídos
│   ├── 3_modelo_predictivo.py # Entrenamiento y evaluación de modelos de predicción
```

## Requisitos Previos

Antes de ejecutar los scripts, asegúrate de tener instaladas las siguientes dependencias:

```sh
pip install pandas sqlalchemy pyodbc seaborn matplotlib scikit-learn
```

## Descripción de los Scripts

### 1. Extracción de Datos (`1_extraccion_datos.py`)

- Se conecta a una base de datos SQL Server utilizando `SQLAlchemy`.
- Extrae datos de las tablas `Empleados`, `EncuestasSatisfaccion` y `RegistrosRotacion`.
- Guarda los datos en archivos CSV dentro del directorio `datos/`.

#### Ejecución:
```sh
python scripts/1_extraccion_datos.py
```

---

### 2. Análisis Exploratorio (`2_analisis_datos.py`)

- Carga los datos extraídos desde los archivos CSV.
- Realiza un análisis exploratorio mediante descripciones estadísticas.
- Genera visualizaciones de:
  - Distribución de salarios
  - Satisfacción laboral por departamento
  - Rotación de empleados por año
- Guarda los gráficos en la carpeta `informes/`.

#### Ejecución:
```sh
python scripts/2_analisis_datos.py
```

---

### 3. Modelo Predictivo (`3_modelo_predictivo.py`)

- Carga y preprocesa los datos de empleados y rotación.
- Entrena tres modelos:
  - `RandomForestClassifier`
  - `LogisticRegression`
  - `SVC` (Máquinas de Soporte Vectorial)
- Evalúa los modelos en base a:
  - Precisión (accuracy)
  - Recall y F1-Score
- Genera un informe con recomendaciones en `informes/informe_recomendaciones.txt`.

#### Ejecución:
```sh
python scripts/3_modelo_predictivo.py
```

## Resultados y Recomendaciones

Los resultados del modelo predictivo se almacenan en el archivo `informes/informe_recomendaciones.txt`, donde se incluyen métricas clave y una explicación simplificada para la toma de decisiones.



