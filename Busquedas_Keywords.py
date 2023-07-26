import requests
from bs4 import BeautifulSoup

# URL a rascar informacion
URL = "https://realpython.github.io/fake-jobs/"
page = requests.get(URL)

# Parseo el contenido de la pagina
soup = BeautifulSoup(page.content, "html.parser")

# Busco primero por ID que me interese
results = soup.find(id="ResultsContainer")

# Busco por nombre de clase y guardo en un objeto que contendrá cosas
job_elements = results.find_all("div", class_="card-content")

# Puedo hacer busquedas concretas con key words. En este caso veo la info que contenga "Python"
python_jobs = results.find_all(
    "h2", string=lambda text: "python" in text.lower()
)

python_job_elements = [
    h2_element.parent.parent.parent for h2_element in python_jobs
]

for job_element in python_job_elements:
    title_element = job_element.find("h2", class_="title")
    company_element = job_element.find("h3", class_="company")
    location_element = job_element.find("p", class_="location")
    print(title_element.text.strip())
    print(company_element.text.strip())
    print(location_element.text.strip())
    print()