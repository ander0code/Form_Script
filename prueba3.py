import random
import pandas as pd
from scipy.stats import pearsonr

# Definición de los datos del formulario con probabilidades
form_data_with_probabilities = {
    'entry.1310967310': {
        "options": ["Nunca", "Casi Nunca", "A veces", "Casi siempre", "Siempre"],
        "probabilities": [1.0, 2.0, 7.0, 8.0, 2.0]  # Ajuste para mayor diversidad
    },
    'entry.561300341': {
        "options": ["Nunca", "Casi Nunca", "A veces", "Casi siempre", "Siempre"],
        "probabilities": [1.0, 2.0, 7.0, 8.0, 2.0]
    },
    'entry.80773409': {
        "options": ["Nunca", "Casi Nunca", "A veces", "Casi siempre", "Siempre"],
        "probabilities": [1.0, 2.0, 7.0, 8.0, 2.0]
    },
    'entry.1013739680': {
        "options": ["Nunca", "Casi Nunca", "A veces", "Casi siempre", "Siempre"],
        "probabilities": [1.0, 2.0, 7.0, 8.0, 2.0]
    },
    'entry.1426771551': {
        "options": ["Nunca", "Casi Nunca", "A veces", "Casi siempre", "Siempre"],
        "probabilities": [1.0, 2.0, 7.0, 8.0, 2.0]
    },
    'entry.1969491809': {
        "options": ["Nunca", "Casi Nunca", "A veces", "Casi siempre", "Siempre"],
        "probabilities": [1.0, 2.0, 7.0, 8.0, 2.0]
    },
    'entry.584749565': {
        "options": ["Nunca", "Casi Nunca", "A veces", "Casi siempre", "Siempre"],
        "probabilities": [1.0, 2.0, 7.0, 8.0, 2.0]
    },
    'entry.2108393907': {
        "options": ["Nunca", "Casi Nunca", "A veces", "Casi siempre", "Siempre"],
        "probabilities": [1.0, 2.0, 7.0, 8.0, 2.0]
    },
    'entry.1386204740': {
        "options": ["Nunca", "Casi Nunca", "A veces", "Casi siempre", "Siempre"],
        "probabilities": [1.0, 2.0, 7.0, 8.0, 2.0]
    },
    'entry.341092859': {
        "options": ["Nunca", "Casi Nunca", "A veces", "Casi siempre", "Siempre"],
        "probabilities": [1.0, 2.0, 7.0, 8.0, 2.0]
    },
    'entry.1234507436': {
        "options": ["Nunca", "Casi Nunca", "A veces", "Casi siempre", "Siempre"],
        "probabilities": [1.0, 2.0, 7.0, 8.0, 2.0]
    },
    'entry.1598203705': {
        "options": ["Nunca", "Casi Nunca", "A veces", "Casi siempre", "Siempre"],
        "probabilities": [1.0, 2.0, 7.0, 8.0, 2.0]
    },
    'entry.615945012': {
        "options": ["Nunca", "Casi Nunca", "A veces", "Casi siempre", "Siempre"],
        "probabilities": [1.0, 2.0, 7.0, 8.0, 2.0]
    },
    'entry.1483905554': {
        "options": ["Nunca", "Casi Nunca", "A veces", "Casi siempre", "Siempre"],
        "probabilities": [1.0, 2.0, 7.0, 8.0, 2.0]
    },
    'entry.1541804207': {
        "options": ["Nunca", "Casi Nunca", "A veces", "Casi siempre", "Siempre"],
        "probabilities": [1.0, 2.0, 7.0, 8.0, 2.0]
    },
    'entry.1830185929': {
        "options": ["Nunca", "Casi Nunca", "A veces", "Casi siempre", "Siempre"],
        "probabilities": [1.0, 2.0, 7.0, 8.0, 2.0]
    },
    'entry.766635446': {
        "options": ["Nunca", "Casi Nunca", "A veces", "Casi siempre", "Siempre"],
        "probabilities": [1.0, 2.0, 7.0, 8.0, 2.0]
    },
    'entry.1984337518': {
        "options": ["Nunca", "Casi Nunca", "A veces", "Casi siempre", "Siempre"],
        "probabilities": [1.0, 2.0, 7.0, 8.0, 2.0]
    },
    'entry.1736372311': {
        "options": ["Nunca", "Casi Nunca", "A veces", "Casi siempre", "Siempre"],
        "probabilities": [1.0, 2.0, 7.0, 8.0, 2.0]
    },
    'entry.946313984': {
        "options": ["Nunca", "Casi Nunca", "A veces", "Casi siempre", "Siempre"],
        "probabilities": [1.0, 2.0, 7.0, 8.0, 2.0]
    },
}

# Función para normalizar los porcentajes a probabilidades para random.choices
def normalize_probabilities(prob_list):
    total = sum(prob_list)
    return [value / total for value in prob_list]

# Generar respuestas hasta obtener un Alfa de Cronbach alto
num_responses = 200
alpha = 0  # Inicializar el alfa
responses = {key: [] for key in form_data_with_probabilities.keys()}

while alpha < 0.7:  # Buscamos un alfa mayor o igual a 0.7
    responses = {key: [] for key in form_data_with_probabilities.keys()}
    
    for _ in range(num_responses):
        random_response = {
            key: random.choices(
                values["options"],
                weights=normalize_probabilities(values["probabilities"])
            )[0] for key, values in form_data_with_probabilities.items()
        }
        for key, value in random_response.items():
            responses[key].append(value)

    # Convertir las respuestas a un DataFrame de pandas
    df_responses = pd.DataFrame(responses)

    # Convertir respuestas categóricas a valores numéricos para el cálculo de Alfa de Cronbach
    mapping = {"Nunca": 1, "Casi Nunca": 2, "A veces": 3, "Casi siempre": 4, "Siempre": 5}
    df_numeric = df_responses.replace(mapping)

    # Función para calcular el Alfa de Cronbach
    def cronbach_alpha(df):
        # Número de items
        items = df.shape[1]
        # Varianza total
        total_var = df.var(axis=0).sum()
        # Varianza total de las puntuaciones
        total_score_var = df.sum(axis=1).var()
        # Calcular alfa
        return (items / (items - 1)) * (1 - (total_var / total_score_var))

    # Calcular el Alfa de Cronbach para las respuestas generadas
    alpha = cronbach_alpha(df_numeric)

# Guardar las respuestas en un archivo Excel
output_file = "/mnt/data/respuestas_formulario_alto_alpha.xlsx"
df_responses.to_excel(output_file, index=False)

alpha, output_file