import json
def abrirJSON():
    dicFinal={}
    with open('./Data/campers.json',"r") as openFile:
        dicFinal=json.load(openFile)
    return dicFinal

def guardarJSON(dic):
    with open("./Data/campers.json",'w') as outFile:
        json.dump(dic,outFile)

camp=abrirJSON()
def aggcamper():
    print("Ingrese el documento de identidad del nuevo Camper")
    id=int(input(": "))
    print("Ingrese el nombre del camper nuevo ")
    name=input(": ")
    print("Ingrese los apellidos del camper")
    apellido=input(": ")
    print("Ingrese la direccion del estudiante")
    dir=input(": ")
    print("Ingrese nombre del acudiente")
    acu=input(": ")
    print("Ingrese el numero de telefo no del estudiante")
    cel=input(": ")
    estado="inscrito"
    camp["Campers"].append({"ID":id,
                            "nombre":name,
                            "apellido":apellido,
                            "direccion":dir,
                            "acudientes":acu,
                            "#celular":cel,
                            "Estado":estado,
                            "Curso":""})
    guardarJSON(camp)

def incripcion():
    print("Igrese su documento de identidad")
    id=int(input(": "))
    print("Ingrese sus nombres (de tener dos ingresar los dos)")
    name=input(": ")
    print("Ingrese sus apellidos")
    apellido=input(": ")
    print("Ingrese su direccion de residencia")
    dir=input(": ")
    print("Ingrese nombre de su acudiente")
    acu=input(": ")
    print("Ingrese el numero de telefono")
    cel=input(": ")
    estado="inscrito"
    camp["Campers"].append({"ID":id,
                            "nombre":name,
                            "apellido":apellido,
                            "direccion":dir,
                            "acudientes":acu,
                            "#celular":cel,
                            "Estado":estado,
                            "Curso":""})
    guardarJSON(camp)

def verestudiantes():
    c=0
    for i in range(len(camp["Campers"])):
       print("Camper#",i+1," ID: ",camp["Campers"][c]["ID"])
       print("Nombre: ",camp["Campers"][c]["nombre"])
       print("apellido: ",camp["Campers"][c]["apellido"])
       print("direccion: ",camp["Campers"][c]["direccion"])
       print("Nacudientes: ",camp["Campers"][c]["acudientes"])
       print("#celular: ",camp["Campers"][c]["#celular"])
       print("Estado: ",camp["Campers"][c]["Estado"])
       print("Curso ",camp["Campers"][c]["Curso"])
       c+=1

def Editarestudiantes():
    verestudiantes()
    print("A que estudiante quiere editar?")
    E=int(input(": "))
    
    print('''
    Que quiere editar?
    (1). ID
    (2). Nombre
    (3). Apellido
    (4). Dieccion
    (5). Acudiente
    (6). #celular
    (7). Estado
    (8). Curso''')
    ed=int(input(": "))
    
    
    
    #match E:  #(Falta entrar al diccionario para elegir el estudiante a editar) 
     #   case 1:
      #      IDnuevo = int(input("Ingresa el nuevo ID: "))
       #     camp["ID"] = IDnuevo
        #    guardarJSON(camp)
##Crear una contrasena para el usuario trainner  
#pero igual solo cree el menu las funciones las implementamos en el main
