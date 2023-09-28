def precio_total(boletas):
    total=0
    for boleta in boletas:
        total +=boleta['precio']
    return total

def precio_mes(boletas):
    precio_por_mes={}
    for boleta in boletas:
        fecha=boleta['fecha_compra']
        mes_año=fecha[3:]
        if mes_año in precio_por_mes:
            precio_por_mes[mes_año]+=boleta['precio']
        else:
            precio_por_mes[mes_año]=boleta['precio']
    return precio_por_mes

def productos_frecuentes(boletas):
    productos_por_boleta = [set(boleta['productos'].keys()) for boleta in boletas]
    
    # Crear un conjunto que contenga todos los productos de todas las boletas
    todos_los_productos = set()
    for productos in productos_por_boleta:
        todos_los_productos.update(productos)
    
    productos_frecuentes = set()
    total_boletas = len(boletas)
    
    for producto in todos_los_productos:
        contador = 0
        for boleta in boletas:
            if producto in boleta['productos']:
                contador += 1
        if contador >= total_boletas / 2:
            productos_frecuentes.add(producto)
    
    return productos_frecuentes


boletas = [{'fecha_compra' : '29-05-22',
'precio' : 12000,
'productos' : {'Chocolate': 1,
'Mantequilla': 1,
'Huevos': 12,
'Pan' : 1}
},
{'fecha_compra' : '31-05-22',
'precio' : 2400,
'productos' : {'Pan': 1, 'Leche' : 2}
},
{'fecha_compra' : '01-06-22',
'precio' : 3000,
'productos' : {'Mantequilla': 2, 'Azucar' : 1}
}
]

print("Precio total de todas las compras:", precio_total(boletas))
print("Precio por Mes:",precio_mes(boletas))
print("Productos Frecuentes:", productos_frecuentes(boletas))