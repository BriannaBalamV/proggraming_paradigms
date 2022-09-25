"""
Brianna Ayelen Balam Velasco

Ejercicio 9: 
Escribir una clase en python con 2 métodos: get_string y print_string. get_string acepta una 
cadena ingresada por el usuario y print_string imprime la cadena en mayúsculas.

"""

class cadena():
    def __init__(self):
        self.cadena_input = ""

    def get_String(self):
        self.cadena_input = input()

    def print_String(self):
        print(self.cadena_input.upper())

print("Ingrese una oracion en minusculas:")
entrada = cadena()
entrada.get_String()
print("Oracion en mayusculas:")
entrada.print_String()