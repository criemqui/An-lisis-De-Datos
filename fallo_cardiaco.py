import numpy as np
from datasets import load_dataset

# Cargar el conjunto de datos "mstz/heart_failure"
dataset = load_dataset("mstz/heart_failure")

# Acceder a la partición 'train'
data = dataset["train"]

# Obtener la lista de edades de data
edades = data["age"]

print(edades)

# Lista de edades

# Convertir la lista de edades a un arreglo de NumPy
edades_np = np.array(edades)

#print(edades_np)

# Calcular el promedio de edades
promedio_edades = np.mean(edades_np)

#print(promedio_edades)

# Redondear el promedio de edades
promedio_edades_redondeado = round(promedio_edades)
print()
print("El promedio de edades es:", promedio_edades_redondeado, "años")