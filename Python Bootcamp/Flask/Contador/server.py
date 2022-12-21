from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = 'root'

import datetime

# Haz que la ruta raíz renderice una plantilla que muestre la cantidad de veces que el cliente ha 
# visitado este sitio. Actualiza la página varias veces para asegurarte de que el contador esté funcionando.
@app.route('/')
def index():
    if "count" not in session:
        session["count"] = 0
    session["count"] += 1
    return render_template("index.html")

# Agrega una ruta "/destroy_session" que elimine la sesión y redirija a la ruta raíz. Pruébalo.
@app.route('/destroy_session')
def reset():
    session.clear()
    return redirect('/')

# agrega un botón +2 debajo del contador y una nueva ruta que incremente el contador en 2
@app.route('/doble')
def doble():
    if "count" not in session:
        session["count"] = 0
    session["count"] += 2
    return render_template("index.html")

@app.route('/formularioincremento', methods=['POST'])
def incremento():
    session['count'] += int(request.form['formularioincremento'])-1
    return redirect('/')

if __name__=="__main__":   
    app.run(debug=True)    