diccionario={
    'nombre':'Clara',
    'Edad': '18',
    'Estatura':'157',
    'ocupacion':'estudiante',
    'habilidad': 'llorar por todo',
    'estado actual':'sobreviviendo',
    'gustos':'leer',
    'musica fav':'De todo menos vallenato',
    'hobbies':'dibujar mal',
    'ganas de existir':'mas o menos'
}

""" Accediendo de forma individual a los atributos y 
valores de un diccionario """
print(diccionario)
#print(diccionario['nombre'])
#print(diccionario.get('Edad'))

""" Acceder a TODOS los atributos y valores de 
un diccionario al mismo tiempo """

#Recorrer un diccionario
for clave,valor in diccionario.items(): 
    print(clave,valor)

#Agegregar desde el código una propiedad mas
diccionario['apellido'] = 'restrepo'