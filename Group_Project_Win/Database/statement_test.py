class StatementTest:
    def __init__(self, database):
        self.database = database
        self.database.send_query("""
        CREATE TABLE IF NOT EXISTS statement_test (
            student_id INT,
            discipline_id INT,
            mark BOOLEAN,
            PRIMARY KEY (student_id, discipline_id))
        """)

    def get_all(self):
        return self.database.send_read_query("""
        SELECT * FROM statement_test
        """)