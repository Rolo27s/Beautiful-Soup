# Recordar que antes debo installar la librería request con el comando:
# python -m pip install requests

import requests

# URL de la que quiero guardar el HTML
URL = "https://realpython.github.io/fake-jobs/"
page = requests.get(URL)

print(page.text)