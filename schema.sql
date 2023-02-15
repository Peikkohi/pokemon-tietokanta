CREATE TABLE Types (
	id SERIAL PRIMARY KEY,
	name TEXT
);
CREATE TABLE Matchups (
	attacker SERIAL REFERENCES Types,
	defender SERIAL REFERENCES Types,
	advantage BOOLEAN
);
CREATE TABLE Pokemon (
	id SERIAL PRIMARY KEY,
	name TEXT,
	type1 SERIAL REFERENCES Types,
	type2 SERIAL REFERENCES Types,
	--ability1 TEXT,
	--ability2 TEXT,
	health INTEGER,
	attack INTEGER,
	defence INTEGER,
	spc_att INTEGER,
	spc_def INTEGER,
	speed INTEGER
);
--CREATE TABLE Abilities (
	--id SERIAL PRIMARY KEY,
	--name TEXT
--);
CREATE TABLE Moves (
	id SERIAL PRIMARY KEY,
	name TEXT,
	typing SERIAL REFERENCES Types,
	force INTEGER,
	amount INTEGER,
	accuracy INTEGER,
	effect TEXT
);
CREATE TABLE Evolutions (
	child SERIAL REFERENCES Pokemon,
	parent SERIAL REFERENCES Pokemon,
	lvl INTEGER
);
