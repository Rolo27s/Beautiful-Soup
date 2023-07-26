import requests
from bs4 import BeautifulSoup

# URL a rascar informacion
URL = "https://www.youtube.com/playlist?list=PLPl81lqbj-4Iy7yuRrVLn4V6isOVpvlpl"
page = requests.get(URL)

# Parseo el contenido de la pagina
soup = BeautifulSoup(page.content, "html.parser")

# Busco primero por ID que me interese
results = soup.find(id="ResultsContainer")