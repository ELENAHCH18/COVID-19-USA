"""
clean.py
--------
Aquí defino las Funciones de limpieza y enriquecimiento del DataFrame histórico
resultado del ETL de reportes COVID-19 EE. UU.
"""

import pandas as pd

# Columnas a borrar porque no se necesitan
DROP_COLS = ["Last_Update", "Date", "Lat", "Long_", "FIPS"]

# Columnas que deben quedar en 0 si llegan nulas
ZERO_FILL = ["new_cases", "new_deaths"]

# Columnas a las que les haremos forward-fill por estado
FFILL_COLS = ["People_Hospitalized", "Hospitalization_Rate"]


def add_derived_columns(df: pd.DataFrame) -> pd.DataFrame:
    """Crea columnas derivadas que te interesan para el dashboard."""
    df["incident_rate"] = (df["confirmed"] / df["population"]) * 1e5
    df["cfr"] = (df["deaths"] / df["confirmed"]).round(4)
    return df


def fill_nulls(df: pd.DataFrame) -> pd.DataFrame:
    """Aplica reglas de imputación / forward-fill básicas."""
    # Relleno con 0 para derivadas
    df[ZERO_FILL] = df[ZERO_FILL].fillna(0)

    # Forward-fill por estado
    df = df.sort_values(["state", "report_date"])
    for col in FFILL_COLS:
        if col in df.columns:
            df[col] = df.groupby("state")[col].ffill()

    return df


def clean(df: pd.DataFrame, meta: pd.DataFrame) -> pd.DataFrame:
    """Función principal de limpieza."""
    # Unir metadata (población, lat, long)
    df = df.merge(meta, on="state", how="left")

    # Derivadas
    df = add_derived_columns(df)

    # Imputación
    df = fill_nulls(df)

    # Eliminar columnas sobrantes
    df.drop(columns=[c for c in DROP_COLS if c in df.columns], inplace=True)

    return df
