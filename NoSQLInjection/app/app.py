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


@app.route("/", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")

        # 🔥 VULNERABILIDAD: interpreta input como JSON
        try:
            username = json.loads(username)
        except:
            pass

        try:
            password = json.loads(password)
        except:
            pass

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
            return "❌ Login fallido"

    return render_template("login.html")


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