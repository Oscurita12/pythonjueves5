opcion=100

print("***Empanadas inteligentes***")
print("1. Agregar Clientes: ")
print("2. Mostrar Clientes: ")
print("3. Busque un CLIENTE por cedula: ")
print("0. Salir ")



#Lista
clientes=[]

while(opcion !=0):  

    #Diccionario
    cliente={}

    #Pedimos la opcion deseada
    opcion=int(input("Digite la opción preferida: "))

    #Caminos del menu
    if(opcion==1):

        cliente['cedula']=input("Digite su cedula: ")
        cliente['nombre']=input("Digite su nombre: ")
        clientes.append(cliente)

        #print(cliente)
    elif(opcion==2):
        print(clientes)
    elif(opcion==3):
        #print(cliente["cedula"])
        cedula = input("Digite la cedula: ")
        for cliente in clientes:
            if(cliente["cedula"]==cedula):
                print(f"Cliente enocntrado: {cliente['cedula']}")
            else:
                print("Usuario no encontrado")
    elif(opcion==0):
        break
    else:
        print("Digite una opción válida")

else:
    print("Adios")
