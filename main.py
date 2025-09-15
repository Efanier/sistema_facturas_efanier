print("Sistema de Facturación")

productos = [{"nombre": "Resma", "precio": 25000, "cantidad": 2},
             {"nombre": "Lapicero", "precio": 1500, "cantidad": 5},]

def calcular_total(productos):
    subtotal = 0
    tasa_iva = 0.19
    for producto in productos:
        subtotal += producto["precio"] * producto["cantidad"]
    if subtotal > 100000:
        subtotal *= 0.9  # Aplicar descuento del 10%
    iva = subtotal * tasa_iva
    total = subtotal + iva
    return subtotal, iva, total

subtotal, iva, total = calcular_total(productos)

productos = [{"nombre": "Resma", "precio": 25000, "cantidad": 2},
             {"nombre": "Lapicero", "precio": 1500, "cantidad": 5},]

def calcular_total(productos):
    subtotal = 0
    tasa_iva = 0.19
    for producto in productos:
        subtotal += producto["precio"] * producto["cantidad"]
    if subtotal > 100000:
        subtotal *= 0.9  # Aplicar descuento del 10%
    iva = subtotal * tasa_iva
    total = subtotal + iva
    return subtotal, iva, total

subtotal, iva, total = calcular_total(productos)

print("\nREPORTE DE VENTA\n")
print(
    "Producto".ljust(15) +
    "Cantidad".ljust(10) +
    "Precio Unitario".ljust(17) +
    "Total".ljust(10) + "\n"
)
for p in productos:
    total_prod = p["precio"] * p["cantidad"]
    print(
        p["nombre"].ljust(15) +
        str(p["cantidad"]).ljust(10) +
        str(p["precio"]).ljust(17) +
        str(total_prod).ljust(10) + "\n"
    )

print(f"Subtotal: {subtotal}\n")
print(f"IVA (19%): {iva}\n")
print(f"TOTAL: {total}\n")