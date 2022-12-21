from flask_app.models.ninja import Ninja
from flask_app.models.dojo import Dojo
from flask import render_template, redirect, request
from flask_app import app
from flask_app.models import dojo, ninja

@app.route('/ninjas')
def ninjas():
    return render_template('newninja.html', dojos= dojo.Dojo.get_all())

@app.route('/crear/ninja', methods=["POST"])
def create_ninja():
    id_ninja = Ninja.save(request.form)
    data = {
        "id_ninja":id_ninja
    }
    results = Ninja.get_un_ninja(data)
    print(results, "AQUIIIII")
    return redirect(f'/dojos/{results["dojo_id"]}')

# @app.route('/crear/ninja', methods=["POST"])
# def create_ninja():
#     ninja.Ninja.save(request.form)
#     return redirect('/')