from flask import Flask, render_template, redirect, request
# importar la clase de friend.py
from usuario import Usuario
app = Flask(__name__)
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

if __name__ == "__main__":
    app.run(debug=True)