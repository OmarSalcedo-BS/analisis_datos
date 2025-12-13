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


def manejar_nulos(df: pd.DataFrame) -> pd.DataFrame:
    """
    Maneja los valores nulos en el DataFrame.
    """
    df_procesado = df.copy()
    print("\nManejo de valores nulos:")

    filas_iniciales = len(df_procesado)
    df_procesado.dropna(subset=['Texto', 'Sentimiento'], inplace=True)
    eliminadas = filas_iniciales - len(df_procesado)
    print(f"Filas eliminadas: {eliminadas} filas (datos criticos faltantes en el texto, sentimiento o autor)")

    df_procesado['Sentimiento'].fillna('No clasificado', inplace=True) # Rellena valores nulos en 'Sentimiento' con 'No clasificado'
    df_procesado['Longitud_Caracteres'].fillna(0, inplace=True) # Rellena valores nulos en 'Longitud_Caracteres' con 0
    df_procesado['Fuente/Autor'].fillna('No clasificado', inplace=True) # Rellena valores nulos en 'Fuente/Autor' con 'No clasificado'


    print("Se rellenó 'Sentimiento' con 'No clasificado' y 'Longitud_Caracteres' con 0")
    print("Se rellenó 'Fuente/Autor' con 'No clasificado'")
    print(f"Total de filas: {len(df_procesado)}")
    print("\nManejo de valores nulos completado")
    return df_procesado
    



def estandarizar_texto(df: pd.DataFrame, columna: str) -> pd.DataFrame:
    """
    Estandariza una columna de texto, convirtiendo a minúsculas y eliminando
    espacios extra
    """

    df_procesado = df.copy()
    print(f"\nEstandarizando la columna '{columna}'...")

    if df_procesado[columna].dtype != 'object':
        
        df_procesado[columna] = df_procesado[columna].str.lower()

        df_procesado[columna] = df_procesado[columna].str.strip()

        print(f"Columna '{columna}' unificada a minúsculas y espacios extra eliminados con éxito")
    else:
        print(f"La columna '{columna}' no es de tipo texto, no se puede estandarizar")    
    
    print("\nEstandarización completada")
    return df_procesado




def limpieza_especifica(df: pd.DataFrame) -> pd.DataFrame:
    """
    Función de limpieza específica (eliminar símbolos y recalcular longitud).
    """
    df_procesado = df.copy()
    
    print("\n[LIMPIEZA ESPECÍFICA DE METADATOS]")
    
    df_procesado['Fuente/Autor'] = df_procesado['Fuente/Autor'].astype(str).str.replace(r'[$,!"]', '', regex=True)
    df_procesado['Fuente/Autor'] = df_procesado['Fuente/Autor'].str.strip()
    print("- Símbolos especiales eliminados de la columna 'Fuente/Autor'.")
    
    df_procesado['Longitud_Caracteres'] = df_procesado['Texto'].astype(str).str.len()
    print("- Recalculada la 'Longitud_Caracteres' basándose en el texto limpio.")
    
    print("Limpieza específica completada.")
    
    return df_procesado 