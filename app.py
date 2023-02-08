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
    return render_template("index.html", links=[
        ("new/pokémon", "Lisää Pokémon"),
        ("new/move", "Lisää Pokémonliike"),
        ("new/evolution", "Lisää kehitys"),
    ])

@app.route("/search/<predicate>")
def search(predicate):
    # TODO with regexp, less hacky
    if ";" in predicate:
        return "predicate contains \";\""
    
    sql = text("""
    SELECT
        name, CONCAT(type1, type2)
    FROM Monsters WHERE %s;
    """ % predicate)
    result = db.session.execute(sql)
    return render_template("show-table.html", query=result.fetchall())

@app.route("/new/<form>")
def new(form):
    match form:
        case "move":
            return render_template("form-move.html", action="send-move")
        case "pokémon":
            return render_template("form-pokémon.html", action="send-pokémon")
        case "evolution":
            sql = text("""
            SELECT id, name FROM Monsters;
            """)
            result = db.session.execute(sql)
            return render_template(
                "form-evolution.html",
                action="send-evolution",
                monsters=result.fetchall(),
            )
        case other:
            return render_template("invalid.html", form=form)

@app.route("/send-pokémon", methods=["POST"])
def send_pokemon():
    sql = text("""
    INSERT INTO Monsters (name, type1, type2)
    VALUES (:name, :type1, :type2);
    """)
    db.session.execute(sql, request.form)
    db.session.commit()
    return redirect("/")

@app.route("/send-move", methods=["POST"])
def send_move():
    sql = text("""
    INSERT INTO Moves (name, description)
    VALUES (:name, :description);
    """)
    db.session.execute(sql, request.form)
    db.session.commit()
    return redirect("/")

@app.route("/send-evolution", methods=["POST"])
def send_evolution():
    sql = text("""
    INSERT INTO Evolutions (child, parent, method)
    VALUES (:child, :parent, :method);
    """)
    db.session.execute(sql, request.form)
    db.session.commit()
    return redirect("/")

