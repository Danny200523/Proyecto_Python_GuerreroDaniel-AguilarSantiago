#1. Para registrar el nivel de riesgo de un camper primero hay que registrar sus notas; para ello, se creará el archvio "Trainer.py" en el cuál el usuario tendrá acceso a las notas, ya sea crear o editar.
#NOTA: El trainner solo tendrá acceso a las notas de las rutas que existen y que además tiene asignadas. NO podrá crear nuevas (ROL Coordinadora)

import json 

def abrirJSO():
    dicFinal={}
    with open('Data/Rutas.json',"r") as openFile:
        dicFinal=json.load(openFile)
    return dicFinal

rutas=abrirJSO()

def guardarJSO(dic):
    with open("Data/Rutas.json",'w') as outFile:
        json.dump(dic,outFile)


####################################################################################################################################################################################################333
## RECORDAR PEDIR 3 NOTAS(FILTRO, PROYECTO Y OTROS) DEF CALCULAROROMEDIO Y EVALUAR SI RIESGO==TRUE
##OPCIONES MENU

''''
=   1. Ver notas         =
=   2. Editar notas      =
=   3. Ver estudiantes   =
'''

def VerNotasJava():
        '''Ruta JAVA'''
        print("Intro:",rutas["Rutas"]["Java"]["Intro"])
        print("Python:",rutas["Rutas"]["Java"]["Python"])
        print("Html/Css:",rutas["Rutas"]["Java"]["Html/css"])
        print("Scrum:",rutas["Rutas"]["Java"]["Scrum"])
        print("Git:",rutas["Rutas"]["Java"]["Git"])
        print("Javascript:",rutas["Rutas"]["Java"]["Javascript"])
        print("IntroBack:",rutas["Rutas"]["Java"]["IntroBack"])
        print("Introbbdd:",rutas["Rutas"]["Java"]["IntroBBDD"])
        print("MySQL:",rutas["Rutas"]["Java"]["MySQL"]) #1115, 431, 
        print("Java:",rutas["Rutas"]["Java"]["Java"])
        print("PostgreSQL:",rutas["Rutas"]["Java"]["PostgreSQL"])
        print("SpringBoot:",rutas["Rutas"]["Java"]["SpringBoot"])

def VerNotasNodeJS():
    print("Intro:",rutas["Rutas"]["Java"]["Intro"])
    print("Python:",rutas["Rutas"]["Java"]["Python"])
    print("Html/Css:",rutas["Rutas"]["Java"]["Html/css"])
    print("Scrum:",rutas["Rutas"]["Java"]["Scrum"])
    print("Git:",rutas["Rutas"]["Java"]["Git"])
    print("Javascript:",rutas["Rutas"]["Java"]["Javascript"])
    print("IntroBack:",rutas["Rutas"]["Java"]["IntroBack"])
    print("Introbbdd:",rutas["Rutas"]["Java"]["IntroBBDD"])
    print("MangoDB:",rutas["Rutas"]["Java"]["MangoDB"]) 
    print("Javascript 2:",rutas["Rutas"]["Java"]["Javascript2"])
    print("MySQL:",rutas["Rutas"]["Java"]["MySQL"])
    print("Express:",rutas["Rutas"]["Java"]["Express"])

def VerNotasNetCore():
    print("Intro:",rutas["Rutas"]["Java"]["Intro"])
    print("Python:",rutas["Rutas"]["Java"]["Python"])
    print("Html/Css:",rutas["Rutas"]["Java"]["Html/css"])
    print("Scrum:",rutas["Rutas"]["Java"]["Scrum"])
    print("Git:",rutas["Rutas"]["Java"]["Git"])
    print("Javascript:",rutas["Rutas"]["Java"]["Javascript"])
    print("IntroBack:",rutas["Rutas"]["Java"]["IntroBack"])
    print("Introbbdd:",rutas["Rutas"]["Java"]["IntroBBDD"])
    print("MySQL:",rutas["Rutas"]["Java"]["MySQL"])  
    print("C##:",rutas["Rutas"]["Java"]["C##"])
    print("PostgreSQL:",rutas["Rutas"]["Java"]["PostgreSQL"])
    print(".NetCore:",rutas["Rutas"]["Java"][".NetCore"])

def EditarnotaJava():
    VerNotasJava()
    EditarJava=input("¿Qué skill desea editar?")
    NuevaNota = int(input("Ingrese la nueva nota: "))
    rutas["Rutas"]["Java"][EditarJava]=NuevaNota
    abrirJSO()
    guardarJSO(rutas)


EditarnotaJava()

'''para que es el [f"EditarJava"]'''
#Porque quería que EditarJava fuera tipo ud pone Python entonces 
# #se va a Python pero no funciona :c
'''pero no seria digamos un estudiante que el elija y luego el campo de la nota que ud quiere editar?'''
#Como así
'''osea, porque tiene que entrar a lo que quiere editar que es su defecto seria algo asi rutas
["Rutas"]["Java"]["Intro"]["estudiante-1"]["NotaFiltro"]=NuevaNota'''
#Genio Bro
#Me faltaba era meterme a Java jjajaja
#Es que lo que ud dice sí pero me confundí porque había puesto una lista, entonces sería poner .append
'''no porque append es para agregar y no para editar, entonces seria con el igual que puse en el comment de arriba'''
# o sea a cada ruta le metemos otros 3 dics? Filtro, proyecto y Otros? Pa pedirle a GPT
'''mentira, porque eso lo asigna esta funcion'''
#Porque más bien el Trainer editaría la nota final
'''
def asignarestruta():
    for i in range(len(camp)):
        if camp["Campers"][i]["Estado"]["Cursando"]==True:
            x=camp["Campers"][i]["ID"]
            if Hor["Horarios"]["HorarioA"]["P1"]["ID"]==x:
                rut["Rutas"]["Java"]["Intro"].append({"nombre":Hor["Horarios"]["HorarioA"]["P1"]["nombre"],
                                                      "ID":Hor["Horarios"]["HorarioA"]["P1"]["ID"],
                                                      "Notas":{"notaProyecto":"",
                                                               "notaFiltro":"",
                                                               "notaTrabajos":""}})
                rut["Rutas"]["Java"]["Python"].append({"nombre":Hor["Horarios"]["HorarioA"]["P1"]["nombre"],
                                                      "ID":Hor["Horarios"]["HorarioA"]["P1"]["ID"],
                                                      "Notas":{"notaProyecto":"",
                                                               "notaFiltro":"",
                                                               "notaTrabajos":""}})
                rut["Rutas"]["Java"]["Html/css"].append({"nombre":Hor["Horarios"]["HorarioA"]["P1"]["nombre"],
                                                      "ID":Hor["Horarios"]["HorarioA"]["P1"]["ID"],
                                                      "Notas":{"notaProyecto":"",
                                                               "notaFiltro":"",
                                                               "notaTrabajos":""}})

es que si dejamos que solo pueda editar la final nos jode todo lit
nokas ya la meto en el main y ud lo ejecuta y salio
ejecute el main a ver que pex
'''
#Es verdad
#Entonces Pasamos esa función para acá? Para poder actualizar d1 y que el
#Trainer le meta a ver
