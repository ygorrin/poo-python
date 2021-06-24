class Animal:
    def __init__(self, numeroPatas, tipoAnimal):
        self.numeroPatas = numeroPatas
        self.tipoAnimal= tipoAnimal
    def comunicacion(self, sonido):
        print("Comunicacion:", sonido)
        return self
    def comer(self, comida):
        print("Come:", comida)
        return self
    def __str__(self):
        return f"El animal tiene {self.numeroPatas} patas y es de tipo {self.tipoAnimal}"

class Pato(Animal):
    def __init__(self, numeroPatas, tipoAnimal):
        super().__init__(numeroPatas, tipoAnimal)
        self.comunicacion("Duck Sound")
        self.comer("Peces")
    def __str__(self):
        return f"El Pato tiene {self.numeroPatas} patas y es de tipo {self.tipoAnimal}"

class Perro(Animal):
    def __init__(self, numeroPatas, tipoAnimal, mascota, nombre):
        super().__init__(numeroPatas, tipoAnimal)
        self.mascota = mascota
        self.nombre = nombre
        self.comunicacion("Ladra")
        self.comer("Pellets")
    def funcion(self, funcion):
        print ("Animal de compañia")
        return self
    def __str__(self):
        return f"El Perro tiene {self.numeroPatas} patas, es de tipo {self.tipoAnimal} y su nombre es: {self.nombre}"

animal1 = Animal(6,"carnivoro")
animal1.comer("carne")
print(animal1)

patito1 = Pato(2, "Ave")
patito1.comer("peces")
patito1.comunicacion("Duck Sound")
print(patito1)

perro1 = Perro(4, "Canino", True, "Buddy")
print(perro1)