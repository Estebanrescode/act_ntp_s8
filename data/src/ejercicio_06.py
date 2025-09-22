import pandas as pd

def libros_dataframe():
    # Lista de listas con datos de libros
    datos = [
        ['El Quijote', 'Cervantes', 1605],
        ['Cien Años de Soledad', 'Garcia Marquez', 1967],
        ['La Ciudad y los Perros', 'Vargas Llosa', 1963]
    ]

    columnas = ['Titulo', 'Autor', 'Año']

    # Crear DataFrame
    df = pd.DataFrame(datos, columns=columnas)
    print("=== DataFrame de Libros ===")
    print(df)

    # Dimensiones
    print("\nDimensiones del DataFrame:", df.shape)

if __name__ == "__main__":
    libros_dataframe()
