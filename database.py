from app import db
from sqlalchemy.sql import text

def execute(query, **kwargs):
    return db.session.execute(text(query), kwargs)

def commit():
    db.session.commit()

def filter(predicate):
    # Make less hacky
    return execute("""
    SELECT
        name, CONCAT(type1, type2)
    FROM Pokemon WHERE %s;
    """ % predicate).fetchall()

def pokemon():
    return execute("SELECT id, name FROM Pokemon;").fetchall()

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
    INSERT INTO Moves (name, description)
    VALUES (:name, :description);
    """, **kwargs)
    commit()

def insert_evolutions(**kwargs):
    execute("""
    INSERT INTO Evolutions (child, parent, lvl)
    VALUES (:child, :parent, :lvl);
    """, **kwargs)
    commit()

def types():
    return execute("SELECT id, name FROM Types").fetchall()

def insert_types(name, defenders, attackers):
    sql = "INSERT INTO Types (name) VALUES (:name) RETURNING id"
    type_id = execute(sql, name=name).fetchone()[0]

    sql = """
    INSERT INTO Matchups (attacker, defender, advantage)
    VALUES (:attacker, :defender, :advantage);
    """
    for adv, types in defenders:
        for t in types:
            execute(sql, attacker=type_id, defender=t, advantage=adv)
    for adv, types in attackers:
        for t in types:
            execute(sql, attacker=t, defender=type_id, advantage=adv)
    commit()

