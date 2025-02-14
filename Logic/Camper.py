import json
def abrirJSON():
    dicFinal={}
    with open('./Data/campers.json',"r") as openFile:
        dicFinal=json.load(openFile)
    return dicFinal

def guardarJSON(dic):
    with open("./Data/campers.json",'w') as outFile:
        json.dump(dic,outFile)

def abrirJSO():
    dicFinal={}
    with open('./Data/Rutas.json',"r") as openFile:
        dicFinal=json.load(openFile)
    return dicFinal

def guardarJSO(dic):
    with open("./Data/Rutas.json",'w') as outFile:
        json.dump(dic,outFile)

def abrirJS():
    dicFinal={}
    with open("./Data/HorariosCursos.json","r") as openFile:
        dicFinal=json.load(openFile)
    return dicFinal

def guardarJS(dic):
    with open("./Data/HorariosCursos.json",'w') as outFile:
        json.dump(dic,outFile)
        
camp=abrirJSON()

def Incripcion():
    print("Ingrese su documento de identidad")
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
    estado={
                "Aprobado": False,
                "Cursando": False,
                "En proceso de ingreso": False,
                "Expulsado": False,
                "Graduado": False,
                "Inscrito": True,
                "Retirado": False
            },
    camp["Campers"].append({"ID":id,
                            "nombre":name,
                            "apellido":apellido,
                            "direccion":dir,
                            "acudientes":acu,
                            "#celular":cel,
                            "Estado":estado,
                            "Curso":""})
    guardarJSON(camp)

def vernota():
    print("Ingrese su documento de identidad")
    id=int(input(": "))
    for i in range(len(camp["Campers"])):
        if camp["Campers"][i]["ID"]==id:
            print("Ingrese la ruta que desea ver")
            print("Java")
            print("NodeJS")
            print("NetCore")
            ruta=input(": ")
            print("Ingrese la skill que desea ver")
            print("Filtro")
            print("Proyecto")
            print("Otros")
            skill=input(": ")
            print("Ingrese la nota que desea ver")
            print("Nota1")
            print("Nota2")
            print("Nota3")
            nota=input(": ")
            print(camp["Campers"][i]["Notas"][ruta][skill][nota])
