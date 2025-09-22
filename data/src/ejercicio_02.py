import pandas as pd

def calificaciones():
    # 1. Creacion de series
    serie = pd.Series([85, 92, 78], index=['Matematicas', 'Ciencias', 'Historia'])
    print("--Serie de Calificaciones--")
    print(serie)
    print()

    # 2. Acceder a un valor específico
    print("Calificacion en Ciencias:", serie['Ciencias'])
    print()

    # 3. Informacion basica
    print("Dimensiones:", serie.shape)
    print("Valores unicos:", serie.unique())
    print()

    # 4. Estadisticas
    print("Suma:", serie.sum())
    print("Promedio:", serie.mean())

if __name__ == "__main__":
    calificaciones()
