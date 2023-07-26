# Tutorial basico de como usar Beautiful Soup para web scrapping con Python
Fuente consultada [aqui](https://realpython.com/beautiful-soup-web-scraper-python/)

## Paso 1 - Estudia la Web
Web scrapping es el proceso de reunir información de internet. Generalmente se presupone que llevará algún tipo de automatización en el proceso de reunir información.
<br>

Se va a practicar con [esta pagina](https://realpython.github.io/fake-jobs/) de prueba que facilita el tutorial de web scrapping con <u>**Python**</u>
<br>

* Paso 1: Inspeccionar tu fuente de datos
* Paso 2: Deconstruir las URL's
    * Start: The beginning of the query parameters is denoted by a question mark (?).
    * Information: The pieces of information constituting one query parameter are encoded in key-value pairs, where related keys and values are joined together by an equals sign (key=value).
    * Separator: Every URL can have multiple query parameters, separated by an ampersand symbol (&).
* Paso 3: Inspeccionar el sitio web con el inspector de Google o similar. Ver el DOM.

## Paso 2 - Raspa codigo HTML
* Copiar el contenido HTML con python usando un entorno virtual
```bash
    $ python -m pip install requests
```
Abrimos un documento .py y copiamos este codigo
``` python
import requests

URL = "https://realpython.github.io/fake-jobs/"
page = requests.get(URL)

print(page.text)
```
Es importante notar que solo copiaremos elementos estáticos. No será posible copiar scripts etc
<br>

Algunas web requieren de Login y la librería request la soporta, pero no se cubrirá de momento. [AQUI](https://docs.python-requests.org/en/latest/user/authentication/) se explica como hacerlo
<br>

Sitios web dinámicos: No lo cubrimos aqui pero existe la librería [requests-html](https://github.com/psf/requests-html) de python o [Selenium](https://www.selenium.dev/)
<br>

## Paso 3 - Analizar codigo HTML
Beautiful Soup es una librería de Python que analiza información estructurada. Instalala con el siguiente comando:

``` bash $ python -m pip install beautifulsoup4 ```

Luego crea un objeto Beautiful Soup
```python 
import requests
from bs4 import BeautifulSoup

URL = "https://realpython.github.io/fake-jobs/"
page = requests.get(URL)

soup = BeautifulSoup(page.content, "html.parser")
```

### Podemos primero tratar de estructurar la informacion a traves de los ID's
```python
results = soup.find(id="ResultsContainer")
```
En este caso estaríamos buscando el id concreto que se llama *ResultsContainer*
<br>

Podemos usar la propiedad prettify para ver la informacion
```python
print(results.prettify())
```

### Encontrar elementos por Class Name
```python 
job_elements = results.find_all("div", class_="card-content")
```
Luego podemos ver cada elemento iterando sobre todos los elementos encontrados con esa clase
```python 
for job_element in job_elements:
    print(job_element, end="\n"*2)
```
Podemos ser mas concretos usando este tipo de sintaxis:
```python
for job_element in job_elements:
    title_element = job_element.find("h2", class_="title")
    company_element = job_element.find("h3", class_="company")
    location_element = job_element.find("p", class_="location")
    print(title_element)
    print(company_element)
    print(location_element)
    print()
```

Si queremos extraer el HTML (texto) de cada cosa en concreto, podemos usar la propiedad **.text**
```python
for job_element in job_elements:
    title_element = job_element.find("h2", class_="title")
    company_element = job_element.find("h3", class_="company")
    location_element = job_element.find("p", class_="location")
    print(title_element.text)
    print(company_element.text)
    print(location_element.text)
    print()
```

En caso de querer limpiar espacios en blanco, podemos usar el metodo .strip de los strings de python y así obtener un resultado más limpio.
```python
for job_element in job_elements:
    title_element = job_element.find("h2", class_="title")
    company_element = job_element.find("h3", class_="company")
    location_element = job_element.find("p", class_="location")
    print(title_element.text.strip())
    print(company_element.text.strip())
    print(location_element.text.strip())
    print()
```

### Encontrar elementos por Class Name y por Contenido de Texto (Palabras claves)

```python
python_jobs = results.find_all("h2", string="Python")
print(python_jobs)
```

### Pasar una funcion al metodo Beautiful Soup
En este ejemplo se pasa una funcion anónima
```python
python_jobs = results.find_all(
    "h2", string=lambda text: "python" in text.lower()
)
# Probamos si funciona, por ejemplo con este print
print(len(python_jobs))
# Devolvería 10, que significa que se han encontrado 10 resultados con la palabra clave "python"
```

### Extraer atributos
Si tengo este trozo de codigo html:
```html
    <footer class="card-footer">
        <a href="https://www.realpython.com" target="_blank"
           class="card-footer-item">Learn</a>
        <a href="https://realpython.github.io/fake-jobs/jobs/senior-python-developer-0.html"
           target="_blank"
           class="card-footer-item">Apply</a>
    </footer>
  </div>
</div>
```
Puedo ver las url's asi:
```python
for job_element in python_job_elements:
    links = job_element.find_all("a")
    for link in links:
        link_url = link["href"]
        print(f"Apply here: {link_url}\n")
```