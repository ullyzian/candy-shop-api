-- Creating tables in this folder

BEGIN TRANSACTION;

CREATE TABLE users (
  id serial PRIMARY KEY,
  username VARCHAR(32) NOT NULL
);

COMMIT;