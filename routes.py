from flask import redirect, render_template, request
from app import app
from querys import execute, commit, insert_matchup

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
    
    result = execute("""
    SELECT
        name, CONCAT(type1, type2)
    FROM Monsters WHERE %s;
    """ % predicate)
    return render_template("show-table.html", query=result.fetchall())

@app.route("/new/move")
def new():
    return render_template("form-move.html", action="send/move")

@app.route("/new/pokémon")
def new_pokemon():
    return render_template("form-pokémon.html", action="send/pokémon")

@app.route("/new/evolution")
def new_evolution():
    result = execute("SELECT id, name FROM Monsters")
    return render_template(
        "form-evolution.html",
        action="send/evolution",
        monsters=result.fetchall(),
    )

@app.route("/new/type")
def new_type():
    result = execute("SELECT id, name FROM Types")
    return render_template(
        "form-types.html",
        action="send/type",
        types=result.fetchall(),
    )

@app.route("/send/pokémon", methods=["POST"])
def send_pokemon():
    execute("""
    INSERT INTO Monsters (name, type1, type2)
    VALUES (:name, :type1, :type2);
    """, **request.form)
    commit()
    return redirect("/")

@app.route("/send/move", methods=["POST"])
def send_move():
    execute("""
    INSERT INTO Moves (name, description)
    VALUES (:name, :description);
    """, **request.form)
    commit()
    return redirect("/")

@app.route("/send/evolution", methods=["POST"])
def send_evolution():
    execute("""
    INSERT INTO Evolutions (child, parent, lvl)
    VALUES (:child, :parent, :lvl);
    """, **request.form)
    commit()
    return redirect("/")

@app.route("/send/type", methods=["POST"])
def send_type():
    sql = "INSERT INTO Types (name) VALUES (:name) RETURNING id"
    result = execute(sql, **request.form).fetchone()[0]
    
    def to_list(val):
        if type(val) == list:
            return val
        else:
            return [val] if val else []
    def get_request(name):
        return to_list(request.form.get(name))
    insert_matchup(result, get_request("effective"), "defender", True)
    insert_matchup(result, get_request("weakness"), "attacker", True)

    insert_matchup(result, get_request("ineffective"), "defender", False)
    insert_matchup(result, get_request("resistance"), "attacker", False)

    commit()
    return redirect("/")
