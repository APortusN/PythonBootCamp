from flask import render_template, redirect, request
from flask_app import app
from flask_app.models.dojo import Dojo

@app.route('/')
def index():
    return redirect('/dojos')

@app.route('/dojos')
def dojos():
    dojos = Dojo.get_all()
    return render_template("dojos.html", all_dojos = dojos)

@app.route('/crear/dojo', methods=['PoST'])
def create_dojo():
    Dojo.save(request.form)
    return redirect('/dojos')

@app.route('/dojos/<int:id>')
def sjpw_dojo(id):
    data = {
        "id": id
    }
    return render_template('dojo_show.html', dojo=Dojo.get_dojo_with_ninjas(data))