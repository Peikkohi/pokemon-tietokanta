from app import db
from sqlalchemy.sql import text

def execute(query, **kwargs):
    return db.session.execute(text(query), kwargs)

def commit():
    db.session.commit()

sql = """
INSERT INTO Matchups (attacker, defender, advantage)
VALUES (:attacker, :defender, :advantage);
"""
def insert_matchup(comp, form, attacker, advantage):
    for id in form:
        if attacker:
            execute(sql, attacker=id, defender=comp, advantage=advantage)
        else:
            execute(sql, attacker=comp, defender=id, advantage=advantage)
