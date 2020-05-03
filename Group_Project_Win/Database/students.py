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
        SELECT  FROM student
        """)

    def get_group(self, group_id):
        return self.database.send_read_query("""
        SELECT id, full_name, budgetary_basis FROM student
        WHERE group_id = '%s'
        """ % group_id)

    def get_student(self, id):
        return self.database.send_read_query("""
        SELECT * FROM student
        WHERE id = '%s'
        """ % id)

    def add(self, group_id, full_name, budgetary_basis):
        self.database.send_query("""
        INSERT INTO
            student (group_id, full_name, budgetary_basis)
        VALUES
            (%s, '%s', %s)
        """ % (group_id, full_name, budgetary_basis))