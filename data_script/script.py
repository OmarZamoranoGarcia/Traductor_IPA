import nltk
import eng_to_ipa as ipa
import pandas as pd
import random

# 1. Descargar el corpus de palabras en inglés (solo se hace la primera vez)
print("Descargando diccionario de palabras...")
nltk.download('words', quiet=True)
from nltk.corpus import words

def generar_dataset_ipa(cantidad_objetivo=10000):
    # 2. Obtener la lista masiva de palabras en inglés
    lista_completa = words.words()
    
    # Limpieza básica: convertimos todo a minúsculas y quitamos duplicados
    palabras_limpias = list(set([palabra.lower() for palabra in lista_completa if palabra.isalpha()]))
    
    # Revolvemos la lista aleatoriamente para tener variedad de palabras
    random.seed(42) # Usamos una semilla para que el resultado sea reproducible
    random.shuffle(palabras_limpias)
    
    dataset = []
    
    print(f"Iniciando la extracción de {cantidad_objetivo} palabras a IPA...")
    
    # 3. Iterar sobre las palabras y extraer su IPA
    for palabra in palabras_limpias:
        # Si ya llegamos a la meta, detenemos el ciclo
        if len(dataset) >= cantidad_objetivo:
            break
            
        # La librería eng_to_ipa hace la conversión
        transcripcion_ipa = ipa.convert(palabra)
        
        # OJO: eng_to_ipa devuelve la palabra con un asterisco (ej. 'palabra*') 
        # si NO la encuentra en su diccionario. Filtramos para guardar solo las exitosas.
        if not transcripcion_ipa.endswith('*'):
            dataset.append({
                'Termino_Ingles': palabra,
                'Transcripcion_IPA': transcripcion_ipa
            })
            
        # Un pequeño indicador de progreso
        if len(dataset) % 1000 == 0 and len(dataset) > 0:
            print(f"Progreso: {len(dataset)} palabras extraídas...")

    # 4. Convertir a un DataFrame de Pandas y guardar en CSV
    df = pd.DataFrame(dataset)
    nombre_archivo = 'dataset_10000_ipa.csv'
    df.to_csv(nombre_archivo, index=False, encoding='utf-8')
    
    print(f"¡Éxito! Dataset guardado como '{nombre_archivo}' con {len(df)} registros.")
    print("\nPrimeros 5 registros de tu nuevo dataset:")
    print(df.head())

# Ejecutar la función
if __name__ == "__main__":
    generar_dataset_ipa(10000)