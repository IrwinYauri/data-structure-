class Humano:
    def __init__(self,edad,apellido=None):
        self.edad=edad
        self.apellido=apellido

    def hablar(self,mensaje):
        print(mensaje)

pedro=Humano(25,"Yauri")
raul=Humano(10)

pedro.hablar("Soy Pedro "+pedro.apellido+" y tengo "+str(pedro.edad))
raul.hablar("Soy Raul "+str(raul.apellido)+" y tengo "+str(raul.edad))