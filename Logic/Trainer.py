#1. Para registrar el nivel de riesgo de un camper primero hay que registrar sus notas; para ello, se creará el archvio "Trainer.py" en el cuál el usuario tendrá acceso a las notas, ya sea crear o editar.
#NOTA: El trainner solo tendrá acceso a las notas de las rutas que existen y que además tiene asignadas. NO podrá crear nuevas (ROL Coordinadora)

import json 

def abrirJSO():
    dicFinal={}
    with open('../Data/Rutas.json',"r") as openFile:
        dicFinal=json.load(openFile)
    return dicFinal

rutas = {}
rutas=abrirJSO()

def guardarJSO(dic):
    with open("../Data/Rutas.json",'w') as outFile:
        json.dump(dic,outFile)


####################################################################################################################################################################################################333
## RECORDAR PEDIR 3 NOTAS(FILTRO, PROYECTO Y OTROS) DEF CALCULAROROMEDIO Y EVALUAR SI RIESGO==TRUE
##OPCIONES MENU

''''
=   1. Ver notas         =
=   2. Editar notas      =
=   3. Ver estudiantes   =
'''
'''
Trainer = "Pedro"
print(f"Bievenido {Trainer}")
print("""
====== ¿Qué desea hacer? ======
=   1. Ver notas         =
=   2. Editar notas      =
=   3. Ver estudiantes   =
""")
'''
def VerRutas():
    print("Java")
    print("NodeJS")
    print("NetCore")
    
## FALTA FUN. VERESTUDIANTE
def verEstudiantes():
    SelRuta = input("Ingrese qué ruta tiene su grupo: ")
    SelecSkill = input("¿Qué skill desea ver?")
    for i in range(len(rutas["Rutas"][SelRuta][SelecSkill])):
        print("\nNombre estudiante: #",i+1, rutas["Rutas"][SelRuta][SelecSkill][i]["nombre"])
        print("Identificacion: ", rutas["Rutas"][SelRuta][SelecSkill][i]["ID"])
        print("========================================================================")


def EstudiantesNotas():
    SelRuta = input("Ingrese qué ruta tiene su grupo: ")
    SelecSkill = input("¿Qué skill desea editar?")
    for i in range(len(rutas["Rutas"][SelRuta][SelecSkill])):
        print("\nNombre estudiante: #",i+1, rutas["Rutas"][SelRuta][SelecSkill][i]["nombre"])
        print("Identificacion: ", rutas["Rutas"][SelRuta][SelecSkill][i]["ID"])
        print("========================================================================")
        #Llamar Estudiante
    SelEstudiante = int(input("Ingrese el estudiante que desea ingresar: #"))
    print("\nNombre estudiante: #", SelEstudiante, rutas["Rutas"][SelRuta][SelecSkill][SelEstudiante-1]["nombre"])
    print("Identificacion: ", rutas["Rutas"][SelRuta][SelecSkill][SelEstudiante-1]["ID"])
    print("1. Nota Proyecto: ", rutas["Rutas"][SelRuta][SelecSkill][SelEstudiante-1]["Notas"]["notaProyecto"])
    print("2 Nota Filtro: ", rutas["Rutas"][SelRuta][SelecSkill][SelEstudiante-1]["Notas"]["notaFiltro"])
    print("3. Nota Trabajos: ", rutas["Rutas"][SelRuta][SelecSkill][SelEstudiante-1]["Notas"]["notaTrabajos"])
    guardarJSO(rutas)
    ##Seleccionar Nota a Editar
    notaSeleccionada = validarOpcion("Seleccione el numero de la nota que va a editar",1, 3)
    # Verificar que ruta se ha seleccionado
    if notaSeleccionada == 1:
        rutas["Rutas"][SelRuta][SelecSkill][SelEstudiante-1]["Notas"]["notaProyecto"] = int(input("Ingrese la nueva nota: "))
    elif notaSeleccionada == 2:
        rutas["Rutas"][SelRuta][SelecSkill][SelEstudiante-1]["Notas"]["notaFiltro"] = int(input("Ingrese la nueva nota: "))
    elif notaSeleccionada == 3:
        rutas["Rutas"][SelRuta][SelecSkill][SelEstudiante-1]["Notas"]["notaTrabajos"] = int(input("Ingrese la nueva nota: "))
    guardarJSO(rutas)
    ##Falta promediar notas

# Funcion para validar una opcion entre un numero y otro
def validarOpcion(message, initialValue, finalValue):
    # Bucle inicial
    while True:
        #Pedimos la opcion al usuario
        option = int(input(message))

        # Validamos si la opcion esta entre el rango escogido
        if (option >= initialValue and option <= finalValue):
            return option # Retornamos la opcion si está entre el rango seleccionado
        else:
            # Si el usuario escoge una opcion incorrecta repetimos el bucle
            print(f"Escoge un numero entre {initialValue} y {finalValue}")


#P  
def EditarNotas():
    verEstudiantes()
    SelRuta = input("Ingrese qué ruta tiene su grupo: ")
    print(rutas["Rutas"][SelRuta])
    SelecSkill = input("¿Qué skill desea editar?")
    NuevaNota = int(input("Ingrese la nueva nota: "))
    rutas["Rutas"][SelRuta][SelecSkill]
    guardarJSO()















# # def VerNotasJava():
# #         '''Ruta JAVA'''
# #         print("Intro:",rutas["Rutas"]["Java"]["Intro"])
# #         print("Python:",rutas["Rutas"]["Java"]["Python"])
# #         print("Html/Css:",rutas["Rutas"]["Java"]["Html/css"])
# #         print("Scrum:",rutas["Rutas"]["Java"]["Scrum"])
# #         print("Git:",rutas["Rutas"]["Java"]["Git"])
# #         print("Javascript:",rutas["Rutas"]["Java"]["Javascript"])
# #         print("IntroBack:",rutas["Rutas"]["Java"]["IntroBack"])
# #         print("Introbbdd:",rutas["Rutas"]["Java"]["IntroBBDD"])
# #         print("MySQL:",rutas["Rutas"]["Java"]["MySQL"]) #1115, 431, 
# #         print("Java:",rutas["Rutas"]["Java"]["Java"])
# #         print("PostgreSQL:",rutas["Rutas"]["Java"]["PostgreSQL"])
# #         print("SpringBoot:",rutas["Rutas"]["Java"]["SpringBoot"])

# # def VerNotasNodeJS():
# #     print("Intro:",rutas["Rutas"]["Java"]["Intro"])
# #     print("Python:",rutas["Rutas"]["Java"]["Python"])
# #     print("Html/Css:",rutas["Rutas"]["Java"]["Html/css"])
# #     print("Scrum:",rutas["Rutas"]["Java"]["Scrum"])
# #     print("Git:",rutas["Rutas"]["Java"]["Git"])
# #     print("Javascript:",rutas["Rutas"]["Java"]["Javascript"])
# #     print("IntroBack:",rutas["Rutas"]["Java"]["IntroBack"])
# #     print("Introbbdd:",rutas["Rutas"]["Java"]["IntroBBDD"])
# #     print("MangoDB:",rutas["Rutas"]["Java"]["MangoDB"]) 
# #     print("Javascript 2:",rutas["Rutas"]["Java"]["Javascript2"])
# #     print("MySQL:",rutas["Rutas"]["Java"]["MySQL"])
# #     print("Express:",rutas["Rutas"]["Java"]["Express"])

# # def VerNotasNetCore():
# #     print("Intro:",rutas["Rutas"]["Java"]["Intro"])
# #     print("Python:",rutas["Rutas"]["Java"]["Python"])
# #     print("Html/Css:",rutas["Rutas"]["Java"]["Html/css"])
# #     print("Scrum:",rutas["Rutas"]["Java"]["Scrum"])
# #     print("Git:",rutas["Rutas"]["Java"]["Git"])
# #     print("Javascript:",rutas["Rutas"]["Java"]["Javascript"])
# #     print("IntroBack:",rutas["Rutas"]["Java"]["IntroBack"])
# #     print("Introbbdd:",rutas["Rutas"]["Java"]["IntroBBDD"])
# #     print("MySQL:",rutas["Rutas"]["Java"]["MySQL"])  
# #     print("C##:",rutas["Rutas"]["Java"]["C##"])
# #     print("PostgreSQL:",rutas["Rutas"]["Java"]["PostgreSQL"])
# #     print(".NetCore:",rutas["Rutas"]["Java"][".NetCore"])

# # def EditarnotaJava():
# #     VerNotasJava()
# #     EditarJava=input("¿Qué skill desea editar?")
# #     NuevaNota = int(input("Ingrese la nueva nota: "))
# #     rutas["Rutas"]["Java"][EditarJava]=NuevaNota
# #     abrirJSO()
# #     guardarJSO(rutas)

# # def EditarnotaNodeJS():
# #     VerNotasJava()
# #     EditarNode=input("¿Qué skill desea editar?")
# #     NuevaNota = int(input("Ingrese la nueva nota: "))
# #     rutas["Rutas"]["NodeJS"][EditarNode]=NuevaNota
# #     abrirJSO()
# #     guardarJSO(rutas)
    
# # def EditarnotaNetCore():
# #     VerNotasJava()
# #     EditarNet=input("¿Qué skill desea editar?")
# #     NuevaNota = int(input("Ingrese la nueva nota: "))
# #     rutas["Rutas"]["NetCore"][EditarNet]=NuevaNota
# #     abrirJSO()
# #     guardarJSO(rutas)

