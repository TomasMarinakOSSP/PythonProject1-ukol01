CREATE TABLE users (
    id INTEGER PRIMARY KEY,
    username VARCHAR UNIQUE NOT NULL,
    email VARCHAR UNIQUE,
    password VARCHAR,
    role VARCHAR NOT NULL
);

INSERT INTO users (username, email, password, role) VALUES
    ("admin", "admin@email.com", "admin123", "admin"),
    ("user", "user@email.com", "user123", "user"),
    ("test", "test@email.com", "test123", "user");