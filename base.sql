CREATE TABLE authors (
  Id INT NOT NULL AUTO_INCREMENT,
  first_name VARCHAR(50) NOT NULL,
  last_name VARCHAR(50) NOT NULL,
  PRIMARY KEY (id)
);

INSERT INTO authors (first_name, last_name) VALUES ('Александр', 'Пушкин');
INSERT INTO authors (first_name, last_name) VALUES ('Лев', 'Толстой');
INSERT INTO authors (first_name, last_name) VALUES ('Сергей', 'Есенин');

CREATE TABLE references_table (
  Id INT NOT NULL AUTO_INCREMENT,
  name VARCHAR(100) NOT NULL,
  PRIMARY KEY (id)
);

CREATE TABLE publisher (
  Id INT NOT NULL AUTO_INCREMENT,
  name VARCHAR(100) NOT NULL,
  PRIMARY KEY (id)
);

INSERT INTO publisher (id, name) VALUES ('01', 'Эксмо');
INSERT INTO publisher (id, name) VALUES ('02', 'Росмэн');

CREATE TABLE books (
  Id INT NOT NULL AUTO_INCREMENT,
  title VARCHAR(100) NOT NULL,
  author_id INT,
  publisher_id INT,
  year INT NOT NULL,
  PRIMARY KEY (id),
  FOREIGN KEY (author_id) REFERENCES authors(Id),
  FOREIGN KEY (publisher_id) REFERENCES publisher(Id)
);

INSERT INTO books (Id, title, author_id, publisher_id, year) VALUES ('01', 'Война и мир', '01', '01', '2000');
INSERT INTO books (Id, title, author_id, publisher_id, year) VALUES ('02', 'Алые паруса', '02', '02', '2003');
INSERT INTO books (Id, title, author_id, publisher_id, year) VALUES ('03', 'Капитанская дочка', '02', '02', '2005');
INSERT INTO books (Id, title, author_id, publisher_id, year) VALUES ('04', 'Мой друг вампир', '01', '01', '2010');

UPDATE books
SET year = '2007'
WHERE year = '2005';

DELETE from books
WHERE year < '2006';

SELECT * FROM books


