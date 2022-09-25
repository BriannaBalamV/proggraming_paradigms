"""
Brianna Ayelen Balam Velasco

Ejercicio 5: 
Escribir una clase en python que encuentre un par de elementos (índice de los números) de una matriz dada cuya 
suma es igual a un número de destino especifico.

Entrada: numeros = [10,20,10,40,50,60,70], objetivo=50
                     0  1  2  3  4  5  6
Salida: 2, 3

"""

class indice_numeros:
    def suma_indices(entrada, objetivo):
        indices = {}

        for i, n in enumerate(entrada):
            if objetivo - n in indices:
                return indices[objetivo - n], i
            
            indices[n] = i


numeros = [10,20,10,40,50,60,70]
objetivo = 50

salida = indice_numeros.suma_indices(numeros, objetivo)
print(salida)
