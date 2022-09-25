"""
Brianna Ayelen Balam Velasco

Ejercicio 6: 
Escribir una clase en python que encuentre los 3 elementos que sumen 0 a partir de números reales
Entrada: [-25, -10, -7, -3, 2, 4, 8, 10]
Salida: [[-10, 2, 8], [-7, -3, 10]]

"""
from itertools import combinations

class suma_elementos:
    def suma_cero(entrada):
        sub_tres = list(combinations(entrada, 3))
        sublistas = []

        for i in sub_tres:
            if sum(i) == 0:
                sublistas.append(i)
        
        return sublistas

entrada = [-25, -10, -7, -3, 2, 4, 8, 10]
resultado = suma_elementos.suma_cero(entrada)

print(resultado)