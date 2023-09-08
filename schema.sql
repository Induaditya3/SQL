CREATE TABLE houses(
    id INTEGER,
    house TEXT,
    PRIMARY KEY(id)
);

CREATE TABLE head(
    id INTEGER,
    hname TEXT,
    PRIMARY KEY(id)
);

CREATE TABLE students(
    id INTEGER,
    sname TEXT,
    headId INTEGER,
    houseId INTEGER,
    FOREIGN KEY(headId) REFERENCES head(id),
    FOREIGN KEY(houseId) REFERENCES houses(id)
);