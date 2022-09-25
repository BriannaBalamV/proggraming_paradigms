"""
Brianna Ayelen Balam Velasco

Ejercicio 1: 
Escribir una clase en python que convierta un número entero a número romano

"""

class enteros:
    def conversion_entero_romano(entero):
        numeros = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
        romanos = ['M', 'CM', 'D', 'CD', 'C', 'XC', 'L', 'XL', 'X', 'IX', 'V', 'IV', 'I']
    
        romano = ''
        i = 0
    
        while entero > 0:
            for _ in range(entero // numeros[i]):
                romano += romanos[i]
                entero -= numeros[i]
    
            i += 1
        
        return romano

entero = int(input("Ingrese un número entero:"))
if entero > 0:
    print(entero,"=",enteros.conversion_entero_romano(entero)) 