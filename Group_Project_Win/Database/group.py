class Group:
    def __init__(self, database):
        self.database = database
        self.database.send_query("""
        CREATE TABLE IF NOT EXISTS group (
            id SERIAL PRIMARY KEY,
            faculty_id INT NOT NULL,
            specialty_id INT NOT NULL,
            receipt_year INT NOT NULL)
        """)

    def get_all(self):
        return self.database.send_read_query("""
        SELECT * FROM group
        """)