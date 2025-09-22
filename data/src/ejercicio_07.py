import pandas as pd
import csv

def cursos_csv():
    archivo = "cursos.csv"

    # Crear archivo CSV
    cursos = [
        ['curso', 'instructor', 'duracion'],
        ['Python', 'Ana', '40h'],
        ['Data Science', 'Luis', '60h'],
        ['Machine Learning', 'Marta', '50h']
    ]

    with open(archivo, mode='w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerows(cursos)

    # Leer archivo CSV
    try:
        df = pd.read_csv(archivo)
        print("=== DataFrame de Cursos ===")
        print(df)
    except FileNotFoundError:
        print("El archivo no existe.")

if __name__ == "__main__":
    cursos_csv()
