from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def prueba(): #Funcion que devuelve una cadena de texto
    return render_template("homepage.html")

if __name__ == "__main__":
    app.run(debug=True) #Ejecuta la aplicacion Flask facilmente desde la terminal
