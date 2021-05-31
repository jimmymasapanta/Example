import base64
import getpass
import hashlib
import hmac
import pprint
import requests
import json
import csv

#PROGRAMA NUEVO
print ("ARUBA CENTRAL")
print ("Informacion de los clientes")
print ("Informacion de la lista de los AP")
print ("Ubicacion de los clientes")
print ("------------------------------")
print ("")
print ("-----ARUBA CENTAL INFORMACION---------")
access_token = input("Acess token= ")
print ("")

#INFORMACION DE LOS CLIENTES DEL AP 
url_aps = "apigw-uswest4.central.arubanetworks.com/monitoring/v1/clients/wireless"
url_aps_full= "https://" + url_aps + "?access_token=" + access_token
print ("Archivo 01")
print ("Obtener APS")
print (url_aps_full)
print ("-------------------")
result_aps = requests.get(url_aps_full)
json_parsed_aps = result_aps.json()
print("Informcion de las AP")
with open ("c:\Aru\\Formulario\\clientesAP1", "w")as out_json_aps:
    json.dump(json_parsed_aps, out_json_aps)
print (" >> file 'clientesAP1' creado correctamente")
print ("")

#FORMATO CSV DE LA INFORMACION

print("Archivo 2 ")
input("Presiona cualquier tecla para crear el archivo csv")
with open ("c:\Aru\\Formulario\\clientesAP2.csv", "w")as file_aps_csv:
    jsontocsv_aps = csv.writer(file_aps_csv)
    jsontocsv_aps.writerow(["GROUP", "Nombre Usuario", "AP MAC ADD", "SITE"])
    for item in json_parsed_aps['clients']:
        #jsontocsv_aps.writerow([item["group_name"], item["name"], item["macaddr"], item["model"], item["firware_version"], item["site"]])
        jsontocsv_aps.writerow([item["group_name"], item["name"], item["macaddr"], item["site"]])
        print(" file 'clientesAP2.csv' Archivo 2 creado corrrectamente")
        print("")
        exit_now = input("Presione [x] para sallir")
        if exit_now.upper() == "x":
            print("Fin del proceso")
            exit()
       




            













        



































