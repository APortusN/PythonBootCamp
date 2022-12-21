from flask import render_template, redirect, request
from flask_app import app
from flask_app.models.encuesta import Encuesta 
from flask_app.models import encuesta


# Haz que la ruta raíz ("/") muestre una página con el formulario
@app.route('/')
def index():
    return render_template("index.html")

# Haz que la ruta "/result" muestre la información del formulario en una nueva página HTML
@app.route('/result')
def result():
    return render_template("resultados.html", encuesta = Encuesta.get_ultima_encuesta())

# Pon los datos del formulario en la sesión
@app.route('/process', methods=['POST'])
def process():   
    if Encuesta.validar_encuesta(request.form):
        Encuesta.save(request.form)
        return redirect('/result')
    return redirect('/')