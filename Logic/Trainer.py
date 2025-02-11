#1. Para registrar el nivel de riesgo de un camper primero hay que registrar sus notas; para ello, se creará el archvio "Trainer.py" en el cuál el usuario tendrá acceso a las notas, ya sea crear o editar.
#NOTA: El trainner solo tendrá acceso a las notas de las rutas que existen y que además tiene asignadas. NO podrá crear nuevas (ROL Coordinadora)

import json 

def abrirJSO():
    dicFinal={}
    with open('Data/Rutas.json',"r") as openFile:
        dicFinal=json.load(openFile)
    return dicFinal

rutas={}
