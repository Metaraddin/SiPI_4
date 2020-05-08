class Discipline:
    def __init__(self, database):
        self.database = database
        self.database.send_query("""
        CREATE TABLE IF NOT EXISTS discipline (
            id SERIAL PRIMARY KEY,
            name TEXT NOT NULL,
            semester INT NOT NULL)
        """)

    def get_all(self):
        return self.database.send_read_query("""
        SELECT * FROM discipline
        """)

    def add(self, name, semester):
        self.database.send_query("""
        INSERT INTO 
            discipline (name, semester)
        VALUES
            ('%s', %s)
        """ % (name, semester))

    def delete(self, id):
        self.database.send_query("""
        DELETE FROM discipline WHERE id = '%s'
        """ % id)

    def clear(self):
        self.database.send_query("""
        DELETE FROM discipline;
        """)

    def reset_id(self):
        self.database.send_query("""
        ALTER SEQUENCE discipline_id_seq RESTART
        """)
