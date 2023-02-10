from app import db
from sqlalchemy.sql import text

def execute(query, **kwargs):
    return db.session.execute(text(query), kwargs)

def commit():
    db.session.commit()

def filter(predicate):
    return execute("""
    SELECT
        name, CONCAT(type1, type2)
    FROM Monsters WHERE %s;
    """ % predicate).fetchall()

def pokemon():
    return execute("SELECT id, name FROM Monsters;").fetchall()

def insert_pokemon(**kwargs):
    execute("""
    INSERT INTO Monsters (name, type1, type2)
    VALUES (:name, :type1, :type2);
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
    for t, adv in defenders:
        execute(sql, attacker=type_id, defender=t, advantage=adv)
    for t, adv in attackers:
        execute(sql, attacker=t, defender=type_id, advantage=adv)
    commit()

