class Employee:
    def __init__(self, database):
        self.database = database
        self.database.send_query("""
        CREATE TABLE IF NOT EXISTS employee (
            login TEXT PRIMARY KEY,
            password TEXT NOT NULL,
            access TEXT NOT NULL,
            full_name TEXT NOT NULL,
            position TEXT NOT NULL)
        """)

    def get_all(self):
        return self.database.send_read_query("""
        SELECT * FROM group
        """)