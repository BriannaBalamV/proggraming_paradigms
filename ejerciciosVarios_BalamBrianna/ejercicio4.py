"""
Brianna Ayelen Balam Velasco

Ejercicio 4: 
Escribir una clase en python que obtenga todos los posibles subconjuntos únicos de un conjunto de números enteros distintos.
Entrada: [4, 5, 6]
Salida: [[], [6], [5], [5, 6], [4], [4, 6], [4, 5], [4, 5, 6]]

"""

class subconjuntos_unicos:
    def subconjuntos(entrada):
        return subconjuntos_recursivo([], sorted(entrada))

def subconjuntos_recursivo(actual, conjunto):
    if conjunto:
        return subconjuntos_recursivo(actual, conjunto[1:]) + subconjuntos_recursivo(actual + [conjunto[0]], conjunto[1:])
    return [actual]


entrada = [4, 5, 6]
resultado = subconjuntos_unicos.subconjuntos(entrada)

print(resultado)