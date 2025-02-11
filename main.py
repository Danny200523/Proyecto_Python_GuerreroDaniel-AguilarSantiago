import json
from Logic.Coordinadora import *
from Design.Menus import *
camp=abrirJSON()
list=[]
bo=True
while bo==True:
    for i in range(len(camp["Campers"])):
        if camp["Campers"][i]["Estado"]["Cursando"]==True:
            list.append({"nombre":camp["Campers"][i]["nombre"],
                        "Estado":True})
    if len(list)<396:
        asignargrupo1()
    MenuPrincipal()
    n=int(input(": "))
    if n==3:
        Menucordinadora()
        opc=int(input(": "))
    if opc==1:
        Aggcamper()