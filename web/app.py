import os
import random
from flask import Flask, render_template, request
import pymysql

app = Flask(__name__)

def get_db_connection():
    return pymysql.connect(
        host=os.getenv("DB_HOST", "db"),
        port=int(os.getenv("DB_PORT", "3306")),
        user=os.getenv("DB_USER", "banduser"),
        password=os.getenv("DB_PASSWORD", "bandpass"),
        database=os.getenv("DB_NAME", "bandnames"),
        cursorclass=pymysql.cursors.DictCursor
    )

@app.route("/", methods=["GET", "POST"])
def index():
    db_status = None
    band_names = []

    if request.method == "POST":
        action = request.form.get("action")

        if action == "check_db":
            try:
                conn = get_db_connection()
                conn.close()
                db_status = "Communication avec la base de données établie"
            except Exception as e:
                # 👉 On affiche l’erreur pour debug
                db_status = f"Impossible de se connecter à la base de données : {e}"

        elif action == "generate":
            try:
                conn = get_db_connection()
                with conn.cursor() as cursor:
                    cursor.execute("SELECT word FROM adjectives")
                    adjectives = [row["word"] for row in cursor.fetchall()]

                    cursor.execute("SELECT word FROM nouns")
                    nouns = [row["word"] for row in cursor.fetchall()]

                conn.close()

                if adjectives and nouns:
                    for _ in range(10):
                        adj = random.choice(adjectives)
                        noun = random.choice(nouns)
                        band_names.append(f"The {adj} {noun}")
            except Exception as e:
                db_status = f"Impossible de se connecter à la base de données : {e}"

    return render_template("index.html", db_status=db_status, band_names=band_names)
