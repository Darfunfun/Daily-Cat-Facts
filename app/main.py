###############################################
# Flask : Micro serveur web
# render_template_string : Afficher du HTML depuis Python
# jsonify : Traduction de dictionnaire Python en JSON pour nos navigateurs
# requests : Pour interagir avec les APIs
###############################################

import requests
from flask import Flask, render_template, jsonify, request


siteweb = Flask(__name__)



@siteweb.route("/")
def Home():
    return render_template("index.html") # retourne le body HTTP de type HTML

#----------------------------------------------------------------------------------------------------------------

@siteweb.route("/catfacts_guardia")
def Catfact_home():
    return render_template("catfacts.html")


@siteweb.route("/catfacts_guardia/fact")
def Show_catfact():
    maRequestCatfact = requests.get("https://catfact.ninja/fact")
    maRequestCatfact = maRequestCatfact.json()
    return maRequestCatfact



# @siteweb.route("/catfacts")
# def catfactHome():
#     return render_template("catfacts.html") # retourne le body  HTTP de type HTML

# @siteweb.route("/catfacts/fact")
# def getCatFact():
#     myCatRequest = requests.get("https://catfact.ninja/fact", timeout=5) # Affiche un json, avec fact: "str" et length: int
#     myCatRequest = myCatRequest.json() # .json() ouvre l’enveloppe de Response et transforme le body JSON (texte) en dict Python
#     #print(myCatRequest)
#     return jsonify(myCatRequest) # transforme le dict Python en JSON texte, crée une réponse HTTP, retourne le body HTTP de type json

# #----------------------------------------------------------------------------------------------------------------















# @siteweb.route("/pokeapi")
# def pokeapiHome():
#     return render_template("pokeapi.html")

# @siteweb.route("/pokeapi/getpokemon")
# def getPokemon():
#     pokeName = request.args.get("name")
#     print(pokeName)
#     myPokeRequest = requests.get("https://pokeapi.co/api/v2/pokemon/{pokeName}")
#     print(myPokeRequest)
#     myPokeRequest = myPokeRequest.json()
#     return jsonify(myPokeRequest)






# #----------------------------------------------------------------------------------------------------------------

siteweb.run(debug=True)







# # OLD : 

# # import requests


# # try:
# #     r = requests.get('https://catfact.ninja/fact', timeout=5)
# #     r.raise_for_status()
# #     print("L'API repond !")

# #     data = r.json()
# #     print("Voici un fait sur les chats : ", data["fact"])

# # except requests.exceptions.RequestException as e:
# #     print("Probleme d'API... Code erreur : ", e)
# #     exit (1)
# # except ValueError as e:
# #     print("Probleme de décodage JSON... Code erreur : ", e)
# #     exit (1)



