class Student:
    def __init__(self, database):
        self.database = database
        self.database.send_query("""
        CREATE TABLE IF NOT EXISTS student (
            id SERIAL PRIMARY KEY,
            group_id INT NOT NULL,
            full_name TEXT NOT NULL,
            budgetary_basis BOOLEAN NOT NULL)
        """)

    def get_all(self):
        return self.database.send_read_query("""
        SELECT * FROM student
        """)

    def add(self, group_id, full_name, budgetary_basis):
        self.database.send_query("""
        INSERT INTO
            student (group_id, full_name, budgetary_basis)
        VALUES
            (%s, '%s', %s)
        """ % (group_id, full_name, budgetary_basis))