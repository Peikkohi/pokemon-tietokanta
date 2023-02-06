from flask import Flask
from flask import redirect, render_template, request
from sqlalchemy.sql import text
from flask_sqlalchemy import SQLAlchemy
from os import getenv

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = getenv("DATABASE_URL")
db = SQLAlchemy(app)

@app.route("/")
def index():
    sql = text("SELECT * FROM Types")
    result = db.session.execute(sql)
    elementals = result.fetchall()
    sql = text("""
    SELECT
        species,
        (SELECT name FROM Types WHERE id=type1),
        (SELECT name FROM Types WHERE id=type2)
    FROM Monsters;
    """)
    result = db.session.execute(sql)
    monsters = result.fetchall()
    return render_template("index.html", elementals=elementals, monsters=monsters)

@app.route("/search/<predicate>")
def search(predicate):
    field, value = tuple(predicate.split("="))
    if field == "name" or True:
        sql = text("SELECT * FROM Monsters WHERE species=:query")
        result = db.session.execute(sql, {"query": value})
        return str(result.fetchall())

@app.route("/new/<data_type>")
def new(data_type):
    sql = text("SELECT * FROM Types")
    result = db.session.execute(sql)
    data = result.fetchall()

    template, form = {
        "pokémon": ("form-pokémon.html", {
            "action": "send/pokémon",
            "types": data,
        }),
        "type": ("form.html", {
            "action": "send/type",
        }),
        "ability": ("form.html", {
            "action": "send/ability",
        }),
    }.get(data_type) or ("invalid.html", None)
    return render_template(template, **form)

@app.route("/send/<param>", methods=["POST"])
def send(param):
    source = {
        "pokémon": """
            INSERT INTO Monsters (species, type1, type2) VALUES
                (:name, :type1, :type2);
        """,
        "type": "INSERT INTO Types (name) VALUES (:name)",
        "ability": "INSERT INTO Abilities (name) VALUES (:name)",
    }.get(param)
    sql = text(source)
    db.session.execute(sql, request.form)
    db.session.commit()
    return redirect("/")

