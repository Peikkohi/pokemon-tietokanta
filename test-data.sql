INSERT INTO Types (id, name) VALUES
	(1, 'Fire'),
	(2, 'Flying'),
	(3, 'Water');

INSERT INTO Matchups (attacker, defender, advantage) VALUES
	(1, 1, FALSE),
	(1, 3, FALSE),
	(3, 3, FALSE),
	(3, 1, TRUE);

INSERT INTO Pokemon (
	id, name, health, attack, defence,
	special_attack, special_defence, speed
) VALUES
	(1, 'Charmander', 39, 52, 43, 60, 50, 65),
	(2, 'Charmeleon', 58, 64, 58, 80, 65, 80),
	(3, 'Charizard', 78, 84, 78, 109, 85, 100),
	(4, 'Magikarp', 20, 10, 55, 15, 20, 80),
	(5, 'Gyarados', 95, 125, 79, 60, 100, 81),
	(6, 'Volcanion', 80, 110, 120, 130, 90, 70);

INSERT INTO Typing (pokemon_id, type_id, is_primary) VALUES
	(1, 1, TRUE),
	(2, 1, TRUE),
	(3, 1, TRUE),
	(3, 2, FALSE),
	(4, 3, TRUE),
	(5, 3, TRUE),
	(5, 2, FALSE),
	(6, 1, TRUE),
	(6, 3, FALSE);


INSERT INTO Evolutions (child, parent, requirement) VALUES
	(1, 2, 16),
	(2, 3, 36),
	(4, 5, 20);	
