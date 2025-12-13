import pandas as pd


RUTA_ARCHIVO = "datos/datos.csv"

def cargar_datos(ruta: str) -> pd.DataFrame:
    try:
        df = pd.read_csv(
            ruta,
            encoding='utf-8',
            on_bad_lines='skip', 
            quotechar='"',
            escapechar='\\'
        )
        print(f"Datos cargados con éxito desde: {ruta} ")
        print(f"Total de filas: {len(df)}")
        return df
    except FileNotFoundError:
        print(f"Error: No se encontró el archivo: {ruta}")
        return pd.DataFrame()
    except pd.errors.ParserError as e:
        print(f"Error al parsear el archivo CSV: {e}")
        print("Intentando con configuración alternativa...")
        try:
            df = pd.read_csv(
                ruta,
                encoding='latin-1',
                on_bad_lines='skip',
                sep=',',
                engine='python'
            )
            print(f"Datos cargados con éxito (modo alternativo)")
            print(f"Total de filas: {len(df)}")
            return df
        except Exception as e2:
            print(f"Error crítico al cargar datos: {e2}")
            return pd.DataFrame()
    except Exception as e:
        print(f"Error inesperado: {e}")
        return pd.DataFrame()


