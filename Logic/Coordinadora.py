import json
import random
import datetime
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

def abrirJ():
    dicFinal={}
    with open("./Data/Trainers.json","r") as openFile:
        dicFinal=json.load(openFile)
    return dicFinal

def guardarJ(dic):
    with open("../Data/Trainers.json",'w') as outFile:
        json.dump(dic,outFile)

train={}
camp={}
rut={}
Hor={}
camp=abrirJSON()
rut=abrirJSO()
Hor=abrirJS()
train=abrirJ()

#FUNCION TIEMPO (Para llamr después)
fecha_inicio = datetime.date(2025,2,14)
fecha_fin = fecha_inicio + datetime.timedelta(days=10 * 30)  # Aproximadamente 10 meses
##FUNCIONES COORDINADORA
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
                            "Curso":"",
                            "Riesgo": "",
                            "notainicial": random.randint(0, 100),
                            "fechaInicio": fecha_inicio,
                            "fechaFin": fecha_fin})
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
        camp["Campers"][E-1]["ID"]=identi
    elif ed==2:
        print("Ingrese el nuevo Nombre(Nombres)")
        name=input(": ")
        camp["Campers"][E-1]["nombre"]=name
    elif ed==3:
        print("Ingrese el nuevo Apellido(Apellidos)")
        apll=input(": ")
        camp["Campers"][E-1]["apellido"]=apll
    elif ed==4:
        print("Ingrese la nueva direccion")
        direc=input(": ")
        camp["Campers"][E-1]["direccion"]=direc
    elif ed==5:
        print("Ingrese el nuevo Nombre del acudiente(Nombres)")
        acud=input(": ")
        camp["Campers"][E-1]["nombre"]=acud
    elif ed==6:
        print("Ingrese el nuevo #Celular")
        celul=input(": ")
        camp["Campers"][E-1]["#celular"]=celul
    elif ed==8:
        print("Ingrese el nuevo curso")
        cur=input(": ")
        camp["Campers"][E-1]["Curso"]=cur
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
                camp["Campers"][E-1]["Estado"]["Aprobado"]=True
                camp["Campers"][E-1]["Estado"]["Cursando"]=False
                camp["Campers"][E-1]["Estado"]["En proceso de ingreso"]=False
                camp["Campers"][E-1]["Estado"]["Expulsado"]=False
                camp["Campers"][E-1]["Estado"]["Graduado"]=False
                camp["Campers"][E-1]["Estado"]["Inscrito"]=False
                camp["Campers"][E-1]["Estado"]["Retirado"]=False
                bo=True
                guardarJSON(camp)
            elif estad==2:
                camp["Campers"][E-1]["Estado"]["Aprobado"]=False
                camp["Campers"][E-1]["Estado"]["Cursando"]=True
                camp["Campers"][E-1]["Estado"]["En proceso de ingreso"]=False
                camp["Campers"][E-1]["Estado"]["Expulsado"]=False
                camp["Campers"][E-1]["Estado"]["Graduado"]=False
                camp["Campers"][E-1]["Estado"]["Inscrito"]=False
                camp["Campers"][E-1]["Estado"]["Retirado"]=False
                bo=True
                guardarJSON(camp)
            elif estad==3:
                camp["Campers"][E-1]["Estado"]["Aprobado"]=False
                camp["Campers"][E-1]["Estado"]["Cursando"]=False
                camp["Campers"][E-1]["Estado"]["En proceso de ingreso"]=True
                camp["Campers"][E-1]["Estado"]["Expulsado"]=False
                camp["Campers"][E-1]["Estado"]["Graduado"]=False
                camp["Campers"][E-1]["Estado"]["Inscrito"]=False
                camp["Campers"][E-1]["Estado"]["Retirado"]=False
                bo=True
                guardarJSON(camp)
            elif estad==4:
                camp["Campers"][E-1]["Estado"]["Aprobado"]=False
                camp["Campers"][E-1]["Estado"]["Cursando"]=False
                camp["Campers"][E-1]["Estado"]["En proceso de ingreso"]=False
                camp["Campers"][E-1]["Estado"]["Expulsado"]=True
                camp["Campers"][E-1]["Estado"]["Graduado"]=False
                camp["Campers"][E-1]["Estado"]["Inscrito"]=False
                camp["Campers"][E-1]["Estado"]["Retirado"]=False
                bo=True
                guardarJSON(camp)
            elif estad==5:
                camp["Campers"][E-1]["Estado"]["Aprobado"]=False
                camp["Campers"][E-1]["Estado"]["Cursando"]=False
                camp["Campers"][E-1]["Estado"]["En proceso de ingreso"]=False
                camp["Campers"][E-1]["Estado"]["Expulsado"]=False
                camp["Campers"][E-1]["Estado"]["Graduado"]=True
                camp["Campers"][E-1]["Estado"]["Inscrito"]=False
                camp["Campers"][E-1]["Estado"]["Retirado"]=False
                bo=True
                guardarJSON(camp)
            elif estad==6:
                camp["Campers"][E-1]["Estado"]["Aprobado"]=False
                camp["Campers"][E-1]["Estado"]["Cursando"]=False
                camp["Campers"][E-1]["Estado"]["En proceso de ingreso"]=False
                camp["Campers"][E-1]["Estado"]["Expulsado"]=False
                camp["Campers"][E-1]["Estado"]["Graduado"]=False
                camp["Campers"][E-1]["Estado"]["Inscrito"]=True
                camp["Campers"][E-1]["Estado"]["Retirado"]=False
                bo=True
                guardarJSON(camp)
            elif estad==7:
                camp["Campers"][E-1]["Estado"]["Aprobado"]=False
                camp["Campers"][E-1]["Estado"]["Cursando"]=False
                camp["Campers"][E-1]["Estado"]["En proceso de ingreso"]=False
                camp["Campers"][E-1]["Estado"]["Expulsado"]=False
                camp["Campers"][E-1]["Estado"]["Graduado"]=False
                camp["Campers"][E-1]["Estado"]["Inscrito"]=False
                camp["Campers"][E-1]["Estado"]["Retirado"]=True
                bo=True
                guardarJSON(camp)
            else:
                print("El estado que ingreso es incorrecto")
                bo=False

def editarnota():
    Vercamper()
    el = input("¿A cuál estudiante le va a cambiar la nota?")
    notanueva = int(input("¿Cuál es la nueva nota?"))
    camp["Campers"][el-1]["notainicial"]=notanueva

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
    for i in range(len(camp["Campers"])):
        if camp["Campers"][i]["Estado"]["Aprobado"]:
            if len(Hor["Horarios"]["HorarioA"]["P1"]) < 33:
                Hor["Horarios"]["HorarioA"]["P1"].append({"ID":camp["Campers"][i]["ID"],
                                                            "nombre":camp["Campers"][i]["nombre"],
                                                            "apellido":camp["Campers"][i]["apellido"]
                                                            })
                camp["Campers"][i]["Estado"]["Aprobado"]=False
                camp["Campers"][i]["Estado"]["Cursando"]=True
                guardarJS(Hor)
                guardarJSON(camp)
            elif len(Hor["Horarios"]["HorarioB"]["P2"]) < 33:
                    Hor["Horarios"]["HorarioB"]["P2"].append({"ID":camp["Campers"][i]["ID"],
                                                                "nombre":camp["Campers"][i]["nombre"],
                                                                "apellido":camp["Campers"][i]["apellido"]
                                                                })
                    camp["Campers"][i]["Estado"]["Aprobado"]=False
                    camp["Campers"][i]["Estado"]["Cursando"]=True
                    guardarJS(Hor)
                    guardarJSON(camp)
            elif len(Hor["Horarios"]["HorarioC"]["P3"]) < 33:
                    Hor["Horarios"]["HorarioC"]["P3"].append({"ID":camp["Campers"][i]["ID"],
                                                                "nombre":camp["Campers"][i]["nombre"],
                                                                "apellido":camp["Campers"][i]["apellido"]
                                                                })
                    camp["Campers"][i]["Estado"]["Aprobado"]=False
                    camp["Campers"][i]["Estado"]["Cursando"]=True
                    guardarJS(Hor)
                    guardarJSON(camp)
            elif len(Hor["Horarios"]["HorarioD"]["P4"]) < 33:
                    Hor["Horarios"]["HorarioD"]["P4"].append({"ID":camp["Campers"][i]["ID"],
                                                                "nombre":camp["Campers"][i]["nombre"],
                                                                "apellido":camp["Campers"][i]["apellido"]
                                                                })
                    camp["Campers"][i]["Estado"]["Aprobado"]=False
                    camp["Campers"][i]["Estado"]["Cursando"]=True
                    guardarJS(Hor)
                    guardarJSON(camp)
            elif len(Hor["Horarios"]["HorarioA"]["M1"]) < 33:
                Hor["Horarios"]["HorarioA"]["M1"].append({"ID":camp["Campers"][i]["ID"],
                                                            "nombre":camp["Campers"][i]["nombre"],
                                                            "apellido":camp["Campers"][i]["apellido"]
                                                            })
                camp["Campers"][i]["Estado"]["Aprobado"]=False
                camp["Campers"][i]["Estado"]["Cursando"]=True
                guardarJS(Hor)
                guardarJSON(camp)
            elif len(Hor["Horarios"]["HorarioB"]["M2"]) < 33:
                Hor["Horarios"]["HorarioB"]["M2"].append({"ID":camp["Campers"][i]["ID"],
                                                                "nombre":camp["Campers"][i]["nombre"],
                                                                "apellido":camp["Campers"][i]["apellido"]
                                                            })
                camp["Campers"][i]["Estado"]["Aprobado"]=False
                camp["Campers"][i]["Estado"]["Cursando"]=True
                guardarJS(Hor)
                guardarJSON(camp)
            elif len(Hor["Horarios"]["HorarioB"]["M2"]) < 33:
                Hor["Horarios"]["HorarioAC"]["M2"].append({"ID":camp["Campers"][i]["ID"],
                                                                "nombre":camp["Campers"][i]["nombre"],
                                                                "apellido":camp["Campers"][i]["apellido"]
                                                            })
                camp["Campers"][i]["Estado"]["Aprobado"]=False
                camp["Campers"][i]["Estado"]["Cursando"]=True
                guardarJS(Hor)
                guardarJSON(camp)
            elif len(Hor["Horarios"]["HorarioD"]["M4"]) < 33:
                Hor["Horarios"]["HorarioD"]["M4"].append({"ID":camp["Campers"][i]["ID"],
                                                                "nombre":camp["Campers"][i]["nombre"],
                                                                "apellido":camp["Campers"][i]["apellido"]
                                                            })
                camp["Campers"][i]["Estado"]["Aprobado"]=False
                camp["Campers"][i]["Estado"]["Cursando"]=True
                guardarJS(Hor)
                guardarJSON(camp)
            elif len(Hor["Horarios"]["HorarioA"]["J1"]) < 33:
                Hor["Horarios"]["HorarioA"]["J1"].append({"ID":camp["Campers"][i]["ID"],
                                                                "nombre":camp["Campers"][i]["nombre"],
                                                                "apellido":camp["Campers"][i]["apellido"]
                                                            })
                camp["Campers"][i]["Estado"]["Aprobado"]=False
                camp["Campers"][i]["Estado"]["Cursando"]=True
                guardarJS(Hor)
                guardarJSON(camp)
            elif len(Hor["Horarios"]["HorarioB"]["J2"]) < 33:
                Hor["Horarios"]["HorarioB"]["J2"].append({"ID":camp["Campers"][i]["ID"],
                                                                "nombre":camp["Campers"][i]["nombre"],
                                                                "apellido":camp["Campers"][i]["apellido"]
                                                            })
                camp["Campers"][i]["Estado"]["Aprobado"]=False
                camp["Campers"][i]["Estado"]["Cursando"]=True
                guardarJS(Hor)
                guardarJSON(camp)
            elif len(Hor["Horarios"]["HorarioC"]["J3"]) < 33:
                Hor["Horarios"]["HorarioC"]["J3"].append({"ID":camp["Campers"][i]["ID"],
                                                                "nombre":camp["Campers"][i]["nombre"],
                                                                "apellido":camp["Campers"][i]["apellido"]
                                                            })
                camp["Campers"][i]["Estado"]["Aprobado"]=False
                camp["Campers"][i]["Estado"]["Cursando"]=True
                guardarJS(Hor)
                guardarJSON(camp)
            elif len(Hor["Horarios"]["HorarioD"]["J4"]) < 33:
                Hor["Horarios"]["HorarioD"]["J4"].append({"ID":camp["Campers"][i]["ID"],
                                                                "nombre":camp["Campers"][i]["nombre"],
                                                                "apellido":camp["Campers"][i]["apellido"]
                                                            })
                camp["Campers"][i]["Estado"]["Aprobado"]=False
                camp["Campers"][i]["Estado"]["Cursando"]=True
                guardarJS(Hor)
                guardarJSON(camp)

def asignarestruta():
    """
    Asigna rutas a los estudiantes en base a su horario.
    """
    # Mapear prefijos a rutas
    rutas = {"P": "Java", "M": "NodeJS", "J": "NetCore"}
    
    # Verificar si los datos de horarios y rutas existen
    if "Horarios" not in Hor or "Rutas" not in rut:
        print("Error: Datos de horarios o rutas no disponibles.")
        return
    
    # Obtener horarios dinámicamente
    horarios_disponibles = Hor.get("Horarios", {})
    
    for tipo_horario, horarios in horarios_disponibles.items():
        for horario, estudiantes in horarios.items():
            ruta = rutas.get(horario[0], "Java")  # Ruta según el prefijo
            
            if ruta not in rut["Rutas"]:
                continue  # Si la ruta no existe, omitir
            
            # Asignar estudiantes a la ruta correspondiente
            for estudiante in estudiantes:
                datos_estudiante = {
                    "nombre": estudiante.get("nombre", "Desconocido"),
                    "ID": estudiante.get("ID", "N/A"),
                    "Notas": {"notaProyecto": "", "notaFiltro": "", "notaTrabajos": ""}
                }
                
                # Agregar el estudiante a cada módulo de la ruta
                for modulo in rut["Rutas"].get(ruta, {}):
                    rut["Rutas"][ruta][modulo].append(datos_estudiante)
    
    guardarJSO(rut)  # Guardar los cambios
    print("Asignación de rutas completada correctamente.")

def asignacionnotainical():
    Vercamper()
    print("A que estudiante le quiere asignar la nota del examen de ingreso")
    x=int(input(": "))
    print("Ingrese la nueva nota")
    nt=int(input(": "))
    camp["Campers"][x-1]["notainicial"]=nt

def AggcamperCurso():


    Vercamper() 
    print("A qué estudiante desea agregar al curso?") 
    estudiante = int(input(": ")) 
    print(
         '''A que grupo lo quiere agregar?
         1. P1
         2. P2
         3. P3
         4. P4
         5. M1
         6. M2
         7. M3
         8. M4
         9. J1
         10. J2
         11. J3
         12. J4
         ''')
    curso=int(input(": "))
    if curso==1:
            if len(Hor["Horarios"]["HorarioA"]["P1"]) < 33:
                Hor["Horarios"]["HorarioA"]["P1"].append({"ID":camp["Campers"][estudiante-1]["ID"],
                                                            "nombre":camp["Campers"][estudiante-1]["nombre"],
                                                            "apellido":camp["Campers"][estudiante-1]["apellido"]
                                                            })
                guardarJS(Hor)
    elif curso==2:
        if len(Hor["Horarios"]["HorarioA"]["P2"]) < 33:
            Hor["Horarios"]["HorarioA"]["P2"].append({"ID":camp["Campers"][estudiante-1]["ID"],
                                                            "nombre":camp["Campers"][estudiante-1]["nombre"],
                                                            "apellido":camp["Campers"][estudiante-1]["apellido"]
                                                            })
            guardarJS(Hor)

def vercampersinscritos():
    for i in range(len(camp["Campers"])):
        if camp["Campers"][i]["Estado"]["Inscrito"]:
            print("ID: ",camp["Campers"][i]["ID"])
            print("Nombre: ",camp["Campers"][i]["nombre"])
            print("Apellido: ",camp["Campers"][i]["apellido"])
            print("Direccion: ",camp["Campers"][i]["direccion"])
            print("Acudiente: ",camp["Campers"][i]["acudientes"])
            print("#Celular: ",camp["Campers"][i]["#celular"])
            print("Estado: ",camp["Campers"][i]["Estado"])

def campersexameninicial():
    for i in range(len(camp["Campers"])):
        if camp["Campers"][i]["notainicial"]>=7:
            print("ID: ",camp["Campers"][i]["ID"])
            print("Nombre: ",camp["Campers"][i]["nombre"])
            print("Apellido: ",camp["Campers"][i]["apellido"])
            print("Direccion: ",camp["Campers"][i]["direccion"])
            print("Acudiente: ",camp["Campers"][i]["acudientes"])
            print("#Celular: ",camp["Campers"][i]["#celular"])
            print("Estado: ",camp["Campers"][i]["Estado"])
            print("Nota examen inicial: ",camp["Campers"][i]["notainicial"])

def vertrainers():
    for i in range(len(train["Trainers"])):
        print("Nombre: ",train["Trainers"][i]["nombre"])

def campersriesgoalto():
    for i in range(len(camp["Campers"])):
        if camp["Campers"][i]["Riesgo"] == "Alto":
            print("ID: ",camp["Campers"][i]["ID"])
            print("Nombre: ",camp["Campers"][i]["nombre"])
            print("Apellido: ",camp["Campers"][i]["apellido"])
            print("Estado: ",camp["Campers"][i]["Estado"])
            print("Riesgo: ",camp["Campers"][i]["Riesgo"])

def asignarriesgo():
    for i in range(len(rut["Rutas"]["Java"]["Intro"])):
        if rut["Rutas"]["Java"]["Intro"][i]["Notas"]["notaFinal"] < 7:
            camp["Campers"][i]["Riesgo"] = "Alto"
        elif rut["Rutas"]["Java"]["Intro"][i]["Notas"]["notaFinal"] < 8:
            camp["Campers"][i]["Riesgo"] = "Medio"
        else:  
            camp["Campers"][i]["Riesgo"] = "Bajo"
    for i in range(len(rut["Rutas"]["NodeJS"]["Intro"])):
        if rut["Rutas"]["NodeJS"]["Intro"][i]["Notas"]["notaFinal"] < 7:
            camp["Campers"][i]["Riesgo"] = "Alto"
        elif rut["Rutas"]["NodeJS"]["Intro"][i]["Notas"]["notaFinal"] < 8:
            camp["Campers"][i]["Riesgo"] = "Medio"
        else:
            camp["Campers"][i]["Riesgo"] = "Bajo"
    for i in range(len(rut["Rutas"]["NetCore"]["Intro"])):
        if rut["Rutas"]["NetCore"]["Intro"][i]["Notas"]["notaFinal"] < 7:
            camp["Campers"][i]["Riesgo"] = "Alto"
        elif rut["Rutas"]["NetCore"]["Intro"][i]["Notas"]["notaFinal"] < 8:
            camp["Campers"][i]["Riesgo"] = "Medio"
        else:
            camp["Campers"][i]["Riesgo"] = "Bajo"
    guardarJSON(camp)
##Crear una contrasena para el usuario trainner  
#pero igual solo cree el menu las funciones las implementamos en el main