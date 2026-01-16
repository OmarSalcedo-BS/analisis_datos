import os
import data_clean
import pandas as pd
import graficos

"""
Momento 2 -  Fecha límite jueves 15 de enero.
Construir una aplicación de análisis de datos en Python. El reto consiste en crear un módulo de funciones que pueda limpiar y preparar datos, y luego usar ese módulo en un script principal para responder preguntas clave sobre la información de su proyecto.

"""




def limpiar_consola():
    """
    Limpia la consola se considera una buena práctica por eso la estoy
    creando aquí como una adición de parte de mi curso de Platzi
    """
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')


def respuestas_preguntas_clave(df: pd.DataFrame, df_autores: pd.DataFrame):
    """
    El programa en su fase final debe 
    Realizar operaciones de filtrado, combinación (merge) y agrupación (groupby)
    Imprimir en la consola las respuestas
    """
    print("\n" + "="*50)
    print("\n--- Respuestas a preguntas clave ---")
    print("="*50)

    #Agrupacion por categoria
    print("\nAgrupación por categoría:")
    longitud_promedio = df.groupby('Categoría')['Longitud_Caracteres'].mean().round(2)
    print("\nLongitud promedio por categoría:")
    print(longitud_promedio)
    print(f"Interpretación: los 'versículos' tienen un promedio de {longitud_promedio['versículo']} caracteres")

    #Filtrado
    df_frases_negativas = df[
        (df['Categoría'] == 'frase') &
        (df['Sentimiento'] == 'negativo')
    ]
    print("\nConteo de frases negativas:")
    print(df_frases_negativas['ID'].count())
    print("\nFrases negativas:")
    print(df_frases_negativas[['Texto', 'Fuente/Autor']]
    if not df_frases_negativas.empty else "No se encontraron frases negativas.")


    #Merge
    df_merge = pd.merge(
        df,
        df_autores,
        left_on = 'Fuente/Autor',
        right_on = 'Nombre_Autor',
        how = 'left'
    )

    #Agruparemos para contar cuantos de los autores son 'clásico'
    conteo_clasicos = df_merge[df_merge['Clasificacion'] == 'clásico']['ID'].count()
    print("\nConteo de autores Clásicos:")
    print(conteo_clasicos)
    print(f"Número total de frases de autores Clásicos: {conteo_clasicos}")
    print("Se úso un left merge para vincular la clasificación de los autores con el DataFrame principal")

    # --- 4. FILTRADO POST-MERGE ---
    df_moderno = df_merge[df_merge['Clasificacion'] == 'moderno'][['Texto', 'Clasificacion']]
    print("\n4. Frases Clasificadas como Modernas:")
    print(df_moderno)
    
    print("="*50)

    graficos.graficar_distribucion_sentimientos(df)
    print("Gráfico de distribución de sentimientos generado y guardado.")
    





def main():
    limpiar_consola()
    print("--- Bienvenido al AF&V (Analizador de frases y versículos) ---")

    df_datos = data_clean.cargar_datos()
    df_autores = data_clean.cargar_datos_secundarios()
    
    if df_datos.empty or df_autores.empty:
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

    respuestas_preguntas_clave(df_limpio, df_autores)
    print("\n--- Proceso de Análisis Completado y respuestas a preguntas clave ---")



if __name__ == "__main__":
    main()
