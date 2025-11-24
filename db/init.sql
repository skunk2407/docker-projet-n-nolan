-- Utiliser la base créée par MYSQL_DATABASE
USE bandnames;

CREATE TABLE IF NOT EXISTS adjectives (
  id INT AUTO_INCREMENT PRIMARY KEY,
  word VARCHAR(50) NOT NULL
);

CREATE TABLE IF NOT EXISTS nouns (
  id INT AUTO_INCREMENT PRIMARY KEY,
  word VARCHAR(50) NOT NULL
);

INSERT INTO adjectives (word) VALUES
('Midnight'),
('Last'),
('Golden'),
('Silent'),
('Broken'),
('Electric'),
('Lonely'),
('Wild'),
('Frozen'),
('Furious');

INSERT INTO nouns (word) VALUES
('Llamas'),
('Biscuits'),
('Dreams'),
('Wolves'),
('Echoes'),
('Giants'),
('Drifters'),
('Lights'),
('Roses'),
('Shadows');
