
#+ clases y objetos ejercicio 2

class Alumno:

    def __init__(self, nombre, nota):
        self.nombre = nombre
        self.nota = nota

    def aprovado(self):
        if self.nota <= 6:
            return f'No es suficiente, debes tenes una nota mayor a 6 y tu nota es {self.nota}'
        else:
            return 'Disfruta tus vacaciones has aprovado'
        
w = True
while w:

    print('Ingresa tus datos, presiona "x" para terminar el programa.')

    name = input('Tu nombre porfavor: ')
    if name == 'x':
        w = False
    else:
        notes = int(input('Cual fue tu nota: '))

        otro_estudiante = Alumno(name, notes)
        print(otro_estudiante.aprovado())
    
    print('Gracias por utilizar los servicios escolares')