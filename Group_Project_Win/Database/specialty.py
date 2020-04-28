class Specialty:
    def __init__(self, database):
        self.database = database
        self.database.send_query("""
        CREATE TABLE IF NOT EXISTS specialty (
            id SERIAL PRIMARY KEY,
            name TEXT NOT NULL)
        """)

    def get_all(self):
        return self.database.send_read_query("""
        SELECT * FROM specialty
        """)