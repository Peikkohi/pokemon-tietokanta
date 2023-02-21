from app import db
from itertools import groupby
from sqlalchemy.sql import text

def execute(query, **kwargs):
    return db.session.execute(text(query), kwargs)

def commit():
    db.session.commit()

def filter(predicate):
    # TODO Make less hacky
    res = execute("""
    SELECT
        name,
        (SELECT STRING_AGG((SELECT name FROM Types WHERE id=type_id), ' ')
        FROM Typing
        WHERE pokemon_id=id),
        COALESCE((SELECT
            STRING_AGG(DISTINCT (SELECT name FROM Types WHERE id=attacker), ' ')
        FROM Typing, Matchups WHERE pokemon_id=id AND defender=type_id AND advantage), ''),
        COALESCE((SELECT
            STRING_AGG(DISTINCT (SELECT name FROM Types WHERE id=attacker), ' ')
        FROM Typing, Matchups WHERE pokemon_id=id AND defender=type_id AND NOT advantage), ''),
        health,
        attack,
        defence,
        special_attack,
        special_defence,
        speed,
        health + attack + defence +
        special_attack + special_defence + speed,
        COALESCE((SELECT
            CONCAT((SELECT name FROM Pokemon WHERE id=child), ': ', requirement)
        FROM Evolutions WHERE parent=id), ''),
        COALESCE((SELECT
            CONCAT((SELECT name FROM Pokemon WHERE id=parent), ': ', requirement)
        FROM Evolutions WHERE child=id), '')
    FROM Pokemon WHERE %s;
    """ % predicate)
    return res.fetchall()


def pokemons():
    return execute("SELECT id, name FROM Pokemon;").fetchall()

def insert_pokemon(**kwargs):
    ret = execute("""
    INSERT INTO Pokemon (
        name, health, attack, defence,
        special_attack, special_defence, speed
    ) VALUES (
        :name, :health, :attack, :defence,
        :special_attack, :special_defence, :speed
    ) RETURNING id;
    """, **kwargs).fetchone()[0]
    commit()
    return ret

def insert_typing(**kwargs):
    execute("""
    INSERT INTO Typing
        (pokemon_id, type_id, is_primary)
    VALUES
        (:pokemon_id, :type_id, :is_primary);
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
    INSERT INTO Evolutions (child, parent, requirement)
    VALUES (:child, :parent, :requirement);
    """, **kwargs)
    commit()

def types():
    return execute("SELECT id, name FROM Types ORDER BY id").fetchall()

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

def matchups():
    sql = """
    SELECT
        A.name, B.name,
        CASE (SELECT advantage FROM Matchups WHERE attacker=A.id AND defender=B.id)
        WHEN TRUE THEN 1
        WHEN FALSE THEN -1
        ELSE 0
        END
    FROM
        Types A, Types B
    ORDER BY
        A.id, B.id;
    """
    res = execute(sql).fetchall()
    return [(val, [effectiveness for _, _, effectiveness in it])
            for val, it in groupby(res, key=lambda n: n[0])]
