CREATE TABLE chess AS
SELECT *
FROM read_csv_auto("data/chessgame.csv");