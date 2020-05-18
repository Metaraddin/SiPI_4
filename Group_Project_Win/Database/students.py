class Student:
    def __init__(self, database):
        self.database = database
        self.database.send_query("""
        CREATE TABLE IF NOT EXISTS student (
            id SERIAL PRIMARY KEY,
            group_id INT REFERENCES groups (id) ON DELETE CASCADE,
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
        WHERE id = %s
        """ % id)

    def add(self, group_id, full_name, budgetary_basis):
        return self.database.send_read_query("""
        INSERT INTO
            student (group_id, full_name, budgetary_basis)
        VALUES
            (%s, '%s', %s)
        RETURNING id
        """ % (group_id, full_name, budgetary_basis))

    def delete(self, id):
        self.database.send_query("""
        DELETE FROM student WHERE id = '%s'
        """ % id)

    def clear(self):
        self.database.send_query("""
        DELETE FROM student
        """)

    def reset_id(self):
        self.database.send_query("""
        ALTER SEQUENCE student_id_seq RESTART
        """)