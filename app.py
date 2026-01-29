from flask import Flask, request

app = Flask(__name__)


@app.route("/")
def index():
       return '<h1>Hola Mundo XDDDD</h1>'
       
@app.route("/user/<int:ID>")
def user(ID):
    return f"Hola {ID}, ! Me encanta decir tu nombre"


@app.route("/agent")
def browser():
    user_agent = request.headers.get("User-Agent")
    return f"<p>Tu Navegador es: {user_agent}<p>"