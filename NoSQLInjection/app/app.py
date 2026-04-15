from flask import Flask, request, render_template, redirect, session
from pymongo import MongoClient
import json

app = Flask(__name__)
app.secret_key = "secret123"

# Conexión a MongoDB (servicio del docker-compose)
client = MongoClient("mongodb://mongo:27017/")
db = client["lab_db"]
users = db["users"]

# Crear usuario por defecto
if users.count_documents({}) == 0:
    users.insert_one({
        "username": "admin",
        "password": "1234"
    })


def parse_if_json_structure(value):
    """Parse only JSON object/array payloads to keep common credentials as strings."""
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

        # 🔥 VULNERABILIDAD: interpreta input como JSON
        username = parse_if_json_structure(username)
        password = parse_if_json_structure(password)

        query = {
            "username": username,
            "password": password
        }

        print("QUERY EJECUTADO:", query)  # 👈 para evidencias

        user = users.find_one(query)

        if user:
            session["user"] = str(user["username"])
            return redirect("/dashboard")
        else:
            error = "Login fallido. Verifica usuario y contraseña."

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


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)