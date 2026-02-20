from yoyo import step

steps = [
    step(
        "ALTER TABLE user_model ADD COLUMN phone VARCHAR(20)",
        "ALTER TABLE user_model DROP COLUMN phone"
    )
]