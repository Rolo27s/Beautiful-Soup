from selenium import webdriver
from bs4 import BeautifulSoup

# Configurar el controlador de Chrome (Me da un error en el path del ejecutable)
driver = webdriver.Chrome(executable_path='/chromedriver.exe')

# URL de YouTube que deseas analizar
url = "https://www.youtube.com/playlist?list=PLPl81lqbj-4Iy7yuRrVLn4V6isOVpvlpl"

# Cargar la página usando Selenium
driver.get(url)

# Obtener el código fuente HTML de la página cargada
html = driver.page_source

# Cerrar el navegador controlado por Selenium
driver.quit()

# Analizar el código HTML con Beautiful Soup
soup = BeautifulSoup(html, 'html.parser')

# Ahora puedes utilizar Beautiful Soup para encontrar y extraer los elementos deseados de la página
# Por ejemplo, puedes buscar los títulos de los videos:
videos = soup.find_all('h3', {'class': 'style-scope ytd-grid-video-renderer'})
for video in videos:
    print(video.text)
