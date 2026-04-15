import pandas as pd

# ==========================================
# RUTAS AQUÍ
# ==========================================
ruta_entrada = './dataset_combinado.csv' 
ruta_salida = './dataset_final.csv' 
# ==========================================

def eliminar_duplicados(input_csv, output_csv):
    try:
        # Cargar el dataset
        df = pd.read_csv(input_csv)
        
        # Asegurarnos de mantener solo los encabezados solicitados (por si el CSV original tiene más)
        df = df[['text', 'ipa']]
        
        # Eliminar las filas donde la palabra en la columna 'text' esté duplicada
        df_limpio = df.drop_duplicates(subset=['text'], keep='first')
        
        # Guardar el nuevo dataset en un archivo CSV
        df_limpio.to_csv(output_csv, index=False)
        
        # Mostrar un pequeño resumen en consola
        print("¡Proceso completado con éxito!")
        print(f"Filas originales: {len(df)}")
        print(f"Filas tras eliminar duplicados: {len(df_limpio)}")
        print(f"Archivo guardado en: {output_csv}")
        
    except FileNotFoundError:
        print(f"Error: No se pudo encontrar el archivo en la ruta '{input_csv}'. Verifica que esté bien escrita.")
    except KeyError:
        print("Error: El archivo original no contiene las columnas 'text' e 'ipa'.")

# Ejecutar la función
eliminar_duplicados(ruta_entrada, ruta_salida)