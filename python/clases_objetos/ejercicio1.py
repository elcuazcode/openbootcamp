
#+ clases y objetos ejercicio 1


class Vehiculo:

    def __init__(self, color, ruedas, puertas):
        self.color = color
        self.ruedas = ruedas
        self.puertas = puertas

class Coche(Vehiculo):
    
    def __init__(self, color, ruedas, puertas, velocidad, cilindrada):
        super().__init__(color, ruedas, puertas)
        self.velocidad = velocidad
        self.cilindrada = cilindrada

bmw = Coche('Gris', 4, 4, '290 Km/h', '3.0 L')

detalles_tecnicos = f'''
El coche es de color {bmw.color} tienes {bmw.ruedas} ruedas
ademas de {bmw.puertas} puertas y alcanza una velocidad de {bmw.velocidad} 
con un cilindraje de {bmw.cilindrada}
'''

print(detalles_tecnicos)