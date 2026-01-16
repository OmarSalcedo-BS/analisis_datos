# 📚 GUÍA COMPLETA PARA DEFENSA DEL PROYECTO

## Analizador de Frases y Versículos (AF&V)

---

## 📋 ÍNDICE

1. [Resumen Ejecutivo del Proyecto](#resumen-ejecutivo)
2. [Arquitectura del Proyecto](#arquitectura)
3. [Entornos Virtuales en Python](#entornos-virtuales)
4. [Explicación Detallada de Funciones](#funciones-detalladas)
5. [Flujo de Ejecución del Programa](#flujo-ejecucion)
6. [Operaciones de Análisis de Datos](#operaciones-analisis)
7. [Conceptos Clave de Pandas](#conceptos-pandas)
8. [Puntos Clave para la Defensa](#puntos-defensa)

---

## 🎯 RESUMEN EJECUTIVO {#resumen-ejecutivo}

### ¿Qué hace este proyecto?

Este proyecto es un **sistema de análisis de datos** que procesa frases filosóficas y versículos bíblicos. El programa:

- Carga datos desde archivos CSV
- Limpia y estandariza la información
- Realiza análisis estadísticos
- Combina múltiples fuentes de datos
- Genera reportes con insights significativos

### Objetivo del Proyecto

Demostrar competencias en:

- ✅ Manipulación de datos con **Pandas**
- ✅ Creación de módulos reutilizables en Python
- ✅ Limpieza y preparación de datos (Data Cleaning)
- ✅ Operaciones avanzadas: `groupby`, `merge`, `filter`
- ✅ Uso de entornos virtuales
- ✅ Control de versiones con Git

---

## 🏗️ ARQUITECTURA DEL PROYECTO {#arquitectura}

### Estructura de Archivos

```
analisis_datos/
│
├── .venv/                          # Entorno virtual (aislamiento de dependencias)
├── .git/                           # Control de versiones
├── datos/
│   ├── datos.csv                   # Dataset principal (frases y versículos)
│   └── autores_clasificacion.csv   # Dataset secundario (clasificación de autores)
│
├── app.py                          # Script principal (orquestador)
├── data_clean.py                   # Módulo de limpieza (funciones reutilizables)
├── requeriments.txt                # Dependencias del proyecto
└── .gitignore                      # Archivos excluidos de Git
```

### Separación de Responsabilidades

| Archivo                     | Responsabilidad                                 | Tipo                |
| --------------------------- | ----------------------------------------------- | ------------------- |
| `app.py`                    | Orquestación del flujo, análisis y presentación | Script principal    |
| `data_clean.py`             | Funciones de limpieza y carga de datos          | Módulo reutilizable |
| `datos.csv`                 | Datos principales a analizar                    | Dataset             |
| `autores_clasificacion.csv` | Datos complementarios para enriquecer análisis  | Dataset secundario  |

---

## 🔧 ENTORNOS VIRTUALES EN PYTHON {#entornos-virtuales}

### ¿Qué es un Entorno Virtual?

Un **entorno virtual** (virtual environment) es un **espacio aislado** donde puedes instalar paquetes de Python específicos para un proyecto sin afectar el sistema global.

### ¿Por qué usar Entornos Virtuales?

#### 1. **Aislamiento de Dependencias**

```
Sistema Global          vs.        Entorno Virtual (.venv)
├── Python 3.11                    ├── Python 3.11
├── pandas 1.5.0                   ├── pandas 2.3.3  ← Versión específica
├── numpy 1.20.0                   ├── numpy 2.3.5   ← Sin conflictos
└── (muchos otros...)              └── (solo lo necesario)
```

**Ventaja**: Cada proyecto tiene sus propias versiones de librerías sin conflictos.

#### 2. **Reproducibilidad**

Con `requeriments.txt` cualquier persona puede recrear el mismo entorno:

```bash
pip install -r requeriments.txt
```

#### 3. **Portabilidad**

El proyecto funciona igual en cualquier computadora que tenga Python.

### Comandos Esenciales

#### Crear un entorno virtual:

```bash
python -m venv .venv
```

- `python -m venv`: Módulo de Python para crear entornos virtuales
- `.venv`: Nombre del directorio (convención estándar)

#### Activar el entorno virtual:

**Windows (PowerShell):**

```powershell
.venv\Scripts\Activate.ps1
```

**Windows (CMD):**

```cmd
.venv\Scripts\activate.bat
```

**Linux/Mac:**

```bash
source .venv/bin/activate
```

#### Desactivar:

```bash
deactivate
```

#### Instalar dependencias:

```bash
pip install pandas numpy
```

#### Guardar dependencias:

```bash
pip freeze > requeriments.txt
```

### Contenido de `requeriments.txt`

```
numpy==2.3.5                    # Biblioteca para cálculos numéricos
pandas==2.3.3                   # Biblioteca para análisis de datos
python-dateutil==2.9.0.post0    # Manejo de fechas (dependencia de pandas)
pytz==2025.2                    # Zonas horarias (dependencia de pandas)
six==1.17.0                     # Compatibilidad Python 2/3 (dependencia)
tzdata==2025.2                  # Datos de zonas horarias
```

**Nota**: Solo instalaste `pandas`, pero `pip freeze` muestra todas las dependencias transitivas.

---

## 🔍 EXPLICACIÓN DETALLADA DE FUNCIONES {#funciones-detalladas}

---

## 📄 ARCHIVO: `data_clean.py`

Este módulo contiene **funciones reutilizables** para cargar y limpiar datos.

---

### 1️⃣ `cargar_datos()` → pd.DataFrame

**Propósito**: Cargar el dataset principal desde un archivo CSV.

```python
def cargar_datos() -> pd.DataFrame:
    try:
        df = pd.read_csv(RUTA_ARCHIVO, on_bad_lines='skip')
        print(f"Datos cargados correctamente desde: {RUTA_ARCHIVO}")
        return df
    except FileNotFoundError:
        print(f"Error: No se encontró el archivo: {RUTA_ARCHIVO}")
        return pd.DataFrame()
```

#### Conceptos Clave:

| Concepto              | Explicación                                                              |
| --------------------- | ------------------------------------------------------------------------ |
| `pd.read_csv()`       | Función de Pandas que lee archivos CSV y los convierte en DataFrame      |
| `on_bad_lines='skip'` | Si hay líneas malformadas en el CSV, las salta en lugar de generar error |
| `try-except`          | Manejo de errores: si el archivo no existe, captura la excepción         |
| `FileNotFoundError`   | Excepción específica cuando un archivo no se encuentra                   |
| `pd.DataFrame()`      | Retorna un DataFrame vacío si hay error (evita que el programa falle)    |
| `-> pd.DataFrame`     | Type hint: indica que la función retorna un DataFrame                    |

#### ¿Qué hace paso a paso?

1. Intenta leer el archivo CSV ubicado en `datos/datos.csv`
2. Si tiene líneas con formato incorrecto, las ignora
3. Si el archivo existe, retorna un DataFrame con los datos
4. Si el archivo NO existe, imprime un mensaje de error y retorna un DataFrame vacío

---

### 2️⃣ `cargar_datos_secundarios()` → pd.DataFrame

**Propósito**: Cargar el dataset secundario de clasificación de autores.

```python
def cargar_datos_secundarios() -> pd.DataFrame:
    try:
        df = pd.read_csv(RUTA_AUTORES)

        df['Nombre_Autor'] = df['Nombre_Autor'].str.lower().str.strip()
        df['Clasificacion'] = df['Clasificacion'].str.lower().str.strip()
        print(f"Datos secundarios cargados correctamente desde: {RUTA_AUTORES}")
        return df
    except FileNotFoundError:
        print(f"Error: No se encontró el archivo: {RUTA_AUTORES}")
        return pd.DataFrame()
```

#### Conceptos Clave:

| Operación      | Explicación                            | Ejemplo                    |
| -------------- | -------------------------------------- | -------------------------- |
| `.str.lower()` | Convierte texto a minúsculas           | "SÓCRATES" → "sócrates"    |
| `.str.strip()` | Elimina espacios al inicio y final     | " Buda " → "Buda"          |
| Encadenamiento | Aplicar múltiples operaciones seguidas | `.str.lower().str.strip()` |

#### ¿Por qué limpiar aquí?

**Razón**: Para facilitar el `merge` posterior. Si un autor aparece como "Albert Einstein" en un archivo y "albert einstein" en otro, el merge NO los reconocerá como iguales. Al estandarizar todo a minúsculas, aseguramos coincidencias.

---

### 3️⃣ `manejar_nulos(df)` → pd.DataFrame

**Propósito**: Gestionar valores faltantes (NaN) en el DataFrame.

```python
def manejar_nulos(df: pd.DataFrame) -> pd.DataFrame:
    df_procesado = df.copy()
    print("\nManejo de valores nulos:")

    filas_iniciales = len(df_procesado)
    df_procesado.dropna(subset=['Texto', 'Sentimiento'], inplace=True)
    eliminadas = filas_iniciales - len(df_procesado)
    print(f"Filas eliminadas: {eliminadas} filas")

    df_procesado['Sentimiento'].fillna('No clasificado', inplace=True)
    df_procesado['Longitud_Caracteres'].fillna(0, inplace=True)
    df_procesado['Fuente/Autor'].fillna('No clasificado', inplace=True)

    print(f"Total de filas: {len(df_procesado)}")
    return df_procesado
```

#### Conceptos Clave:

| Método                    | Acción                             | Cuándo usar                             |
| ------------------------- | ---------------------------------- | --------------------------------------- |
| `.copy()`                 | Crea una copia del DataFrame       | Para no modificar el original           |
| `.dropna()`               | Elimina filas con valores nulos    | Cuando los datos son críticos           |
| `subset=['col1', 'col2']` | Especifica columnas a verificar    | Solo elimina si esas columnas son nulas |
| `inplace=True`            | Modifica el DataFrame directamente | Evita crear copias adicionales          |
| `.fillna(valor)`          | Rellena valores nulos con un valor | Cuando quieres conservar la fila        |

#### Estrategia de Limpieza:

**1. Eliminación Estricta** (columnas críticas):

```python
df_procesado.dropna(subset=['Texto', 'Sentimiento'], inplace=True)
```

- Si `Texto` o `Sentimiento` están vacíos → **ELIMINAR** la fila
- **Razón**: Sin texto no hay nada que analizar; sin sentimiento el análisis pierde sentido

**2. Relleno con Valores Predeterminados** (columnas opcionales):

```python
df_procesado['Fuente/Autor'].fillna('No clasificado', inplace=True)
```

- Si `Fuente/Autor` está vacío → **RELLENAR** con "No clasificado"
- **Razón**: Podemos conservar la frase aunque no sepamos el autor

---

### 4️⃣ `estandarizar_texto(df, columna)` → pd.DataFrame

**Propósito**: Normalizar texto para análisis consistente.

```python
def estandarizar_texto(df: pd.DataFrame, columna: str) -> pd.DataFrame:
    df_procesado = df.copy()
    print(f"\nEstandarizando la columna '{columna}'...")

    if df_procesado[columna].dtype == 'object':
        df_procesado[columna] = df_procesado[columna].str.lower()
        df_procesado[columna] = df_procesado[columna].str.strip()
        df_procesado[columna] = df_procesado[columna].str.replace(r'\s+', ' ', regex=True)
        print(f"Columna '{columna}' unificada a minúsculas")
    else:
        print(f"La columna '{columna}' no es de tipo texto")

    return df_procesado
```

#### Conceptos Clave:

| Operación                               | Explicación                    | Antes         | Después       |
| --------------------------------------- | ------------------------------ | ------------- | ------------- |
| `.dtype == 'object'`                    | Verifica que sea texto         | -             | -             |
| `.str.lower()`                          | Minúsculas                     | "FRASE"       | "frase"       |
| `.str.strip()`                          | Quita espacios extremos        | " frase "     | "frase"       |
| `.str.replace(r'\s+', ' ', regex=True)` | Múltiples espacios → 1 espacio | "frase larga" | "frase larga" |

#### ¿Por qué es importante?

```
Antes de estandarizar:
- "Frase"
- "FRASE"
- "frase"
→ Pandas los trata como 3 valores diferentes

Después de estandarizar:
- "frase"
- "frase"
- "frase"
→ Pandas los agrupa correctamente
```

---

### 5️⃣ `limpieza_especifica(df)` → pd.DataFrame

**Propósito**: Limpieza personalizada del proyecto (símbolos especiales y recálculo).

```python
def limpieza_especifica(df: pd.DataFrame) -> pd.DataFrame:
    df_procesado = df.copy()

    print("\n[LIMPIEZA ESPECÍFICA DE METADATOS]")

    df_procesado['Fuente/Autor'] = df_procesado['Fuente/Autor'].astype(str).str.replace(r'[$,!"]', '', regex=True)
    df_procesado['Fuente/Autor'] = df_procesado['Fuente/Autor'].str.strip()
    df_procesado['Fuente/Autor'] = df_procesado['Fuente/Autor'].str.lower()
    print("- Símbolos especiales eliminados en 'Fuente/Autor'.")

    df_procesado['Longitud_Caracteres'] = df_procesado['Texto'].astype(str).str.len()
    print("- Recalculada la 'Longitud_Caracteres'.")

    return df_procesado
```

#### Conceptos Clave:

| Operación      | Explicación                    | Ejemplo                         |
| -------------- | ------------------------------ | ------------------------------- |
| `.astype(str)` | Convierte a texto              | Asegura que sea string          |
| `r'[$,!"]'`    | Expresión regular              | Busca los caracteres $, ,, !, " |
| `regex=True`   | Habilita expresiones regulares | Permite patrones complejos      |
| `.str.len()`   | Calcula longitud del texto     | "Hola" → 4                      |

#### Ejemplo Práctico:

```
Antes: "$ Albert Einstein $$"
Después: "albert einstein"

Pasos:
1. .str.replace(r'[$,!"]', '', regex=True)  → "  Albert Einstein  "
2. .str.strip()                              → "Albert Einstein"
3. .str.lower()                              → "albert einstein"
```

---

## 📄 ARCHIVO: `app.py`

Este es el **script principal** que orquesta todo el flujo del programa.

---

### 6️⃣ `limpiar_consola()`

**Propósito**: Limpiar la pantalla de la consola para mejor presentación.

```python
def limpiar_consola():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')
```

#### Conceptos Clave:

| Concepto      | Explicación                               |
| ------------- | ----------------------------------------- |
| `os.name`     | Identifica el sistema operativo           |
| `'nt'`        | Código para Windows (NT = New Technology) |
| `os.system()` | Ejecuta comandos del sistema operativo    |
| `'cls'`       | Comando de Windows para limpiar consola   |
| `'clear'`     | Comando de Linux/Mac para limpiar consola |

---

### 7️⃣ `respuestas_preguntas_clave(df, df_autores)`

**Propósito**: Realizar análisis de datos usando operaciones avanzadas de Pandas.

```python
def respuestas_preguntas_clave(df: pd.DataFrame, df_autores: pd.DataFrame):
    print("\n" + "="*50)
    print("\n--- Respuestas a preguntas clave ---")
    print("="*50)

    # 1. AGRUPACIÓN (groupby)
    print("\nAgrupación por categoría:")
    longitud_promedio = df.groupby('Categoría')['Longitud_Caracteres'].mean().round(2)
    print("\nLongitud promedio por categoría:")
    print(longitud_promedio)

    # 2. FILTRADO
    df_frases_negativas = df[
        (df['Categoría'] == 'frase') &
        (df['Sentimiento'] == 'negativo')
    ]
    print("\nConteo de frases negativas:")
    print(df_frases_negativas['ID'].count())

    # 3. MERGE (combinación de DataFrames)
    df_merge = pd.merge(
        df,
        df_autores,
        left_on = 'Fuente/Autor',
        right_on = 'Nombre_Autor',
        how = 'left'
    )

    # 4. FILTRADO POST-MERGE
    conteo_clasicos = df_merge[df_merge['Clasificacion'] == 'clásico']['ID'].count()
    print(f"\nNúmero total de frases de autores Clásicos: {conteo_clasicos}")
```

#### Operación 1: GROUPBY (Agrupación)

**¿Qué hace?**
Agrupa datos por categoría y calcula el promedio de longitud.

```python
longitud_promedio = df.groupby('Categoría')['Longitud_Caracteres'].mean().round(2)
```

**Desglose**:

```python
df.groupby('Categoría')          # Agrupa por categoría (frase, versículo)
  ['Longitud_Caracteres']        # Selecciona la columna a analizar
  .mean()                        # Calcula el promedio
  .round(2)                      # Redondea a 2 decimales
```

**Resultado**:

```
Categoría
frase        58.33
versículo    47.67
```

**Interpretación**: Las frases tienen en promedio 58.33 caracteres, mientras que los versículos tienen 47.67.

---

#### Operación 2: FILTRADO (Filtering)

**¿Qué hace?**
Selecciona solo las filas que cumplen múltiples condiciones.

```python
df_frases_negativas = df[
    (df['Categoría'] == 'frase') &
    (df['Sentimiento'] == 'negativo')
]
```

**Conceptos**:

- `&`: Operador AND lógico (ambas condiciones deben cumplirse)
- `()`: Paréntesis obligatorios para cada condición
- `==`: Comparación de igualdad

**Ejemplo Visual**:

```
DataFrame Original:
ID | Categoría  | Sentimiento | Texto
1  | versículo  | positivo    | ...
2  | frase      | negativo    | "La vida es sufrimiento"  ✓
3  | frase      | positivo    | ...
4  | frase      | negativo    | "Casaté y te arrepentiras" ✓

Resultado (df_frases_negativas):
ID | Categoría  | Sentimiento | Texto
2  | frase      | negativo    | "La vida es sufrimiento"
4  | frase      | negativo    | "Casaté y te arrepentiras"
```

---

#### Operación 3: MERGE (Combinación de DataFrames)

**¿Qué hace?**
Combina dos DataFrames basándose en una columna común (como un JOIN en SQL).

```python
df_merge = pd.merge(
    df,                          # DataFrame izquierdo (principal)
    df_autores,                  # DataFrame derecho (secundario)
    left_on = 'Fuente/Autor',    # Columna del DataFrame izquierdo
    right_on = 'Nombre_Autor',   # Columna del DataFrame derecho
    how = 'left'                 # Tipo de merge
)
```

**Tipos de Merge**:

| Tipo    | Descripción                                      | Analogía                  |
| ------- | ------------------------------------------------ | ------------------------- |
| `left`  | Mantiene todas las filas del DataFrame izquierdo | "Prioridad al principal"  |
| `right` | Mantiene todas las filas del DataFrame derecho   | "Prioridad al secundario" |
| `inner` | Solo filas que coinciden en ambos                | "Solo coincidencias"      |
| `outer` | Todas las filas de ambos DataFrames              | "Todo incluido"           |

**Ejemplo Visual**:

```
DataFrame Principal (df):
Fuente/Autor      | Texto
albert einstein   | "Si tu intención..."
buda              | "No es más rico..."
sócrates          | "Una vida sin examen..."

DataFrame Secundario (df_autores):
Nombre_Autor      | Clasificacion
albert einstein   | moderno
buda              | clásico
sócrates          | clásico

Resultado (df_merge):
Fuente/Autor      | Texto                | Clasificacion
albert einstein   | "Si tu intención..." | moderno
buda              | "No es más rico..."  | clásico
sócrates          | "Una vida sin..."    | clásico
```

**¿Por qué `left`?**
Porque queremos conservar TODAS las frases, incluso si no tienen clasificación de autor.

---

### 8️⃣ `main()`

**Propósito**: Función principal que orquesta todo el flujo del programa.

```python
def main():
    limpiar_consola()
    print("--- Bienvenido al AF&V (Analizador de frases y versículos) ---")

    # 1. CARGA DE DATOS
    df_datos = data_clean.cargar_datos()
    df_autores = data_clean.cargar_datos_secundarios()

    if df_datos.empty or df_autores.empty:
        print("Finalizando ejecución debido a error de carga.")
        return

    # 2. LIMPIEZA DE DATOS
    df_limpio = data_clean.manejar_nulos(df_datos)
    df_limpio = data_clean.estandarizar_texto(df_limpio, 'Categoría')
    df_limpio = data_clean.estandarizar_texto(df_limpio, 'Sentimiento')
    df_limpio = data_clean.limpieza_especifica(df_limpio)

    # 3. ANÁLISIS
    respuestas_preguntas_clave(df_limpio, df_autores)
    print("\n--- Proceso de Análisis Completado ---")

if __name__ == "__main__":
    main()
```

#### Conceptos Clave:

| Concepto                     | Explicación                                                                   |
| ---------------------------- | ----------------------------------------------------------------------------- |
| `if __name__ == "__main__":` | Solo ejecuta `main()` si el script se ejecuta directamente (no si se importa) |
| `data_clean.funcion()`       | Llama funciones del módulo `data_clean`                                       |
| `.empty`                     | Propiedad que retorna `True` si el DataFrame está vacío                       |
| `return`                     | Sale de la función inmediatamente                                             |

---

## 🔄 FLUJO DE EJECUCIÓN DEL PROGRAMA {#flujo-ejecucion}

```
┌─────────────────────────────────────┐
│  1. INICIO DEL PROGRAMA             │
│     python app.py                   │
└──────────────┬──────────────────────┘
               │
               ▼
┌─────────────────────────────────────┐
│  2. CARGA DE DATOS                  │
│     ├─ cargar_datos()               │
│     │   → datos.csv                 │
│     └─ cargar_datos_secundarios()   │
│         → autores_clasificacion.csv │
└──────────────┬──────────────────────┘
               │
               ▼
┌─────────────────────────────────────┐
│  3. VALIDACIÓN                      │
│     ¿DataFrames vacíos?             │
│     ├─ Sí → Terminar programa       │
│     └─ No → Continuar               │
└──────────────┬──────────────────────┘
               │
               ▼
┌─────────────────────────────────────┐
│  4. LIMPIEZA DE DATOS               │
│     ├─ manejar_nulos()              │
│     ├─ estandarizar_texto()         │
│     │   ├─ Columna 'Categoría'      │
│     │   └─ Columna 'Sentimiento'    │
│     └─ limpieza_especifica()        │
└──────────────┬──────────────────────┘
               │
               ▼
┌─────────────────────────────────────┐
│  5. ANÁLISIS DE DATOS               │
│     ├─ GroupBy (agrupación)         │
│     ├─ Filter (filtrado)            │
│     ├─ Merge (combinación)          │
│     └─ Análisis post-merge          │
└──────────────┬──────────────────────┘
               │
               ▼
┌─────────────────────────────────────┐
│  6. PRESENTACIÓN DE RESULTADOS      │
│     └─ Impresión en consola         │
└──────────────┬──────────────────────┘
               │
               ▼
           [FIN]
```

---

## 📊 OPERACIONES DE ANÁLISIS DE DATOS {#operaciones-analisis}

### 1. GroupBy (Agrupación)

**Definición**: Divide los datos en grupos basados en una o más columnas y aplica una función de agregación.

**Sintaxis**:

```python
df.groupby('columna')['columna_a_analizar'].funcion_agregacion()
```

**Funciones de agregación comunes**:

- `.mean()`: Promedio
- `.sum()`: Suma
- `.count()`: Conteo
- `.min()`: Mínimo
- `.max()`: Máximo
- `.std()`: Desviación estándar

**Ejemplo del proyecto**:

```python
longitud_promedio = df.groupby('Categoría')['Longitud_Caracteres'].mean()
```

---

### 2. Filter (Filtrado)

**Definición**: Selecciona filas que cumplen condiciones específicas.

**Operadores**:

- `==`: Igual
- `!=`: Diferente
- `>`, `<`, `>=`, `<=`: Comparaciones numéricas
- `&`: AND (y)
- `|`: OR (o)
- `~`: NOT (no)

**Ejemplo del proyecto**:

```python
df_frases_negativas = df[
    (df['Categoría'] == 'frase') &
    (df['Sentimiento'] == 'negativo')
]
```

---

### 3. Merge (Combinación)

**Definición**: Combina dos DataFrames basándose en columnas comunes.

**Parámetros clave**:

- `left_on`: Columna del DataFrame izquierdo
- `right_on`: Columna del DataFrame derecho
- `how`: Tipo de merge (`left`, `right`, `inner`, `outer`)

**Ejemplo del proyecto**:

```python
df_merge = pd.merge(
    df,
    df_autores,
    left_on='Fuente/Autor',
    right_on='Nombre_Autor',
    how='left'
)
```

---

## 📚 CONCEPTOS CLAVE DE PANDAS {#conceptos-pandas}

### DataFrame

**Definición**: Estructura de datos bidimensional (como una tabla de Excel) con filas y columnas.

```python
   ID  Categoría    Sentimiento
0   1  versículo    positivo
1   2  frase        positivo
2   3  versículo    negativo
```

### Series

**Definición**: Estructura unidimensional (como una columna de Excel).

```python
0    versículo
1    frase
2    versículo
Name: Categoría, dtype: object
```

### Indexación

```python
df['Categoría']              # Selecciona una columna (Series)
df[['Categoría', 'Texto']]   # Selecciona múltiples columnas (DataFrame)
df.loc[0]                    # Selecciona fila por índice
df.iloc[0]                   # Selecciona fila por posición
```

### Métodos de String

```python
df['columna'].str.lower()     # Minúsculas
df['columna'].str.upper()     # Mayúsculas
df['columna'].str.strip()     # Quitar espacios
df['columna'].str.replace()   # Reemplazar texto
df['columna'].str.len()       # Longitud
```

---

## 🎓 PUNTOS CLAVE PARA LA DEFENSA {#puntos-defensa}

### 1. Arquitectura Modular

**Pregunta**: ¿Por qué separaste el código en dos archivos?

**Respuesta**:

> "Implementé una arquitectura modular separando `app.py` (orquestación) de `data_clean.py` (funciones reutilizables). Esto sigue el principio de **Separación de Responsabilidades** (Separation of Concerns), facilitando el mantenimiento, testing y reutilización del código. Si en el futuro necesito limpiar datos en otro proyecto, puedo importar `data_clean` sin modificaciones."

---

### 2. Manejo de Errores

**Pregunta**: ¿Qué pasa si el archivo CSV no existe?

**Respuesta**:

> "Implementé bloques `try-except` que capturan la excepción `FileNotFoundError`. En lugar de que el programa falle abruptamente, retorno un DataFrame vacío y muestro un mensaje descriptivo. En `main()`, verifico si los DataFrames están vacíos con `.empty` y termino la ejecución de forma controlada."

---

### 3. Limpieza de Datos

**Pregunta**: ¿Por qué es importante estandarizar el texto?

**Respuesta**:

> "La estandarización es crítica para análisis consistente. Sin ella, 'Frase', 'FRASE' y 'frase' se tratarían como valores diferentes, fragmentando los resultados del `groupby`. Al convertir todo a minúsculas y eliminar espacios extra, garantizo que el análisis agrupe correctamente los datos. Esto es especialmente importante para el `merge`, donde las coincidencias deben ser exactas."

---

### 4. Estrategia de Nulos

**Pregunta**: ¿Por qué eliminas algunas filas con nulos pero rellenas otras?

**Respuesta**:

> "Apliqué una estrategia diferenciada basada en la criticidad de los datos:
>
> - **Eliminación** (`dropna`): Para columnas críticas como 'Texto' y 'Sentimiento', porque sin ellas el análisis pierde sentido.
> - **Relleno** (`fillna`): Para columnas opcionales como 'Fuente/Autor', porque puedo conservar la frase aunque no sepa el autor, rellenando con 'No clasificado'.
>   Esta estrategia maximiza la cantidad de datos útiles sin comprometer la calidad del análisis."

---

### 5. Operaciones Avanzadas

**Pregunta**: Explica el merge que realizaste.

**Respuesta**:

> "Realicé un `left merge` entre el DataFrame principal (frases) y el secundario (clasificación de autores). Usé `left_on='Fuente/Autor'` y `right_on='Nombre_Autor'` para vincular ambos DataFrames. Elegí `how='left'` para conservar todas las frases, incluso si no tienen clasificación de autor. Esto me permitió enriquecer los datos originales con información adicional (clasificación clásico/moderno) sin perder registros."

---

### 6. Entornos Virtuales

**Pregunta**: ¿Para qué sirve el entorno virtual?

**Respuesta**:

> "El entorno virtual (`.venv`) crea un espacio aislado con versiones específicas de librerías. Esto evita conflictos con otros proyectos y asegura reproducibilidad. Cualquier persona puede recrear el mismo entorno ejecutando `pip install -r requeriments.txt`. Además, mantiene el sistema global limpio, instalando solo las dependencias necesarias para este proyecto."

---

### 7. Type Hints

**Pregunta**: ¿Qué significan las anotaciones `-> pd.DataFrame`?

**Respuesta**:

> "Son **type hints** (anotaciones de tipo) que documentan qué tipo de dato retorna la función. `-> pd.DataFrame` indica que la función retorna un DataFrame de Pandas. Aunque Python no las valida en tiempo de ejecución, mejoran la legibilidad del código y permiten que IDEs como VS Code ofrezcan mejor autocompletado y detección de errores."

---

### 8. Expresiones Regulares

**Pregunta**: ¿Qué hace `r'[$,!"]'` en el código?

**Respuesta**:

> "Es una **expresión regular** (regex) que define un patrón de búsqueda. Los corchetes `[]` indican 'cualquiera de estos caracteres'. En este caso, busca `$`, `,`, `!` o `"` y los elimina. El prefijo `r` indica una raw string, evitando que Python interprete caracteres especiales. Esto limpia símbolos no deseados en los nombres de autores."

---

### 9. Encadenamiento de Métodos

**Pregunta**: ¿Por qué usas `.str.lower().str.strip()`?

**Respuesta**:

> "Es **method chaining** (encadenamiento de métodos), una técnica que aplica múltiples transformaciones secuencialmente. Primero `.str.lower()` convierte a minúsculas, luego `.str.strip()` elimina espacios. Es más legible y eficiente que crear variables intermedias para cada paso."

---

### 10. Git y Control de Versiones

**Pregunta**: ¿Por qué usas `.gitignore`?

**Respuesta**:

> "El `.gitignore` excluye archivos que no deben versionarse, como:
>
> - `.venv/`: El entorno virtual (ocupa mucho espacio y es específico de cada máquina)
> - `__pycache__/`: Archivos compilados de Python (se regeneran automáticamente)
> - Archivos temporales del sistema
>
> Esto mantiene el repositorio limpio, reduce el tamaño y evita conflictos entre diferentes sistemas operativos."

---

## 📝 RESUMEN FINAL

### Lo que demuestra este proyecto:

✅ **Competencia en Pandas**: Uso de DataFrames, Series, operaciones de limpieza y análisis  
✅ **Programación Modular**: Separación de responsabilidades en módulos reutilizables  
✅ **Manejo de Errores**: Try-except para robustez  
✅ **Limpieza de Datos**: Estrategias diferenciadas para nulos, estandarización de texto  
✅ **Operaciones Avanzadas**: GroupBy, Filter, Merge  
✅ **Buenas Prácticas**: Type hints, documentación, entornos virtuales  
✅ **Control de Versiones**: Git, .gitignore  
✅ **Pensamiento Analítico**: Interpretación de resultados y generación de insights

---

## 🚀 COMANDOS PARA EJECUTAR EL PROYECTO

```bash
# 1. Activar entorno virtual
.venv\Scripts\Activate.ps1

# 2. Instalar dependencias (si es necesario)
pip install -r requeriments.txt

# 3. Ejecutar el programa
python app.py
```

---

**Fecha de creación**: 15 de enero de 2026  
**Proyecto**: Analizador de Frases y Versículos (AF&V)  
**Autor**: Omar Salcedo  
**Curso**: Backend - Momento 2

---

_Este documento fue creado para facilitar la defensa del proyecto y aclarar conceptos clave de Python, Pandas y análisis de datos._
