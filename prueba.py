import requests
import random
import threading

# URL del formulario de Google
GoogleURL = "https://docs.google.com/forms/d/e/1FAIpQLSegKd5kTcMZ02LJ_VxajDH-lhe541dnQLMxZWwJ4CcMj6kTiA"

urlResponse = GoogleURL + "/formResponse"
urlReferer = GoogleURL + "/viewform"

# Probabilidades específicas para cada pregunta en porcentaje
# Cada entrada tiene su propio diccionario de opciones y probabilidades
form_data_with_probabilities = {
    'entry.1310967310': {
        "options": ["Nunca", "Casi Nunca", "A veces", "Casi siempre", "Siempre"],
        "probabilities": [5.5, 2.5, 1.5, 0.5, 0.5]
    },
    'entry.561300341': {
        "options": ["Nunca", "Casi Nunca", "A veces", "Casi siempre", "Siempre"],
        "probabilities": [3.0, 3.0, 2.0, 1.0, 1.0]
    },
    'entry.80773409': {
        "options": ["Nunca", "Casi Nunca", "A veces", "Casi siempre", "Siempre"],
        "probabilities": [4.0, 3.0, 2.0, 0.8, 0.2]
    },
    'entry.1013739680': {
        "options": ["Nunca", "Casi Nunca", "A veces", "Casi siempre", "Siempre"],
        "probabilities": [2.5, 3.0, 3.5, 1.0, 0.5]
    },
    'entry.1426771551': {
        "options": ["Nunca", "Casi Nunca", "A veces", "Casi siempre", "Siempre"],
        "probabilities": [3.5, 2.5, 1.5, 1.0, 1.5]
    },
    'entry.1969491809': {
        "options": ["Nunca", "Casi Nunca", "A veces", "Casi siempre", "Siempre"],
        "probabilities": [2.0, 2.0, 2.0, 2.0, 2.0]
    },
    'entry.584749565': {
        "options": ["Nunca", "Casi Nunca", "A veces", "Casi siempre", "Siempre"],
        "probabilities": [1.0, 2.5, 3.0, 2.5, 1.0]
    },
    'entry.2108393907': {
        "options": ["Nunca", "Casi Nunca", "A veces", "Casi siempre", "Siempre"],
        "probabilities": [4.0, 1.5, 2.5, 1.0, 1.0]
    },
    'entry.1386204740': {
        "options": ["Nunca", "Casi Nunca", "A veces", "Casi siempre", "Siempre"],
        "probabilities": [1.5, 2.0, 2.5, 2.0, 2.0]
    },
    'entry.341092859': {
        "options": ["Nunca", "Casi Nunca", "A veces", "Casi siempre", "Siempre"],
        "probabilities": [2.0, 2.5, 3.0, 1.0, 1.5]
    },
    'entry.1234507436': {
        "options": ["Nunca", "Casi Nunca", "A veces", "Casi siempre", "Siempre"],
        "probabilities": [2.0, 3.0, 2.0, 1.5, 1.5]
    },
    'entry.1598203705': {
        "options": ["Nunca", "Casi Nunca", "A veces", "Casi siempre", "Siempre"],
        "probabilities": [3.0, 2.5, 1.5, 1.5, 1.5]
    },
    'entry.615945012': {
        "options": ["Nunca", "Casi Nunca", "A veces", "Casi siempre", "Siempre"],
        "probabilities": [1.0, 1.0, 3.0, 2.5, 2.5]
    },
    'entry.1483905554': {
        "options": ["Nunca", "Casi Nunca", "A veces", "Casi siempre", "Siempre"],
        "probabilities": [2.0, 1.5, 3.0, 2.5, 1.0]
    },
    'entry.1541804207': {
        "options": ["Nunca", "Casi Nunca", "A veces", "Casi siempre", "Siempre"],
        "probabilities": [2.5, 2.5, 2.0, 1.5, 1.5]
    },
    'entry.1830185929': {
        "options": ["Nunca", "Casi Nunca", "A veces", "Casi siempre", "Siempre"],
        "probabilities": [3.5, 2.5, 1.5, 1.0, 1.5]
    },
    'entry.766635446': {
        "options": ["Nunca", "Casi Nunca", "A veces", "Casi siempre", "Siempre"],
        "probabilities": [1.5, 2.0, 3.0, 1.5, 2.0]
    },
    'entry.1984337518': {
        "options": ["Nunca", "Casi Nunca", "A veces", "Casi siempre", "Siempre"],
        "probabilities": [3.5, 1.5, 2.0, 1.5, 1.5]
    },
    'entry.1736372311': {
        "options": ["Nunca", "Casi Nunca", "A veces", "Casi siempre", "Siempre"],
        "probabilities": [2.5, 3.5, 1.5, 1.0, 1.5]
    },
    'entry.946313984': {
        "options": ["Nunca", "Casi Nunca", "A veces", "Casi siempre", "Siempre"],
        "probabilities": [1.5, 1.5, 3.5, 2.0, 1.5]
    },
}

# Función para normalizar los porcentajes a probabilidades para random.choices
def normalize_probabilities(prob_list):
    total = sum(prob_list)
    return [value / total for value in prob_list]

# Número de hilos y repeticiones por hilo
num_threads = 5
chunks_per_thread = 10

# Contador global de envíos
count = 0
threads = []

def submit_form(chunks_per_thread):
    global count
    user_agent = {
        'Referer': urlReferer,
        'User-Agent': "Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/28.0.1500.52 Safari/537.36"
    }
    for _ in range(chunks_per_thread):
        # Para cada entrada, selecciona una respuesta basada en probabilidades específicas
        random_form_data = {
            key: random.choices(
                values["options"],
                weights=normalize_probabilities(values["probabilities"])
            )[0] for key, values in form_data_with_probabilities.items()
        }
        r = requests.post(urlResponse, data=random_form_data, headers=user_agent)
        count += 1
        print(f"Envío número: {count}, Status code: {r.status_code}")

# Crear y comenzar los hilos
for _ in range(num_threads):
    thread = threading.Thread(target=submit_form, args=(chunks_per_thread,))
    threads.append(thread)
    thread.start()

# Esperar a que todos los hilos terminen
for thread in threads:
    thread.join()

print("Todos los envíos completados.")