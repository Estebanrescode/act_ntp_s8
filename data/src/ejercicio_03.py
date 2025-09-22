import pandas as pd

def operaciones_series():
    precios = pd.Series([100, 150, 200])
    descuentos = pd.Series([10, 20, 15])

    print("-- Precios --")
    print(precios)
    print("\n-- Descuentos --")
    print(descuentos)

    # Resta elemento a elemento
    precios_descuento = precios - descuentos
    print("\nPrecios con descuentos aplicados:")
    print(precios_descuento)

    # Multiplicar por IVA 16%
    precios_iva = precios * 1.16
    print("\nPrecios con IVA (16%):")
    print(precios_iva)

    # Demostracion operaciones elemento a elemento
    print("\n Demostracion (precio[0] - descuento[0]):", precios[1] - descuentos[1])

if __name__ == "__main__":
    operaciones_series()
