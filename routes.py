from flask import redirect, render_template, request

from app import app
import database

@app.route("/")
def index():
    return render_template("index.html", links=[
        ("new/pokémon", "Lisää Pokémon"),
        ("new/move", "Lisää Pokémonliike"),
        ("new/evolution", "Lisää kehitys"),
        ("new/type", "Lisää tyypitys"),
    ])

@app.route("/search/<predicate>")
def search(predicate):
    for char in ";()":
        if char in predicate:
            return "predicate contains: " + char
    
    pokemon = database.filter(predicate)
    return render_template("show-table.html", query=pokemon)

@app.route("/new/move")
def new():
    return render_template("form-move.html", action="send/move")

@app.route("/new/pokémon")
def new_pokemon():
    return render_template(
        "form-pokémon.html",
        action="send/pokémon",
        types=database.types(),
    )

@app.route("/new/evolution")
def new_evolution():
    return render_template(
        "form-evolution.html",
        action="send/evolution",
        pokemon=database.pokemon(),
    )

@app.route("/new/type")
def new_type():
    return render_template(
        "form-types.html",
        action="send/type",
        types=database.types(),
    )

@app.route("/send/pokémon", methods=["POST"])
def send_pokemon():
    database.insert_pokemon(**request.form)
    return redirect("/")

@app.route("/send/move", methods=["POST"])
def send_move():
    database.insert_moves(**request.form)
    return redirect("/")

@app.route("/send/evolution", methods=["POST"])
def send_evolution():
    database.insert_evolution(**request.form)
    return redirect("/")

@app.route("/send/type", methods=["POST"])
def send_type():
    database.insert_types(
        name=request.form["name"],
        defenders=(
            (True, request.form.getlist("effective")),
            (False, request.form.getlist("ineffective")),
        ),
        attackers=(
            (True, request.form.getlist("weakness")),
            (False, request.form.getlist("resistance"))
        )
    )
    return redirect("/")
