nombre = input("¿Cuál es tu nombre?")
print ("Hola ",nombre,"¿tienes alguna palabra juvenil que no entiendas? Escribela a continuación: ")
diccionario_memes = {
     "LOL": "una respuesta a algo gracioso",
     "CRINGE": "algo raro o embarazoso",
     "ROFL": "una respuesta a una broma",
     "SHEESH": "ligera desaprobación",
     "CREEPY": "aterrador, siniestro",
     "AGGRO": "ponerse agresivo/enojado",
}
while True:
 word = input("Escribe una papabra que no entiendas -en mayusculas-: ")
 if word in diccionario_memes.keys(): 
     print (word, "significa", diccionario_memes.get(word))
 else:
     print ("Lo siento, tampoco conozco esa palabra")
 exit = input("Quieres buscar otra palabra? (Escribe SI o NO) ")
 if exit=="NO":
     print("Hasta luego!")
     break;
