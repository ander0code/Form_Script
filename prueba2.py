import pandas as pd
import random

# Definición de las opciones y las probabilidades ajustadas para obtener un alto alfa de Cronbach
form_data_with_probabilities = {
    'entry.1310967310': {
        "options": ["Nunca", "Casi Nunca", "A veces", "Casi siempre", "Siempre"],
        "probabilities": [2.0, 5.0, 7.0, 5.0, 2.0]  # Probabilidades ajustadas
    },
    'entry.561300341': {
        "options": ["Nunca", "Casi Nunca", "A veces", "Casi siempre", "Siempre"],
        "probabilities": [2.0, 5.0, 7.0, 5.0, 2.0]
    },
    'entry.80773409': {
        "options": ["Nunca", "Casi Nunca", "A veces", "Casi siempre", "Siempre"],
        "probabilities": [2.0, 5.0, 7.0, 5.0, 2.0]
    },
    'entry.1013739680': {
        "options": ["Nunca", "Casi Nunca", "A veces", "Casi siempre", "Siempre"],
        "probabilities": [2.0, 5.0, 7.0, 5.0, 2.0]
    },
    'entry.1426771551': {
        "options": ["Nunca", "Casi Nunca", "A veces", "Casi siempre", "Siempre"],
        "probabilities": [2.0, 5.0, 7.0, 5.0, 2.0]
    },
    'entry.1969491809': {
        "options": ["Nunca", "Casi Nunca", "A veces", "Casi siempre", "Siempre"],
        "probabilities": [2.0, 5.0, 7.0, 5.0, 2.0]
    },
    'entry.584749565': {
        "options": ["Nunca", "Casi Nunca", "A veces", "Casi siempre", "Siempre"],
        "probabilities": [2.0, 5.0, 7.0, 5.0, 2.0]
    },
    'entry.2108393907': {
        "options": ["Nunca", "Casi Nunca", "A veces", "Casi siempre", "Siempre"],
        "probabilities": [2.0, 5.0, 7.0, 5.0, 2.0]
    },
    'entry.1386204740': {
        "options": ["Nunca", "Casi Nunca", "A veces", "Casi siempre", "Siempre"],
        "probabilities": [2.0, 5.0, 7.0, 5.0, 2.0]
    },
    'entry.341092859': {
        "options": ["Nunca", "Casi Nunca", "A veces", "Casi siempre", "Siempre"],
        "probabilities": [2.0, 5.0, 7.0, 5.0, 2.0]
    },
    'entry.1234507436': {
        "options": ["Nunca", "Casi Nunca", "A veces", "Casi siempre", "Siempre"],
        "probabilities": [2.0, 5.0, 7.0, 5.0, 2.0]
    },
    'entry.1598203705': {
        "options": ["Nunca", "Casi Nunca", "A veces", "Casi siempre", "Siempre"],
        "probabilities": [2.0, 5.0, 7.0, 5.0, 2.0]
    },
    'entry.615945012': {
        "options": ["Nunca", "Casi Nunca", "A veces", "Casi siempre", "Siempre"],
        "probabilities": [2.0, 5.0, 7.0, 5.0, 2.0]
    },
    'entry.1483905554': {
        "options": ["Nunca", "Casi Nunca", "A veces", "Casi siempre", "Siempre"],
        "probabilities": [2.0, 5.0, 7.0, 5.0, 2.0]
    },
    'entry.1541804207': {
        "options": ["Nunca", "Casi Nunca", "A veces", "Casi siempre", "Siempre"],
        "probabilities": [2.0, 5.0, 7.0, 5.0, 2.0]
    },
    'entry.1830185929': {
        "options": ["Nunca", "Casi Nunca", "A veces", "Casi siempre", "Siempre"],
        "probabilities": [2.0, 5.0, 7.0, 5.0, 2.0]
    },
    'entry.766635446': {
        "options": ["Nunca", "Casi Nunca", "A veces", "Casi siempre", "Siempre"],
        "probabilities": [2.0, 5.0, 7.0, 5.0, 2.0]
    },
    'entry.1984337518': {
        "options": ["Nunca", "Casi Nunca", "A veces", "Casi siempre", "Siempre"],
        "probabilities": [2.0, 5.0, 7.0, 5.0, 2.0]
    },
    'entry.1736372311': {
        "options": ["Nunca", "Casi Nunca", "A veces", "Casi siempre", "Siempre"],
        "probabilities": [2.0, 5.0, 7.0, 5.0, 2.0]
    },
    'entry.946313984': {
        "options": ["Nunca", "Casi Nunca", "A veces", "Casi siempre", "Siempre"],
        "probabilities": [2.0, 5.0, 7.0, 5.0, 2.0]
    },
}

# Normalizar las probabilidades
def normalize_probabilities(prob_list):
    total = sum(prob_list)
    return [value / total for value in prob_list]

# Generar datos simulados para el formulario
num_responses = 100  # Número total de respuestas simuladas
data = {
    "Response ID": [],
}

# Agregar entradas para cada pregunta
for entry in form_data_with_probabilities.keys():
    data[entry] = []

# Generar las respuestas
for i in range(num_responses):
    response_id = f"Response {i + 1}"
    data["Response ID"].append(response_id)
    for key, values in form_data_with_probabilities.items():
        response = random.choices(
            values["options"],
            weights=normalize_probabilities(values["probabilities"])
        )[0]
        data[key].append(response)

# Crear el DataFrame
df = pd.DataFrame(data)

# Guardar el DataFrame en un archivo Excel
excel_file_path = 'C:/Users/AUTONOMA/Desktop/simulated_form_data.xlsx'
df.to_excel(excel_file_path, index=False)

excel_file_path
