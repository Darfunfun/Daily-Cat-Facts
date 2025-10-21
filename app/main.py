import requests


try:
    r = requests.get('https://catfact.ninja/fact', timeout=5)
    r.raise_for_status()
    print("L'API repond !")

    data = r.json()
    print("Voici un fait sur les chats : ", data["fact"])

except requests.exceptions.RequestException as e:
    print("Probleme d'API... Code erreur : ", e)
    exit (1)
except ValueError as e:
    print("Probleme de décodage JSON... Code erreur : ", e)
    exit (1)

