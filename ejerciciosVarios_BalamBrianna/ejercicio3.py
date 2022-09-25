"""
Brianna Ayelen Balam Velasco

Ejercicio 3: 
Escribir una clase en python para encontrar la validez de una cadena de paréntesis, '(', ')', '{', '}', '['  ']. Los paréntesis 
deben aparecer en el orden correcto, por ejemplo "()" y "()[]{}" son validos, pero "[)", "({[)]" y "{{{" son inválidos.

"""

class validez_cadena:
    def cadena_true(cadena):
        lista = []
        parentesis = {'{':'}', '(':')', '[':']'}

        for i in cadena:
            if i in parentesis:
                lista.append(i)
            elif len(lista) == 0 or i != parentesis[lista.pop()]:
                return False
        
        return len(lista) == 0
    
cadena = input("Ingrese la cadena de parentesis a validar:")
print(cadena,'=', validez_cadena.cadena_true(cadena))