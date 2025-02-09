import json
from Logic.Modulos import *
from Design.Menus import *

asignargrupo()
MenuPrincipal()
n=int(input(": "))
if n==3:
    MenuCamper()
    opc=int(input(": "))
    if opc==1:
        Aggcamper()