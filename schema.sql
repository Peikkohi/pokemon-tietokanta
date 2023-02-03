CREATE TABLE Types (
	id SERIAL PRIMARY KEY,
	name TEXT
);
CREATE TABLE Matchups (
	attacker SERIAL REFERENCES Types,
	defender SERIAL REFERENCES Types,
	effectiveness INTEGER
);
CREATE TABLE Monsters (
	id SERIAL PRIMARY KEY,
	name TEXT,
	type1 SERIAL REFERENCES Types,
	type2 SERIAL REFERENCES Types
	--ability1 TEXT,
	--ability2 TEXT,
	--health INTEGER,
	--attack INTEGER,
	--defence INTEGER,
	--spc_att INTEGER,
	--spc_def INTEGER,
	--speed INTEGER
);
CREATE TABLE Abilities (
	id SERIAL PRIMARY KEY,
	name TEXT
);
