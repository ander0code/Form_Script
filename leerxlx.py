import pandas as pd
from scipy.stats import pearsonr

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

# Cargar el archivo Excel
file_path = 'C:\Users\AUTONOMA\Downloads\simulated_form_data1111.xlsx'  
df = pd.read_excel(file_path)

# Convertir respuestas categóricas a valores numéricos
mapping = {"Nunca": 1, "Casi Nunca": 2, "A veces": 3, "Casi siempre": 4, "Siempre": 5}
df_numeric = df.replace(mapping)

# Calcular el Alfa de Cronbach para las respuestas
alpha = cronbach_alpha(df_numeric)

print(f"Alfa de Cronbach: {alpha}")
