import json
from Logic.Coordinadora import *
from Design.Menus import *
camp=abrirJSON
list=[]
bo=True
while bo==True:
    for i in range(len(camp["Campers"])):
        print("")
    MenuPrincipal()
    n=int(input(": "))
    if n==3:
        MenuCamper()
        opc=int(input(": "))
    if opc==1:
        Aggcamper()