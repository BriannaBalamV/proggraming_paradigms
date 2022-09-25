"""
Brianna Ayelen Balam Velasco

Ejercicio 7: 
Escribir una clase en python que calcule pow(x, n)
x = es la base
n = es el exponente

"""

class potencia:
    def potencia_numero(base, exponente):
        resultado = 1
        
        for i in range(exponente):
            resultado *= base
            
        return resultado
    

base = int(input("Ingresa la base de la potencia:"))
exponente = int(input("Ingrese el exponente de la potencia:"))

print(base, "^", exponente, "=", potencia.potencia_numero(base, exponente))