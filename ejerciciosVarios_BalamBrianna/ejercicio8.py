"""
Brianna Ayelen Balam Velasco

Ejercicio 8: 
Escribir una clase en python que revierta una cadena de palabras
Entrada: "Mi Diario Python"
Salida: "Python Diario Mi"

"""

class cadenas_invertidas:
    def invertir(oracion):
        oracion_invertida = ' '.join(reversed(oracion.split()))
        return oracion_invertida
    
oracion = 'Mi Diario Python'

print(oracion)
print(cadenas_invertidas.invertir(oracion))