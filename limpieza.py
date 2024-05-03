import pandas as pd
from datasets import load_dataset

# Define la función que categoriza las edades
def categorizar_edades(edad):
    if edad <= 12:
        return 'Niño'
    elif 13 <= edad <= 19:
        return 'Adolescente'
    elif 20 <= edad <= 39:
        return 'Jóven adulto'
    elif 40 <= edad <= 59:
        return 'Adulto'
    else:
        return 'Adulto mayor'

# Cargar el conjunto de datos "mstz/heart_failure"
dataset = load_dataset("mstz/heart_failure")

# Acceder a la partición 'train'
data = dataset["train"]

# Convertir la partición 'train' a un DataFrame de pandas
df = pd.DataFrame(data)

# Verificar si existen valores faltantes
missing_values = df.isnull().sum().sum()

if missing_values == 0:
    print("No hay valores faltantes en el conjunto de datos.")
else:
    print(f"Se encontraron {missing_values} valores faltantes en el conjunto de datos.")

# Verificar filas duplicadas
duplicated_rows = df[df.duplicated()]

if duplicated_rows.empty:
    print("No hay filas duplicadas en el conjunto de datos.")
else:
    print("Se encontraron filas duplicadas en el conjunto de datos:")
    print(duplicated_rows)
    print()

def clean_and_categorize_data(dataframe):
    Q1 = dataframe['age'].quantile(0.25)
    Q3 = dataframe['age'].quantile(0.75)
    IQR = Q3 - Q1

    lower_limit = Q1 - 1.5 * IQR
    upper_limit = Q3 + 1.5 * IQR

    outliers = dataframe[(dataframe['age'] < lower_limit) | (dataframe['age'] > upper_limit)]

    df_cleaned = dataframe[(dataframe['age'] >= lower_limit) & (dataframe['age'] <= upper_limit)]
    df_cleaned['categoria_edad'] = df_cleaned['age'].apply(categorizar_edades)

    return df_cleaned

# Cargar el conjunto de datos "mstz/heart_failure"
dataset = load_dataset("mstz/heart_failure")

# Acceder a la partición 'train'
data = dataset["train"]

# Convertir la partición 'train' a un DataFrame de pandas
df = pd.DataFrame(data)

# Llamar a la función para limpiar y categorizar los datos
df_processed = clean_and_categorize_data(df)

# Guardar el DataFrame procesado con las edades categorizadas como un archivo CSV
df_processed.to_csv('categorias.csv', index=False)

# Verificar el DataFrame procesado con las edades categorizadas
print(df_processed)

# Función que encapsula toda la lógica anterior y recibe un DataFrame como entrada
def process_dataframe(input_dataframe):
    df = pd.DataFrame(input_dataframe)
    df_processed = clean_and_categorize_data(df)
    return df_processed