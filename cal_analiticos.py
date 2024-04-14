import pandas as pd
from datasets import load_dataset

# Cargar el conjunto de datos "mstz/heart_failure"
dataset = load_dataset("mstz/heart_failure")

# Acceder a la partición 'train'
data = dataset["train"]

# Convertir a DataFrame de Pandas
df = data.to_pandas()

# Mostrar las primeras filas del DataFrame
#print(df.head())


# Verificar los tipos de datos en cada columna
print("Tipos de datos en el DataFrame:")
print(df.dtypes)
print()

# Calcular la cantidad de hombres fumadores
hombres_fumadores = df[(df['is_male'] == 1) & (df['is_smoker'] == 1)].shape[0]

# Calcular la cantidad de mujeres fumadoras
mujeres_fumadoras = df[(df['is_male'] == 0) & (df['is_smoker'] == 1)].shape[0]

print("Cantidad de hombres fumadores:", hombres_fumadores)
print()
print("Cantidad de mujeres fumadoras:", mujeres_fumadoras)
print()