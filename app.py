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
        print("No se pudo cargar los datos. Por favor, verifica la ruta del archivo.")
        return
    print("\nDatos cargados correctamente:\n")
    print(df_datos.head()) 
    print("-" * 50)



if __name__ == "__main__":
    main()
