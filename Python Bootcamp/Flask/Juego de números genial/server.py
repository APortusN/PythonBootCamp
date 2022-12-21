from flask import Flask, render_template, session, redirect, request
import random

app = Flask(__name__)

app.secret_key = "Secreto"

# En la ruta raíz, guarda un número aleatorio entre 1 y 100 y muestra un formulario para que el usuario adivine el número
@app.route('/')
def index():
    if "num" not in session:
        session['num'] = random.randint(1,100)
    return render_template("index.html")

# Crea una ruta que determine si el número enviado es demasiado alto, demasiado bajo o correcto. Muestra este estado en la página HTML.
# Muestra los resultados como en el esquema de arriba (es decir, con los colores y el posicionamiento apropiados)
# Permite que el usuario siga adivinando hasta que lo adivine
@app.route('/adivinar',methods=['POST'])
def adivinar():
    session['adivinar'] = int(request.form['adivinar'])
    return redirect('/')

@app.route('/reiniciar')
def reiniciar():
    session.clear()
    return redirect('/')

# Informa al usuario cuántos intentos realizó antes de adivinar el número correcto
@app.route('/')
def adivinar_intentos():
    if "count" not in session:
        session["count"] = 0
    session ["count"] += 1
    return render_template("index.html")

if __name__=="__main__":
    app.run(debug=True)