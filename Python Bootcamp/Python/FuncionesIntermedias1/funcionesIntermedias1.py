'''
a. Actualizar valores en diccionarios y listas
1. Cambia el valor 10 en x a 15. Una vez que hayas terminado, x ahora debería ser [ [5,2,3], [15,8,9] ].
2. Cambia el "apellido” del primer alumno de 'Jordan' a 'Bryant'.
3. En el directorio_deportes, cambia "Messi" por "Andrés".
4 Cambia el valor 20 en z a 30.
'''

x = [ [5,2,3], [10,8,9] ] 
estudiantes = [
    {'first_name':  'Michael', 'last_name' : 'Jordan'},
    {'first_name' : 'John', 'last_name' : 'Rosales'}
]
directorio_deportes = {
    'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
    'fútbol' : ['Messi', 'Ronaldo', 'Rooney']
}

z = [ {'x': 10, 'y': 20} ]

#a-1
x[1][0] = 15
print(x[1][0])

#a-2
estudiantes[0]["last_name"] = "Bryant"
print(estudiantes[0]["last_name"])

#a-3
directorio_deportes["fútbol"][0] = "Andrés"
print(directorio_deportes["fútbol"][0])

#a-4
z[0]['y'] = 30
print(z[0]['y'])

'''
b.Iterar a través de una lista de diccionarios
Crea una función iterateDictionary(some_list)para que, dada una lista de diccionarios,
la función recorra cada diccionarios de la lista e imprima cada llave y el valor asociado. 
Por ejemplo, dada la siguiente lista:
# debería devolver: (está bien si cada par clave-valor termina en 2 líneas separadas;
# un bonus para que aparezcan exactamente como se muestra a continuación)
first_name - Michael, last_name - Jordan
first_name - John, last_name - Rosales
first_name - Mark, last_name - Guillen
first_name - KB, last_name - Tonel
'''

estudiantes = [
        {'first_name':  'Michael', 'last_name' : 'Jordan'},
        {'first_name' : 'John', 'last_name' : 'Rosales'},
        {'first_name' : 'Mark', 'last_name' : 'Guillen'},
        {'first_name' : 'KB', 'last_name' : 'Tonel'}
    ]

def iterateDictionary(some_list):
    for ite in some_list:
        valor = list(ite.items()) #list convierte diccionario en lista
        print(valor[0][0],"-",valor[0][1],",",valor[1][0],"-",valor[1][1])

iterateDictionary(estudiantes)


'''
c. Obtener valores de una lista de diccionarios
Crea una función iterateDictionary2(key_name, some_list)que, dada una lista de diccionarios y 
un nombre de clave, la función imprima el valor almacenado en esa clave para cada diccionario. 
Por ejemplo, iterateDictionary2('name', estudiantes) debería generar:
Michael
John
Mark
KB
Y iterateDictionary2('last_name', estudiantes) debería generar:
Jordan
Rosales
Guillen
Tonel
'''

estudiantes = [
        {'first_name':  'Michael', 'last_name' : 'Jordan'},
        {'first_name' : 'John', 'last_name' : 'Rosales'},
        {'first_name' : 'Mark', 'last_name' : 'Guillen'},
        {'first_name' : 'KB', 'last_name' : 'Tonel'}
    ]

def iterateDictionary2(key_name, some_list):
    for i in some_list:
        print(i[key_name])
    

print(iterateDictionary2('first_name', estudiantes))
print(iterateDictionary2('last_name', estudiantes))

'''
d. Iterar a través de un diccionarios con valores de lista
Crea una función printInfo(some_dict)que, dado un diccionario cuyos valores son todos listas, 
imprima el nombre de cada clave junto con el tamaño de su lista, y luego imprima los valores 
asociados dentro de la lista de cada clave. Por ejemplo:
# salida:
7 UBICACIONES
San Jose
Seattle
Dallas
Chicago
Tulsa
DC
Burbank
    
8 INSTRUCTORES
Michael
Amy
Eduardo
Josh
Graham
Patrick
Minh
Devon
'''

dojo = {
'ubicaciones': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
'instructores': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}


def printInfo(some_dict):
    for k in some_dict:
        print(len(some_dict[k]),k)
        for i in some_dict[k]:
            print(i)
            
printInfo(dojo)
