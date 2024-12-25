CREATE TABLE IF NOT EXISTS users(
	id SERIAL PRIMARY KEY,
	fio VARCHAR(50) NOT NULL,
	email VARCHAR(100) NOT NULL UNIQUE
);

INSERT INTO users (fio, email) VALUES ('Зубенко Михаил Петрович', 'mafioznik@gmail.com');
