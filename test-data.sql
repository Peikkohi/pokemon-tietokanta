INSERT INTO Types (name) VALUES
	('Fire'), ('Flying'), ('Water');

INSERT INTO Pokemon (
	name, type1, type2,
	health, attack, defence, spc_att, spc_def, speed
) VALUES (
	'Charizard',
	(SELECT id FROM Types WHERE name='Fire'),
	(SELECT id FROM Types WHERE name='Flying'),
	78, 84, 78, 109, 85, 100);
