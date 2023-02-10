from flask import redirect, render_template, request
import itertools

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
    # TODO with regexp, less hacky
    for char in ";()":
        if char in predicate:
            return "predicate contains: " + char
    
    monsters = database.filter(predicate)
    return render_template("show-table.html", query=monsters)

@app.route("/new/move")
def new():
    return render_template("form-move.html", action="send/move")

@app.route("/new/pokémon")
def new_pokemon():
    return render_template("form-pokémon.html", action="send/pokémon")

@app.route("/new/evolution")
def new_evolution():
    return render_template(
        "form-evolution.html",
        action="send/evolution",
        monsters=database.pokemon(),
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
    def to_list(val):
        if type(val) == list:
            return val
        else:
            return [val] if val else []
    def field(name):
        return to_list(request.form.get(name))
    database.insert_types(
        name=request.form["name"],
        defenders=itertools.chain(
            zip(field("effective"), itertools.repeat(True)),
            zip(field("ineffective"), itertools.repeat(False))
        ),
        attackers=itertools.chain(
            zip(field("weakness"), itertools.repeat(True)),
            zip(field("resistance"), itertools.repeat(False))
        )
    )
    return redirect("/")
