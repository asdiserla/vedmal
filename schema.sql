DROP TABLE IF EXISTS bets;

CREATE TABLE bets (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    created TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    bet VARCHAR(128) NOT NULL,
    better1 VARCHAR(64) NOT NULL,
    better2 VARCHAR(64) NOT NULL
);

-- CREATE TABLE betters (
--     id INTEGER PRIMARY KEY AUTOINCREMENT,
--     name TEXT NOT NULL
-- );
