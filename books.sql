CREATE DATABASE IF NOT EXISTS library;

USE library;

CREATE TABLE IF NOT EXISTS books (
    id INT AUTO_INCREMENT PRIMARY KEY,
    title VARCHAR(255) NOT NULL,
    author VARCHAR(255) NOT NULL,
    about TEXT,
    first_chapter TEXT
);


INSERT INTO books (title, author, about, first_chapter) VALUES (
    'Harry Potter and the Sorcerer\'s Stone',
    'J.K. Rowling',
    'The first book in the Harry Potter series.',
    'Mr. and Mrs. Dursley, of number four, Privet Drive...'
);

INSERT INTO books (title, author, about, first_chapter) VALUES (
    'To Kill a Mockingbird',
    'Harper Lee',
    'A classic novel exploring racial injustice and moral growth.',
    'When he was nearly thirteen, my brother Jem got his arm badly broken...'
);

