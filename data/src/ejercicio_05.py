import pandas as pd

def empleados_dataframe():
    # Lista de diccionarios
    empleados = [
        {'empleado': 'Ana', 'salario': 2500, 'departamento': 'Ventas'},
        {'empleado': 'Luis', 'salario': 3200, 'departamento': 'TI'},
        {'empleado': 'Marta', 'salario': 2800, 'departamento': 'Marketing'}
    ]

    # Crear DataFrame
    df = pd.DataFrame(empleados)
    print("=== DataFrame de Empleados ===")
    print(df)

    # Acceder a filas específicas
    print("\nPrimer empleado:")
    print(df.loc[0])

    print("\nEmpleados 0 y 2:")
    print(df.loc[[0, 2]])

if __name__ == "__main__":
    empleados_dataframe()
