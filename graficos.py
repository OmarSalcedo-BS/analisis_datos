import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import data_clean


df = data_clean.cargar_datos()

df = data_clean.estandarizar_texto(df, 'Sentimiento')



def graficar_distribucion_sentimientos(df: pd.DataFrame):
    """
    Crea un gráfico de pastel con la distribución de sentimientos.
    
    Args:
        df: DataFrame con la columna 'Sentimiento'
    """
    # Contar sentimientos
    sentimientos_conteo = df['Sentimiento'].value_counts()
    print(f"\nDistribución de sentimientos:\n{sentimientos_conteo}")

    #Definir colores personalizados
    colores = {
        'positivo': '#2ecc71',      # Verde
        'negativo': '#e74c3c',      # Rojo
        'na': '#95a5a6'             # Gris
    }

    # Mapear colores a los sentimientos
    colores_lista = [colores.get(sentimiento, '#95a5a6') 
                for sentimiento in sentimientos_conteo.index]
    
    # Crear figura
    plt.figure(figsize=(9, 7))
    
    # Crear gráfico de pastel
    plt.pie(
        sentimientos_conteo.values,      # Números
        labels=sentimientos_conteo.index, # Etiquetas (positivo, negativo, etc)
        autopct='%1.1f%%',               # Mostrar porcentaje
        colors=colores_lista,            # Colores personalizados
        startangle=90,                   # Ángulo inicial
        shadow=True                      # Sombra para efecto 3D
    )

    plt.title('Distribución de Sentimientos en Frases y Versículos', 
            fontsize=14, 
            fontweight='bold',
            pad=20)
    
    plt.tight_layout()
    plt.savefig('distribucion_sentimientos.png', dpi=300, bbox_inches='tight')
    print("✓ Gráfico guardado en: distribucion_sentimientos.png")
    plt.show()
    
    return sentimientos_conteo
