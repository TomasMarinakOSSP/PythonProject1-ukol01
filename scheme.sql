CREATE TABLE users (int id PRIMARY KEY,
                    username VARCHAR unique NOT NULL,
                    email VARCHAR unique,
                    password VARCHAR);

INSERT INTO users (username, email, password) VALUES
    ("admin", "admin@email.com", "admin123"),
    ("user", "user@email.com", "user123"),
    ("test","test@email.com", "test123");
