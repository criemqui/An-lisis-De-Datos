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

# Separar en dos DataFrames
df_dead = df.loc[df['is_dead'] == 1]
df_alive = df.loc[df['is_dead'] == 0]

# Mostrar las primeras filas de cada DataFrame
print("Personas que perecieron:")
print()
print(df_dead.head())
print("\nPersonas que no perecieron:")
print()
print(df_alive.head())

# Calcular los promedios de las edades
avg_age_dead = df_dead['age'].mean()
avg_age_alive = df_alive['age'].mean()

promedio_redondeado = round(avg_age_dead)
promedio_redondeado_alive = round(avg_age_alive)

# Imprimir los promedios
print("Promedio de edad de personas que perecieron:", promedio_redondeado, "Años")
print()

print("Promedio de edad de personas que no perecieron:", promedio_redondeado_alive, "Años")
print()
