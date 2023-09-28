# command+k+c -- comentar
# command+k+u --descomentar

# EJECRICIO 1

# def sacar_promedio(tupla):
#     nombre = tupla[0]
#     notas = tupla[1:]
#     promedio = sum(notas) / len(notas)
#     nueva_tupla = (nombre, promedio)
#     return nueva_tupla

# tupla = ('Camila', 5.0, 6.2, 4.8, 6.0)
# resultado = sacar_promedio(tupla)
# print(resultado)

#Ejecicio 2

# def agregar_entero(lista, entero):
#     index = 0
    
#     while index < len(lista) and lista[index] < entero:
#         index += 1
        
#     lista.insert(index, entero)
#     return lista

# lista = [-40, -1, 1, 5, 16, 72, 100]
# entero = 13

# lista_actualizada = agregar_entero(lista, entero)
# print(lista_actualizada)

#Ejercicio 3

# def max_repetido(lista):
#     frecuencia = {}
    
#     for num in lista:
#         if num in frecuencia:
#             frecuencia[num] += 1
#         else:
#             frecuencia[num] = 1
    
#     max_repeticiones = max(frecuencia.values())
#     return max_repeticiones

# lista = [1, 4, 6, 2, 4, 3, 1, 1, 3, 5, 6, 7, 3, 4, 5, 5, 5, 3, 3, 2, 1, 2, 1, 1, 1, 2, 6, 6]
# resultado = max_repetido(lista)
# print(resultado)

# Ejecicio 4

# def agregar_estudiante(lista, estudiante):
#     lista.append(estudiante)
#     lista.sort(key=lambda x: (x.split()[-1], x.split()[0]))
#     return lista

# estudiantes = [
#     'Mario Avedaño',
#     'Policarpo Avedaño',
#     'Juan Bodoque',
#     'Juanin Harry',
#     'Mario Hugo',
#     'Dylan Manguera',
#     'Eusebio Manguera'
# ]

# nuevo_estudiante = 'Eliza Manguera'

# estudiantes_actualizados = agregar_estudiante(estudiantes, nuevo_estudiante)
# print(estudiantes_actualizados)

