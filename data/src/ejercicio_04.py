import pandas as pd

def productos_dataframe():
    # 1. Diccionario de datos
    datos = {
        'Producto': ['Laptop', 'Smartphone', 'Tablet'],
        'Precio': [3500, 1200, 800],
        'Categoria': ['Tecnologia', 'Tecnologia', 'Tecnologia']
    }

    # 2. Crear DataFrame
    df = pd.DataFrame(datos)
    print("-- DataFrame de Productos --")
    print(df)

    # 3. Acceder a columna
    print("\nColumna de precios:")
    print(df['Precio'])

    # 4. Información básica
    print("\nInformacion del DataFrame:")
    print(df.info())

if __name__ == "__main__":
    productos_dataframe()
