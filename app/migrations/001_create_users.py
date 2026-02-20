from yoyo import step

steps = [
    step(
        "CREATE TABLE IF NOT EXISTS user_model (id SERIAL PRIMARY KEY, name VARCHAR(80) NOT NULL, email VARCHAR(120) UNIQUE NOT NULL)",
        "DROP TABLE user_model"
    )
]