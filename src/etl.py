# src/etl.py
import pandas as pd
from tqdm import tqdm
from src.config import RAW_DATA_PATH, OUTPUT_PATH, META_PATH
from src.clean import clean  

# ----------------- ETL -----------------
def extract() -> pd.DataFrame:
    frames = []
    for file in tqdm(sorted(RAW_DATA_PATH.glob("*.csv"))):
        date = pd.to_datetime(file.stem, format="%m-%d-%Y")
        df = pd.read_csv(file).assign(report_date=date)
        frames.append(df)
    return pd.concat(frames, ignore_index=True)


def transform(df: pd.DataFrame) -> pd.DataFrame:
    df = df.rename(
        columns={
            "Province_State": "state",
            "Confirmed": "confirmed",
            "Deaths": "deaths",
            "Recovered": "recovered",
            "Active": "active",
        }
    )

    num_cols = ["confirmed", "deaths", "recovered", "active"]
    df[num_cols] = df[num_cols].fillna(0).astype("int64")

    df = df.sort_values(["state", "report_date"])
    df["new_cases"]  = df.groupby("state")["confirmed"].diff().clip(lower=0)
    df["new_deaths"] = df.groupby("state")["deaths"].diff().clip(lower=0)
    return df


def load(df: pd.DataFrame) -> None:
    df.to_parquet(OUTPUT_PATH, compression="snappy")
    print(f"✅ Guardado: {OUTPUT_PATH.absolute()}")


# ----------------- CLI -----------------
if __name__ == "__main__":
    raw = extract()
    tidy = transform(raw)

    meta = pd.read_csv(META_PATH)      # aquí usamos el archivo CSV
    final_df = clean(tidy, meta)       # llamamos a la funcion de limpieza usando el módulo

    load(final_df)

