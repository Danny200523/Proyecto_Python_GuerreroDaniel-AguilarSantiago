import json
def abrirJSON():
    dicFinal={}
    with open('/home/camper/Documentos/Proyecto_Python_GuerreroDaniel-AguilarSantiago/Data/campers.json',"r") as openFile:
        dicFinal=json.load(openFile)
    return dicFinal

def guardarJSON(dic):
    with open("/home/camper/Documentos/Proyecto_Python_GuerreroDaniel-AguilarSantiago/Data/campers.json",'w') as outFile:
        json.dump(dic,outFile)

camp=abrirJSON()
def aggcamper():
    print("Igrese el documento de identidad del nuevo Camper")
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
    camp["Campers"].append({"ID":id,
                            "nombre":name,
                            "apellido":apellido,
                            "direccion":dir,
                            "acudientes":acu,
                            "#celular":cel,
                            "Estado":"",
                            "Curso":""})
    guardarJSON(camp)

def verestudiantes():
    c=0
    for i in range(len(camp["Campers"])):
       print("Camper#",i+1," ".join(camp["Campers"][c]["ID"]))
       c+=1

verestudiantes()
##Crear una contrasena para el usuario trainner
