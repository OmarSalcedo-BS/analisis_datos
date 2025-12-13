import os
import data_clean

def limpiar_consola():
    """
    Limpia la consola se considera una buena práctica por eso la estoy
    creando aquí como una adición de parte de mi curso de Platzi
    """
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')


def main():
    limpiar_consola()
    print("--- Bienvenido al AF&V (Analizador de frases y versículos) ---")

    df_datos = data_clean.cargar_datos(data_clean.RUTA_ARCHIVO)
    
    if df_datos.empty:
        print("Finalizando ejecución debido a error de carga.")
        return
        
    print("\n--- Vista preliminar de los datos crudos ---")
    print(df_datos[['Categoría', 'Sentimiento', 'Fuente/Autor']].head())
    print("-" * 120)
    
    df_limpio = data_clean.manejar_nulos(df_datos)
    
    df_limpio = data_clean.estandarizar_texto(df_limpio, 'Categoría')
    df_limpio = data_clean.estandarizar_texto(df_limpio, 'Sentimiento')

    print("\n--- Vista después de Estandarización de Texto ---")
    print(df_limpio[['Categoría', 'Sentimiento', 'Fuente/Autor', 'Texto']].head())
    print("-" * 120)
    
    df_limpio = data_clean.limpieza_especifica(df_limpio)

    print("\n --- Vista de textos completo ---")
    print(df_limpio[['Texto']].tail())
    print("-" * 120)
    
    print("\n--- Vista FINAL de Datos Limpios (Listos para Análisis) ---")
    print(df_limpio[['Fuente/Autor', 'Longitud_Caracteres']].tail())
    print("-" * 120)


  
    
    print("--- Proceso de Limpieza Completado. ---")



if __name__ == "__main__":
    main()
