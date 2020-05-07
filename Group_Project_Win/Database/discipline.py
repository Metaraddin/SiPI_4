import psycopg2 as psql

class Discipline:
    def __init__(self, database):
        self.database = database
        self.database.send_query("""
        CREATE TABLE IF NOT EXISTS discipline (
            id SERIAL PRIMARY KEY,
            name TEXT NOT NULL UNIQUE,
            semester INT NOT NULL)
        """)

    def get_all(self):
        return self.database.send_read_query("""
        SELECT * FROM discipline
        """)

    def add(self, name, semester):
        try:
            self.database.send_query("""
            INSERT INTO 
                discipline (name, semester)
            VALUES
                ('%s', %s)
            """ % (name, semester))
        except psql.errors.UniqueViolation:
            pass

    def clear(self):
        self.database.send_query("""
        DELETE FROM discipline
        """)
