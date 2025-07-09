# src/config.py
from pathlib import Path

# Raíz del proyecto
BASE_DIR = Path(__file__).resolve().parent.parent

# Ruta a los CSV diarios de EE. UU.
RAW_DATA_PATH = BASE_DIR / "COVID-19" / "csse_covid_19_data" / "csse_covid_19_daily_reports_us"

# Ruta de salida de la tabla histórica
OUTPUT_PATH = BASE_DIR / "data" / "historico_us.parquet"

# Ruta de salida de la información adicional por estado
META_PATH     = BASE_DIR / "data" / "state_metadata.csv" 

#Se usó .parquet porque es un formato columnar, comprimido y eficiente
