from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)

app.secret_key = 'root'

# Haz que la ruta raíz ("/") muestre una página con el formulario
@app.route('/')
def index():
    return render_template("index.html")

# Haz que la ruta "/result" muestre la información del formulario en una nueva página HTML
@app.route('/result')
def result():
    return render_template("resultados.html")

# Pon los datos del formulario en la sesión
@app.route('/process', methods=['POST'])
def process():
    session['nombre'] = request.form['nombre1']
    session['ubicacion'] = request.form['ubicacion1']
    session['lenguaje'] = request.form['lenguaje1']
    session['comentario'] = request.form['comentarios1']
    return redirect('/result')

if __name__=="__main__":   
    app.run(debug=True)    