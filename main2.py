import json
def abrirJSON():
    dicFinal={}
    with open('./Data/campers.json',"r") as openFile:
        dicFinal=json.load(openFile)
    return dicFinal

def guardarJSON(dic):
    with open("./Data/campers.json",'w') as outFile:
        json.dump(dic,outFile)

camp=abrirJSON()
cursando=camp["Campers"]["Estado"]["Cursando"].count("true")
print(cursando,"1")