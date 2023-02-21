CREATE TABLE Types (
	id SERIAL PRIMARY KEY,
	name TEXT UNIQUE
);
CREATE TABLE Matchups (
	attacker SERIAL REFERENCES Types,
	defender SERIAL REFERENCES Types,
	advantage BOOLEAN,
	PRIMARY KEY (attacker, defender)
);
CREATE TABLE Pokemon (
	id SERIAL PRIMARY KEY,
	name TEXT UNIQUE,
	health INTEGER,
	attack INTEGER,
	defence INTEGER,
	special_attack INTEGER,
	special_defence INTEGER,
	speed INTEGER
);
CREATE TABLE Evolutions (
	child SERIAL REFERENCES Pokemon,
	parent SERIAL REFERENCES Pokemon,
	requirement INTEGER
);
CREATE TABLE Typing (
	pokemon_id SERIAL REFERENCES Pokemon,
	type_id SERIAL REFERENCES Types,
	is_primary BOOLEAN,
	PRIMARY KEY (pokemon_id, type_id, is_primary)
)
