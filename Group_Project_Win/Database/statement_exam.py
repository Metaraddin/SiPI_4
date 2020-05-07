import psycopg2 as psql


class StatementExam:
    def __init__(self, database):
        self.database = database
        self.database.send_query("""
        CREATE TABLE IF NOT EXISTS statement_exam (
            student_id INT REFERENCES student (id) ON DELETE CASCADE,
            discipline_id INT REFERENCES discipline (id) ON DELETE CASCADE,
            mark INT,
            PRIMARY KEY (student_id, discipline_id))
        """)

    def get_all(self):
        return self.database.send_read_query("""
        SELECT * FROM statement_exam
        """)

    def get_student(self, student_id):
        return self.database.send_read_query("""
        SELECT d.id, d.name, 'Экзамен', se.mark, d.semester
        FROM discipline as d
        JOIN statement_exam as se on d.id = se.discipline_id
        WHERE se.student_id = '%s'
        """ % student_id)

    def add(self, student_id, discipline_id, mark):
        try:
            self.database.send_query("""
            INSERT INTO 
                statement_exam (student_id, discipline_id, mark)
            VALUES
                (%s, %s, %s)
            """ % (student_id, discipline_id, mark))
        except psql.errors.UniqueViolation:
            pass

    def clear(self):
        self.database.send_query("""
        DELETE FROM statement_exam
        """)