from flask import Flask, request, render_template, redirect, session
from pymongo import MongoClient
import json

app = Flask(__name__)
app.secret_key = "secret123"

# Conexión a MongoDB
client = MongoClient("mongodb://mongo:27017/")
db = client["lab_db"]
users = db["users"]

# Crear usuarios por defecto
if users.count_documents({}) == 0:
    users.insert_many([
        {"username": "admin", "password": "234"},
        {"username": "ana", "password": "ana1234"},
        {"username": "bruno", "password": "bruno1234"},
        {"username": "carla", "password": "carla1234"},
        {"username": "diego", "password": "diego1234"},
        {"username": "elena", "password": "elena1234"},
        {"username": "fabian", "password": "fabian1234"},
        {"username": "gabriela", "password": "gabriela1234"},
        {"username": "hector", "password": "hector1234"},
        {"username": "isabel", "password": "isabel1234"},
        {"username": "jorge", "password": "jorge1234"}
    ])


def parse_if_json_structure(value):
    """Parsea JSON solo si parece objeto/lista"""
    if not isinstance(value, str):
        return value

    trimmed = value.strip()
    if not trimmed.startswith("{") and not trimmed.startswith("["):
        return value

    try:
        return json.loads(trimmed)
    except Exception:
        return value


@app.route("/", methods=["GET", "POST"])
def login():
    error = None
    form_username = ""

    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")
        form_username = username or ""

        # 🔥 VULNERABILIDAD 1: interpretar input como JSON
        username = parse_if_json_structure(username)
        password = parse_if_json_structure(password)

        query = {
            "username": username,
            "password": password
        }

        # 💣 VULNERABILIDAD 2 (PRO): permitir $where injection
        if isinstance(username, dict) and "$where" in username:
            query = username  # reemplaza toda la consulta

        print("🔥 QUERY EJECUTADO:", query)

        user = users.find_one(query)

        if user:
            session["user"] = str(user["username"])
            return redirect("/dashboard")
        else:
            error = "❌ Login fallido. Verifica usuario y contraseña."

    return render_template("login.html", error=error, form_username=form_username)


@app.route("/dashboard")
def dashboard():
    if "user" not in session:
        return redirect("/")

    return render_template("dashboard.html", user=session["user"])


@app.route("/logout")
def logout():
    session.clear()
    return redirect("/")


# 💣 ENDPOINT PARA DEMOSTRAR EXFILTRACIÓN
@app.route("/debug_users")
def debug_users():
    data = list(users.find({}, {"_id": 0}))
    return str(data)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)