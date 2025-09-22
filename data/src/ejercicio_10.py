# src/ejercicio_10.py
import os
import json
from pathlib import Path

import requests
import pandas as pd

def usuarios_api(url="http://localhost:3001/users"):
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()

        # Mostrar la respuesta cruda (primeros caracteres) para debug
        print("Respuesta (preview):", response.text[:300])

        # Intentar parsear JSON
        try:
            datos = response.json()
        except ValueError:
            print("La respuesta no es JSON válido:")
            print(response.text)
            return

        print("Tipo de datos recibido:", type(datos))

        # Si la respuesta es un dict con lista en 'users' o 'data', extraerla
        if isinstance(datos, dict):
            if "users" in datos and isinstance(datos["users"], list):
                datos = datos["users"]
            elif "data" in datos and isinstance(datos["data"], list):
                datos = datos["data"]
            else:
                # convertir dict simple en lista de un elemento
                datos = [datos]

        # Ahora datos debe ser una lista de dicts
        if not isinstance(datos, list):
            print("Formato inesperado. Se esperaba lista de objetos JSON.")
            return

        # Crear DataFrame
        df = pd.DataFrame(datos)
        print("=== DataFrame de Usuarios ===")
        print(df.head())

        print("\nInformación del DataFrame:")
        print(df.info())

        # Guardar JSON dentro de la carpeta 'data' de tu proyecto (busca ancestro con carpeta data o créala)
        current_file = Path(__file__).resolve()
        # Buscar un ancestro que ya contenga 'data'
        data_dir = None
        for a in current_file.parents:
            if (a / 'data').exists():
                data_dir = a / 'data'
                break
        if data_dir is None:
            # Si no existe, crear 'data' en el nivel esperado (padre de src)
            # Asumimos que este archivo está dentro de 'src' en el proyecto
            data_dir = current_file.parents[1] / 'data'
        data_dir.mkdir(parents=True, exist_ok=True)

        save_path = data_dir / "users_data.json"
        with open(save_path, "w", encoding="utf-8") as f:
            json.dump(datos, f, ensure_ascii=False, indent=2)

        print(f"\nJSON guardado en: {save_path}")

    except requests.exceptions.HTTPError as e:
        print("Error HTTP:", e)
    except requests.exceptions.Timeout:
        print("La petición tardó demasiado (timeout).")
    except requests.exceptions.ConnectionError as e:
        print("No se pudo conectar al servidor (¿arrancaste Mockoon?).", e)
    except requests.exceptions.RequestException as e:
        print("Error en la petición:", e)

if __name__ == "__main__":
    usuarios_api()
