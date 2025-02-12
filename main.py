import os
from Logic.Coordinadora import *
from Design.Menus import *
from Logic.Camper import *
from Logic.Trainer import *

cam=abrirJSON
asignarestruta()
while True:
    try:
        MenuPrincipal()  # Mostrar menú principal
        opc = int(input("Seleccione una opción: "))
        os.system("clear")

        if opc == 1:  # Opciones para Camper
            MenuCamper()
            opc = int(input("Seleccione una opción: "))
            if opc == 1:
                SiInscrito()
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
                elif x==2:
                    VerNotasNetCore()
                elif x==3:
                    VerNotasNodeJS()
                else:
                    break
            elif opc == 2:
                VerNotas()
            elif opc == 3:
                Vercamper()
            elif opc == 4:
                break  # Regresar al menú principal
        elif opc == 3:  # Opciones para Coordinadora
            Menucordinadora()
            opc = int(input("Seleccione una opción: "))
            if opc == 1:
                Aggcamper()
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
                break  # Regresar al menú principal
        elif opc == 4:
            print("GRACIAS POR USAR EL SISTEMA")
            break

    except ValueError:
        print("Error: Ingrese un número válido.")
    except Exception as e:
        print(f"Error inesperado: {e}")
