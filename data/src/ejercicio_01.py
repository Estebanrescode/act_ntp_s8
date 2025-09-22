# Ejercicio 1
import pandas as pd

def analisis_ventas():
    # creacion de series de ventas
    ventas = pd.Series([150, 200, 180, 220, 175, 190, 165])
    print("--Serie de Ventas Diarias--")
    print(ventas)
    print()

    # 2. Acceder al valor numero 3
    print("Valor en indice 3:", ventas[3])
    print()

    # 3. calculacion de promedio
    promedio = ventas.mean()
    print("Promedio de ventas:", promedio)
    print()

    # 4. orden de valores
    ordenadas = ventas.sort_values()
    print("Ventas ordenadas:")
    print(ordenadas)

if __name__ == "__main__":
    analisis_ventas()

print("=== Fin del ejercicio ===")