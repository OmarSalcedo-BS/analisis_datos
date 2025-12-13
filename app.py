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

    df_datos = data_clean.cargar_datos()
    
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

    print("\n--- Ejemplos de Autores Limpiados (símbolos especiales eliminados) ---")
    autores_ejemplo = df_limpio[df_limpio['Fuente/Autor'].str.contains('einstein|camus|sócrates', case=False, na=False)]
    if not autores_ejemplo.empty:
        print(autores_ejemplo[['Fuente/Autor', 'Longitud_Caracteres', 'Texto']].head(10))
    else:
        print("No se encontraron los autores de ejemplo")
    print("-" * 120)
    
    print("\n--- Vista FINAL de Datos Limpios (Primeras 10 filas) ---")
    print(df_limpio[['Fuente/Autor', 'Sentimiento', 'Longitud_Caracteres']].head(10))
    print("-" * 120)


  
    
    print("--- Proceso de Limpieza Completado. ---")



if __name__ == "__main__":
    main()
