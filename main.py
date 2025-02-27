import os
from Logic.Coordinadora import *
from Design.Menus import *
from Logic.Camper import *
from Logic.Trainer import *

cam=abrirJSON

while True:
    try:
        MenuPrincipal()
        asignarriesgo()  # Mostrar menú principal
        opc = int(input("Seleccione una opción: "))
        os.system("clear")

        if opc == 1:  # Opciones para Camper
            MenuCamper()
            opc = int(input("Seleccione una opción: "))
            if opc == 1:
                SiInscrito()
                vernota()
            elif opc == 2:
                MenuInscripcionCamper()
                Incripcion()
            elif opc == 3:
                break  # Regresar al menú principal
        elif opc == 2:  # Opciones para Trainer
            LogTrainer()
            MenuTrainer()
            opc = int(input("Seleccione una opción: "))
            if opc == 1:
                print("Elija de que ruta quiere ver las notas")
                print("(1). Java")
                print("(2). NodeJS")
                print("(3) NetCore")
                x=int(input(": "))
                if x==1:
                    VerNotasJava()
                    pass
                elif x==2:
                    VerNotasNetCore()
                    pass
                elif x==3:
                    VerNotasNodeJS()
                    pass
                else:
                    break
            elif opc == 2:
                EditarNotas()
            elif opc == 3:
                Vercamper()
            elif opc == 4:
                break  # Regresar al menú principal
        elif opc == 3:  # Opciones para Coordinadora
            Menucordinadora()
            opc = int(input("Seleccione una opción: "))
            if opc == 1:
                Aggcamper()
                asignarestruta()
            elif opc == 2:
                Editarcamper()
            elif opc == 3:
                Vercamper()
            elif opc == 4:
                Eliminarcamper()
            elif opc == 5:
                AggcamperCurso()
            elif opc == 6:
                agregarnuevaruta()
            elif opc == 7:
                MenuReportes()
                opc = int(input("Seleccione una opción: "))
                if opc == 1:
                    vercampersinscritos()
                elif opc == 2:
                    campersexameninicial()
                elif opc == 3:
                    vertrainers()
                elif opc == 4:
                    campersriesgoalto()
                elif opc == 5:
                    break
            elif opc == 8:
                break  # Regresar al menú principal
        elif opc == 4:
            print("GRACIAS POR USAR EL SISTEMA")
            break

    except ValueError:
        print("Error: Ingrese un número válido.")
    except Exception as e:
        print(f"Error inesperado: {e}")
