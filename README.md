# Proyecto ETL - COVID-19 en Estados Unidos

Este proyecto tiene como objetivo realizar un proceso completo de **Extracción, Transformación y Carga (ETL)** sobre datos relacionados con la pandemia de COVID-19 en Estados Unidos. Los datos procesados se utilizan para generar visualizaciones y análisis exploratorios en Power BI.

## 🗂 Estructura del Proyecto

```
COVID-ETL/
├── archived_data/
├── csse_covid_19_data/
├── who_covid_19_situation_reports/
├── data/
│   ├── resumen_dashboard.csv
│   ├── state_metadata.csv
│   └── historico_us.parquet
├── notebooks/
│   ├── Análisis1.ipynb
│   └── Análisis2.ipynb
├── src/
│   ├── etl.py
│   ├── clean.py
│   └── config.py
├── requirements.txt
└── README.md
```

## 📥 Fuente de los Datos

Los datos utilizados en este proyecto fueron obtenidos desde un repositorio público de GitHub:

- [CSSE COVID-19 Data - Johns Hopkins University](https://github.com/CSSEGISandData/COVID-19)

Estos datos incluyen información diaria de casos confirmados, muertes, tasas de letalidad, y nuevos contagios por estado en Estados Unidos.

## ⚙️ Descripción de los Scripts

### `etl.py`

Este script realiza el proceso principal de **extracción, transformación y carga**:

- Extrae datos crudos desde archivos CSV de la carpeta `csse_covid_19_data`.
- Realiza limpieza y conversión de fechas.
- Calcula métricas como casos nuevos, muertes nuevas, y CFR (case fatality rate).
- Combina información con metadatos del estado.
- Exporta el archivo consolidado a `resumen_dashboard.csv`.

### `clean.py`

Script auxiliar encargado de la **limpieza de datos**:

- Convierte fechas a formato estándar.
- Elimina valores nulos y columnas irrelevantes.
- Convierte tipos de datos para facilitar el análisis.

Este script se importa dentro de `etl.py` para separar responsabilidades y mantener un código más limpio y modular.

### `config.py`

Contiene configuraciones globales del proyecto:

- Rutas a los archivos fuente y destino.
- Nombres de columnas clave.
- Parámetros generales para reutilizar en otros scripts.

## 📓 Notebooks

### `Análisis1.ipynb`

- Carga y exploración inicial del dataset limpio.
- Estadísticas descriptivas.
- Distribución de casos por estado.

### `Análisis2.ipynb`

- Gráficas de evolución temporal de KPIs como casos confirmados, muertes y CFR.
- Filtrado por estados y comparación entre ellos.
- Resultados exportados para visualización en Power BI.

## 📊 Visualización

La información procesada se visualiza en **Power BI**, incluyendo:

- KPIs dinámicos por estado y periodo.
- Gráficos comparativos.
- Alertas automáticas basadas en condiciones críticas.
- Cambio de modo Iluminado/Oscuro

## ✅ Requisitos

Instala las dependencias con:

```bash
pip install -r requirements.txt
```

## 💡 Autor

Este proyecto fue desarrollado por Elena Chávez como parte de una práctica de análisis de datos con enfoque en ingeniería de datos y visualización.