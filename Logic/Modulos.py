import json
def abrirJSON():
    dicFinal={}
    with open('../Data/campers.json',"r") as openFile:
        dicFinal=json.load(openFile)
    return dicFinal

def guardarJSON(dic):
    with open("../Data/campers.json",'w') as outFile:
        json.dump(dic,outFile)

def abrirJSO():
    dicFinal={}
    with open('../Data/Rutas.json',"r") as openFile:
        dicFinal=json.load(openFile)
    return dicFinal

def guardarJSO(dic):
    with open("../Data/Rutas.json",'w') as outFile:
        json.dump(dic,outFile)

def abrirJS():
    dicFinal={}
    with open('../Data/HorariosCursos.json',"r") as openFile:
        dicFinal=json.load(openFile)
    return dicFinal

def guardarJS(dic):
    with open("../Data/HorariosCursos.json",'w') as outFile:
        json.dump(dic,outFile)

camp=abrirJSON()
rut=abrirJSO()
Hor=abrirJS()
def Aggcamper():
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

def Incripcion():
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

def Vercamper():
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

def Editarcamper():
    Vercamper()
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
    if ed==1:
        print("Ingrese el nuevo ID")
        identi=input(": ")
        camp["Campers"][ed-1]["ID"]=identi
    elif ed==2:
        print("Ingrese el nuevo Nombre(Nombres)")
        name=input(": ")
        camp["Campers"][ed-1]["nombre"]=name
    elif ed==3:
        print("Ingrese el nuevo Apellido(Apellidos)")
        apll=input(": ")
        camp["Campers"][ed-1]["apellido"]=apll
    elif ed==4:
        print("Ingrese la nueva direccion")
        direc=input(": ")
        camp["Campers"][ed-1]["direccion"]=direc
    elif ed==5:
        print("Ingrese el nuevo Nombre del acudiente(Nombres)")
        acud=input(": ")
        camp["Campers"][ed-1]["nombre"]=acud
    elif ed==6:
        print("Ingrese el nuevo #Celular")
        celul=input(": ")
        camp["Campers"][ed-1]["#celular"]=celul
    elif ed==8:
        print("Ingrese el nuevo curso")
        cur=input(": ")
        camp["Campers"][ed-1]["Curso"]=cur
    bo=False
    while bo==False:
        if ed==7:
            print("Ingrese el nuevo Estado")
            print('''
                (1). Aprobado
                (2). Cursando
                (3). En proceso de ingreso
                (4). Expulsado
                (5). Graduado
                (6). Inscrito
                (7). Retirado
              ''')
            estad=input(": ")
            if estad==1:
                camp["Campers"][ed-1]["Estado"]["Aprobado"]=True
                camp["Campers"][ed-1]["Estado"]["Cursando"]=False
                camp["Campers"][ed-1]["Estado"]["En proceso de ingreso"]=False
                camp["Campers"][ed-1]["Estado"]["Expulsado"]=False
                camp["Campers"][ed-1]["Estado"]["Graduado"]=False
                camp["Campers"][ed-1]["Estado"]["Inscrito"]=False
                camp["Campers"][ed-1]["Estado"]["Retirado"]=False
                bo=True
                guardarJSON(camp)
            elif estad==2:
                camp["Campers"][ed-1]["Estado"]["Aprobado"]=False
                camp["Campers"][ed-1]["Estado"]["Cursando"]=True
                camp["Campers"][ed-1]["Estado"]["En proceso de ingreso"]=False
                camp["Campers"][ed-1]["Estado"]["Expulsado"]=False
                camp["Campers"][ed-1]["Estado"]["Graduado"]=False
                camp["Campers"][ed-1]["Estado"]["Inscrito"]=False
                camp["Campers"][ed-1]["Estado"]["Retirado"]=False
                bo=True
                guardarJSON(camp)
            elif estad==3:
                camp["Campers"][ed-1]["Estado"]["Aprobado"]=False
                camp["Campers"][ed-1]["Estado"]["Cursando"]=False
                camp["Campers"][ed-1]["Estado"]["En proceso de ingreso"]=True
                camp["Campers"][ed-1]["Estado"]["Expulsado"]=False
                camp["Campers"][ed-1]["Estado"]["Graduado"]=False
                camp["Campers"][ed-1]["Estado"]["Inscrito"]=False
                camp["Campers"][ed-1]["Estado"]["Retirado"]=False
                bo=True
                guardarJSON(camp)
            elif estad==4:
                camp["Campers"][ed-1]["Estado"]["Aprobado"]=False
                camp["Campers"][ed-1]["Estado"]["Cursando"]=False
                camp["Campers"][ed-1]["Estado"]["En proceso de ingreso"]=False
                camp["Campers"][ed-1]["Estado"]["Expulsado"]=True
                camp["Campers"][ed-1]["Estado"]["Graduado"]=False
                camp["Campers"][ed-1]["Estado"]["Inscrito"]=False
                camp["Campers"][ed-1]["Estado"]["Retirado"]=False
                bo=True
                guardarJSON(camp)
            elif estad==5:
                camp["Campers"][ed-1]["Estado"]["Aprobado"]=False
                camp["Campers"][ed-1]["Estado"]["Cursando"]=False
                camp["Campers"][ed-1]["Estado"]["En proceso de ingreso"]=False
                camp["Campers"][ed-1]["Estado"]["Expulsado"]=False
                camp["Campers"][ed-1]["Estado"]["Graduado"]=True
                camp["Campers"][ed-1]["Estado"]["Inscrito"]=False
                camp["Campers"][ed-1]["Estado"]["Retirado"]=False
                bo=True
                guardarJSON(camp)
            elif estad==6:
                camp["Campers"][ed-1]["Estado"]["Aprobado"]=False
                camp["Campers"][ed-1]["Estado"]["Cursando"]=False
                camp["Campers"][ed-1]["Estado"]["En proceso de ingreso"]=False
                camp["Campers"][ed-1]["Estado"]["Expulsado"]=False
                camp["Campers"][ed-1]["Estado"]["Graduado"]=False
                camp["Campers"][ed-1]["Estado"]["Inscrito"]=True
                camp["Campers"][ed-1]["Estado"]["Retirado"]=False
                bo=True
                guardarJSON(camp)
            elif estad==7:
                camp["Campers"][ed-1]["Estado"]["Aprobado"]=False
                camp["Campers"][ed-1]["Estado"]["Cursando"]=False
                camp["Campers"][ed-1]["Estado"]["En proceso de ingreso"]=False
                camp["Campers"][ed-1]["Estado"]["Expulsado"]=False
                camp["Campers"][ed-1]["Estado"]["Graduado"]=False
                camp["Campers"][ed-1]["Estado"]["Inscrito"]=False
                camp["Campers"][ed-1]["Estado"]["Retirado"]=True
                bo=True
                guardarJSON(camp)
            else:
                print("El estado que ingreso es incorrecto")
                bo=False

def Eliminarcamper():
    Vercamper()
    print("Que camper quiere eliminar?")
    eli=int(input(": "))
    camp["Campers"][eli-1]["Estado"]["Aprobado"]=False
    camp["Campers"][eli-1]["Estado"]["Cursando"]=False
    camp["Campers"][eli-1]["Estado"]["En proceso de ingreso"]=False
    camp["Campers"][eli-1]["Estado"]["Expulsado"]=False
    camp["Campers"][eli-1]["Estado"]["Graduado"]=False
    camp["Campers"][eli-1]["Estado"]["Inscrito"]=False
    camp["Campers"][eli-1]["Estado"]["Retirado"]=True
    guardarJSON(camp)
    
def agregarnuevaruta():
    print("Ingrese el nombre de la nueva ruta")
    nvr=input(": ") 
    print("Cuantos skills tiene?")
    n=int(input(": "))
    rut["Rutas"][nvr]={}
    guardarJSO(rut)
    for i in range(0,n):
        print("Ingrese skill")
        ski=input(": ")
        rut["Rutas"][nvr][ski]=[]
        guardarJSO(rut)

def asignargrupo():
    for i in range(camp["Campers"]):
        if camp["Campers"][i]["Estado"]["Aprobado"]:
            if Hor["Horarios"]["HorarioA"]["P1"] < 33:
                Hor["Horarios"]["HorarioA"]["P1"].append({camp["Campers"][i]["ID"],
                                                          camp["Campers"][i]["nombre"],
                                                          camp["Campers"][i]["Apellido"],
                                                          Hor["Horarios"]["HorarioA"]["P1"]["NotaProyecto"],
                                                          Hor["Horarios"]["HorarioA"]["P1"]["NotaFiltro"],
                                                          Hor["Horarios"]["HorarioA"]["P1"]["NotaTrabajos"]
                                                          })

                camp["Campers"][i]["Estado"]["Aprobado"]=False
                camp["Campers"][i]["Estado"]["Cursando"]=True

    #match E:  #(Falta entrar al diccionario para elegir el estudiante a editar) 
     #   case 1:
      #      IDnuevo = int(input("Ingresa el nuevo ID: "))
       #     camp["ID"] = IDnuevo
        #    guardarJSON(camp)
##Crear una contrasena para el usuario trainner  
#pero igual solo cree el menu las funciones las implementamos en el main