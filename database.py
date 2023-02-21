from app import db
from sqlalchemy.sql import text
from sqlalchemy.exc import ProgrammingError

def execute(query, **kwargs):
    return db.session.execute(text(query), kwargs)

def commit():
    db.session.commit()

def filter(predicate):
    # TODO Make less hacky
    try:
        res = execute("""
        SELECT
            name,
            CONCAT(
                (SELECT name FROM Types WHERE id=type1),
                ' ',
                (SELECT name FROM Types WHERE id=type2)
            ),
            health,
            attack,
            defence,
            spc_att,
            spc_def,
            speed
        FROM Pokemon WHERE %s;
        """ % predicate)
        return res.fetchall()
    except ProgrammingError:
        return None


def pokemons():
    return execute("SELECT id, name FROM Pokemon;").fetchall()

def pokemon(name):
    return execute("""
    SELECT
        name,
        CONCAT(
            (SELECT name FROM Types WHERE id=type1),
            ' ',
            (SELECT name FROM Types WHERE id=type2)
        ),
        health,
        attack,
        defence,
        spc_att,
        spc_def,
        speed
    FROM Pokemon WHERE name=:name;
    """, name=name)

def insert_pokemon(**kwargs):
    execute("""
    INSERT INTO Pokemon (
        name, type1, type2,
        health, attack, defence, spc_att, spc_def, speed
    ) VALUES (
        :name, :type1, :type2,
        :health, :attack, :defence, :spc_att, :spc_def, :speed
    );
    """, **kwargs)
    commit()

def insert_moves(**kwargs):
    execute("""
    INSERT INTO Moves (
        name, typing, force, amount, accuracy, effect
    ) VALUES (
        :name, :typing, :force, :amount, :accuracy, :effect
    );
    """, **kwargs)
    commit()

def insert_evolution(**kwargs):
    execute("""
    INSERT INTO Evolutions (child, parent, lvl)
    VALUES (:child, :parent, :lvl);
    """, **kwargs)
    commit()

def types():
    return execute("SELECT id, name FROM Types").fetchall()

def insert_types(name, self, defenders, attackers):
    sql = "INSERT INTO Types (name) VALUES (:name) RETURNING id"
    type_id = execute(sql, name=name).fetchone()[0]

    sql = """
    INSERT INTO Matchups (attacker, defender, advantage)
    VALUES (:attacker, :defender, :advantage);
    """
    if self in {"good", "bad"}:
        execute(sql, attacker=type_id, defender=type_id, advantage=self=="good")

    for adv, types in defenders:
        for t in types:
            execute(sql, attacker=type_id, defender=t, advantage=adv)
    for adv, types in attackers:
        for t in types:
            execute(sql, attacker=t, defender=type_id, advantage=adv)
    commit()

