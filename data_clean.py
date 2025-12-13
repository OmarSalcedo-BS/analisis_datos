import pandas as pd


RUTA_ARCHIVO = "datos/datos.csv"

def cargar_datos(ruta: str) -> pd.DataFrame:
    try:
        df = pd.read_csv(ruta)
        print(f"Datos cargados con éxito desde: {ruta} ")
        return df
    except FileNotFoundError:
        print(f"Error al cargar los datos del archivo: {ruta}")
        return pd.DataFrame()


