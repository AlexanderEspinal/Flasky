from flask import Flask, request,redirect ,make_response,render_template
from flask_bootstrap import Bootstrap

app = Flask(__name__)

bootstrap = Bootstrap(app)

       
@app.route("/")
def index():
    return render_template("index.html", name='Pedro')


@app.route("/agent")
def browser():
    user_agent = request.headers.get("User-Agent")
    user_ip = request.remote_addr

    return f"<p>Tu Navegador es:  {user_agent} \n y tu IP es:  {user_ip}<p>"

@app.route("/cookie")
def cookies():
    response = make_response("<h1>Aceptas tus cookies</h1>")
    response.set_cookie("Propiedad de", "Alexander")
    return response

@app.route("/escape")
def ruta_externa():
    return redirect("https://archlinux.org", code=302)


    


