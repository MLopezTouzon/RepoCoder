class Persona():
    def __init__(self, nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido
    def hablar(self):
        print(f"Hola mi nombre es {self.nombre}")
    def __str__(self):
        print (f"hola soy {self.nombre} {self.apellido}")


