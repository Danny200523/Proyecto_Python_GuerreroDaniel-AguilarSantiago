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

def EditarnotaNodeJS():
    VerNotasJava()
    EditarNode=input("¿Qué skill desea editar?")
    NuevaNota = int(input("Ingrese la nueva nota: "))
    rutas["Rutas"]["NodeJS"][EditarNode]=NuevaNota
    abrirJSO()
    guardarJSO(rutas)
    
def EditarnotaNetCore():
    VerNotasJava()
    EditarNet=input("¿Qué skill desea editar?")
    NuevaNota = int(input("Ingrese la nueva nota: "))
    rutas["Rutas"]["NetCore"][EditarNet]=NuevaNota
    abrirJSO()
    guardarJSO(rutas)
