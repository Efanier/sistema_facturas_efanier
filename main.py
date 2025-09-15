print("Sistema de Facturación")

productos = [{"nombre": "Resma", "precio": 25000, "cantidad": 2},
             {"nombre": "Lapicero", "precio": 1500, "cantidad": 5},]


def calcular_total(productos, cliente_frecuente=True):
    subtotal = 0
    tasa_iva = 0.19
    for producto in productos:
        subtotal += producto["precio"] * producto["cantidad"]
    
    if subtotal > 100000:
        subtotal *= 0.9  # Aplicar descuento del 10%

    if cliente_frecuente == True:
        subtotal *= 0.95  # Aplicar descuento del 5%
    
    iva = subtotal * tasa_iva
    total = subtotal + iva
    return subtotal, iva, total

subtotal, iva, total = calcular_total(productos)
print(f"Subtotal: {subtotal:.2f}")
print(f"IVA: {iva:.2f}")
print(f"Total: {total:.2f}")

