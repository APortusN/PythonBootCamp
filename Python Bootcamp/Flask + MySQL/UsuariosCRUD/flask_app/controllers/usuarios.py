
from flask_app import app
from flask import render_template,redirect,request,session,flash
from flask_app.models.usuario import Usuario

@app.route("/usuarios")
def index():
    # llamar al método de clase get all para obtener todos los amigos
    usuarios = Usuario.get_all()
    print(usuarios)
    return render_template("leer.html", all_usuarios = usuarios)

@app.route('/usuarios/nuevo')
def nuevo_usuario():
    return render_template("crear.html")

# fragmento de código relevante de server.py

@app.route('/usuarios/crear', methods=["POST"])
def crear_usuario():
    # Primero hacemos un diccionario de datos a partir de nuestro request.form proveniente de nuestra plantilla
    # Las claves en los datos tienen que alinearse exactamente con las variables en nuestra cadena de consulta
    data = {
        "fnombre": request.form["fnombre"],
        "fapellido" : request.form["fapellido"],
        "fcorreoe" : request.form["fcorreoe"]
    }
    # Pasamos el diccionario de datos al método save de la clase Friend
    Usuario.save(data)
    # No olvides redirigir después de guardar en la base de datos
    return redirect('/usuarios')

@app.route('/usuarios/<int:id>')
def ver_usuario(id):
    data ={ 
        "id":id
    }
    return render_template("infousuario.html",ver_usuario=Usuario.get_one(data))

@app.route('/usuarios/<int:id>/editar')
def edit(id):
    data ={ 
        "id":id
    }
    return render_template("editar.html",editar_usuario=Usuario.get_one(data))

@app.route('/usuarios/actualizar',methods=['POST'])
def update():
    
    Usuario.update(request.form)
    return redirect('/usuarios')

@app.route('/usuarios/<int:id>/eliminar')
def destroy(id):
    data ={
        'id': id
    }
    Usuario.destroy(data)
    return redirect('/usuarios')