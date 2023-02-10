CREATE TABLE Types (
	id SERIAL PRIMARY KEY,
	name TEXT
);
CREATE TABLE Matchups (
	attacker SERIAL REFERENCES Types,
	defender SERIAL REFERENCES Types,
	advantage BOOLEAN
);
CREATE TABLE Monsters (
	id SERIAL PRIMARY KEY,
	name TEXT,
	type1 TEXT, --SERIAL REFERENCES Types,
	type2 TEXT --SERIAL REFERENCES Types
	--ability1 TEXT,
	--ability2 TEXT,
	--health INTEGER,
	--attack INTEGER,
	--defence INTEGER,
	--spc_att INTEGER,
	--spc_def INTEGER,
	--speed INTEGER
);
--CREATE TABLE Abilities (
	--id SERIAL PRIMARY KEY,
	--name TEXT
--);
CREATE TABLE Moves (
	id SERIAL PRIMARY KEY,
	name TEXT,
	description TEXT
);
CREATE TABLE Evolutions (
	child SERIAL REFERENCES Monsters,
	parent SERIAL REFERENCES Monsters,
	lvl INTEGER
);
