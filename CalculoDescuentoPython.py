# archivo: calculo_descuento.py

def calcular_descuento(monto_total, porcentaje_descuento=10):
    """
    Calcula el descuento aplicado a una compra.
    - monto_total: valor de la compra
    - porcentaje_descuento: porcentaje de descuento (por defecto 10%)
    """
    descuento = monto_total * (porcentaje_descuento / 100)
    return descuento


# Programa principal
if __name__ == "__main__":
    # Ejemplo 1: solo monto total (usa 10% por defecto)
    monto1 = 100
    descuento1 = calcular_descuento(monto1)
    total1 = monto1 - descuento1
    print(f"Compra: ${monto1} | Descuento: ${descuento1:.2f} | Total a pagar: ${total1:.2f}")

    # Ejemplo 2: monto total + porcentaje personalizado
    monto2 = 300
    descuento2 = calcular_descuento(monto2, 15)  # 15% de descuento
    total2 = monto2 - descuento2
    print(f"Compra: ${monto2} | Descuento: ${descuento2:.2f} | Total a pagar: ${total2:.2f}")
