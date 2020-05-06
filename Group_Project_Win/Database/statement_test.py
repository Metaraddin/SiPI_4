class StatementTest:
    def __init__(self, database):
        self.database = database
        self.database.send_query("""
        CREATE TABLE IF NOT EXISTS statement_test (
            student_id INT REFERENCES student (id),
            discipline_id INT REFERENCES discipline (id),
            mark BOOLEAN,
            PRIMARY KEY (student_id, discipline_id))
        """)

    def get_all(self):
        return self.database.send_read_query("""
        SELECT * FROM statement_test
        """)

    def get_student(self, student_id):
        return self.database.send_read_query("""
        SELECT d.id, d.name, 'Зачёт', st.mark, d.semester
        FROM discipline as d
        JOIN statement_test as st on d.id = st.discipline_id
        WHERE st.student_id = '%s'
        """ % student_id)