print("Sistema de Facturación")

productos = [{"nombre": "Resma", "precio": 25000, "cantidad": 2},
             {"nombre": "Lapicero", "precio": 1500, "cantidad": 5},]

def calcular_total(productos):
    subtotal = 0
    tasa_iva = 0.16
    for producto in productos:
        subtotal += producto["precio"] * producto["cantidad"]
    if subtotal > 100000:
        subtotal *= 0.9  # Aplicar descuento del 10%
    iva = subtotal * tasa_iva
    total = subtotal + iva
    return subtotal, iva, total

subtotal, iva, total = calcular_total(productos)
print(f"Subtotal: {subtotal}")
print(f"IVA: {iva}")
print(f"Total: {total}")

