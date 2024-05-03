import argparse
import pandas as pd
import requests
import zipfile
import io

def descargar_y_descomprimir_datos(url):
    try:
        # Realizar la solicitud GET a la URL para descargar el archivo ZIP
        response = requests.get(url)
        response.raise_for_status()  # Verificar si la solicitud fue exitosa
        
        # Descomprimir el contenido del archivo ZIP en memoria
        with zipfile.ZipFile(io.BytesIO(response.content)) as zip_file:
            # Obtener la lista de nombres de archivos dentro del ZIP
            zip_file_list = zip_file.namelist()
            
            # Buscar el archivo CSV dentro del ZIP (puede haber múltiples archivos)
            csv_files = [filename for filename in zip_file_list if filename.lower().endswith('.csv')]
            
            if not csv_files:
                raise ValueError("No se encontró ningún archivo CSV dentro del ZIP.")
            
            # Seleccionar el primer archivo CSV encontrado (asumimos que es el que queremos)
            csv_filename = csv_files[0]
            
            # Extraer el archivo CSV del ZIP
            with zip_file.open(csv_filename) as file:
                # Cargar el archivo CSV en un DataFrame
                df = pd.read_csv(file)
        
        return df
    
    except requests.exceptions.RequestException as e:
        print(f"Error al descargar los datos desde la URL: {e}")
        return None
    except (zipfile.BadZipFile, ValueError) as e:
        print(f"Error al descomprimir el archivo ZIP: {e}")
        return None

def categorizar_en_grupos(df):
    # Categorizar los datos en grupos según alguna columna (por ejemplo, edad)
    # En este ejemplo, agrupamos por rangos de edad
    df['Grupo_Edad'] = pd.cut(df['age'], bins=[0, 30, 40, 50, float('inf')],
                              labels=['<30', '30-40', '40-50', '50+'])
    return df

def exportar_a_csv(df, nombre_archivo):
    # Exportar el DataFrame a un archivo CSV
    df.to_csv(nombre_archivo, index=False)
    print(f"Datos exportados correctamente a {nombre_archivo}")

def main():
    # Configuración del argumento de línea de comandos para la URL
    parser = argparse.ArgumentParser(description='Procesamiento de datos desde una URL')
    parser.add_argument('url', type=str, help='URL desde la cual descargar los datos')
    parser.add_argument('--output', type=str, default='datos_procesados.csv', 
                        help='Ruta del archivo CSV de salida')
    args = parser.parse_args()
    
    # Descargar y descomprimir datos desde la URL proporcionada
    df = descargar_y_descomprimir_datos(args.url)
    
    if df is not None:
        # Categorizar los datos en grupos
        df_categorizado = categorizar_en_grupos(df)
        
        # Exportar el DataFrame resultante a un archivo CSV
        exportar_a_csv(df_categorizado, args.output)

if __name__ == '__main__':
    main()
