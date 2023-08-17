CREATE TABLE IF NOT EXISTS books (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title VARCHAR(255) NOT NULL,
    author VARCHAR(255) NOT NULL,
    about TEXT,
    book BLOOB
);


INSERT INTO books (title, author, about, book) VALUES (
    'Harry Potter and the Sorcerers Stone',
    'J.K. Rowling',
    'The first book in the Harry Potter series.',
    'Mr. and Mrs. Dursley, of number four, Privet Drive...'
);

INSERT INTO books (title, author, about, book) VALUES (
    'To Kill a Mockingbird',
    'Harper Lee',
    'A classic novel exploring racial injustice and moral growth.',
    'When he was nearly thirteen, my brother Jem got his arm badly broken...'
);

