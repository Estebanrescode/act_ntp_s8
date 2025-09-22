import pandas as pd
import json

def vehiculos_json():
    archivo = "vehiculos.json"

    # Generar archivo JSON
    vehiculos = [
        {"marca": "Toyota", "modelo": "Corolla", "año": 2020},
        {"marca": "Ford", "modelo": "Fiesta", "año": 2018},
        {"marca": "Honda", "modelo": "Civic", "año": 2019}
    ]

    with open(archivo, "w", encoding="utf-8") as f:
        json.dump(vehiculos, f, ensure_ascii=False, indent=4)

    # Leer archivo JSON
    df = pd.read_json(archivo)
    print("=== DataFrame de Vehículos ===")
    print(df)

    # Tipos de datos
    print("\nTipos de datos:")
    print(df.dtypes)

if __name__ == "__main__":
    vehiculos_json()
