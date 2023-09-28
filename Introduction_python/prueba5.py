class Carta:
    def __init__(self, emisor, receptor):
        self.emisor = emisor
        self.receptor = receptor
        self.tiene_estampilla = False

    def poner_estampilla(self):
        self.tiene_estampilla = True

    def enviar(self):
        if self.tiene_estampilla:
            print(f"{self.emisor} ha enviado Carta a {self.receptor}")
        else:
            print("No se puede enviar la carta sin estampilla")

class Paquete:
    def __init__(self, emisor, receptor, max_volumen):
        self.emisor = emisor
        self.receptor = receptor
        self.max_volumen = max_volumen
        self.abierto = True
        self.productos = []

    def agregar_producto(self, peso, volumen):
        if not self.abierto:
            self.abrir()
        self.productos.append((peso, volumen))

    def cerrar(self):
        volumen_total = sum(volumen for peso, volumen in self.productos)
        if volumen_total <= self.max_volumen:
            self.abierto = False
        else:
            print("No se puede cerrar el paquete debido al exceso de volumen")

    def enviar(self):
        if not self.abierto:
            peso_total = sum(peso for peso, volumen in self.productos)
            if peso_total <= 30:
                print(f"{self.emisor} ha enviado Paquete a {self.receptor}")
            else:
                print("No se puede enviar el paquete debido al exceso de peso")
        else:
            print("No se puede enviar el paquete abierto")

# Ejemplo de uso:
carta = Carta("Gastón", "David")
carta.poner_estampilla()
carta.enviar()

paquete = Paquete("Gastón", "Alicia", 100)
paquete.agregar_producto(10, 20)
paquete.agregar_producto(15, 30)
paquete.cerrar()
paquete.enviar()

paquete2 = Paquete("Elliot", "Alicia", 100)
paquete2.agregar_producto(10, 5)  # Modificar peso para que sea menor o igual a 30
paquete2.cerrar()
paquete2.enviar()
