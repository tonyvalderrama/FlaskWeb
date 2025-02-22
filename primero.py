# Importar flask
from flask import Flask, render_template

# Crear una instancia de flask (ayuda a Flask encontrar todos los archivos y carpetas)
app = Flask(__name__)

# Crear una ruta (llamado "decorator" por razones que aún no entiendo) del servidor
# o sea, las "carpetas" donde puede buscar cosas en el sitio web.
# Éste es de la raíz: si solo ponen el URL...
@app.route('/')

# Defino la función que se va a ejecutar cuando visitan la raíz
def index():
    # Declaro variable para pasar a la página index.html
    primer_nombre = "Tony"
    textoConHTML = "Este es texto <strong>en negritas</strong>."
    # Puedo pasar arreglos de Python
    pizzaFavorita = ["Pepperoni","Margarita","4 quesos",1200,"Queso"]
    # Paso primer_nombre a la página (template) index.html
    return render_template("index.html",
        primer_nombre=primer_nombre,
        textoConHTML=textoConHTML,
        pizza=pizzaFavorita)

# Definir otra ruta (para cuando hagan IP/user/nombre, 
# ejemplo localhost:5000/user/Tony)
@app.route('/user/<nombre>')

# Defino la función que se va a ejecutar cuando visitan ruta user
# (nombre es lo que escribieron en la ruta después de user/)
def user(nombre):
    # user_name lo puedo usar en el template (ver HTML)
    return render_template("user.html",user_name=nombre)

# Crear páginas de error "propias"
# Invalid URL - errorhandler recibe el número de error
@app.errorhandler(404)
def pagina_no_ta(error):
    return render_template("404.html"),404

# Internal Server Errorr
@app.errorhandler(500)
def pagina_no_ta(error):
    return render_template("500.html"),500