import pandas as pd
import numpy as np

def ventas_numpy():
    # Crear array NumPy 2D
    array = np.array([
        [1500, 2000, 1800],
        [2200, 2100, 2500],
        [1700, 1600, 1900]
    ])

    # Crear DataFrame
    df = pd.DataFrame(array, columns=['Q1', 'Q2', 'Q3'])
    print("-- DataFrame de Ventas Trimestrales --")
    print(df)

    # Tipos de datos
    print("\nTipos de datos:")
    print(df.dtypes)

if __name__ == "__main__":
    ventas_numpy()
