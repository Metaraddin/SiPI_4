class Employee:
    def __init__(self, database):
        self.database = database
        self.database.send_query("""
        CREATE TABLE IF NOT EXISTS employee (
            login TEXT PRIMARY KEY,
            password TEXT NOT NULL,
            full_name TEXT NOT NULL,
            position TEXT NOT NULL)
        """)

    def get_all(self):
        return self.database.send_read_query("""
        SELECT login, full_name, position FROM employee
        """)

    def set(self, last_login, login, full_name, position):
        self.database.send_query("""
        UPDATE employee SET login = '%s', full_name = '%s', position = '%s'
        WHERE login = '%s'
        """ % (login, full_name, position, last_login))

    def get_employee(self, login):
        return self.database.send_read_query("""
        SELECT login, full_name, position FROM employee
        WHERE login = '%s'
        """ % login)

    def add(self, login, password, full_name, position):
        self.database.send_query("""
        INSERT INTO 
            employee (login, password, full_name, position)
        VALUES
            ('%s', '%s', '%s', '%s')
        """ % (login, password, full_name, position))

    def delete(self, login):
        self.database.send_query("""
        DELETE FROM employee WHERE login = '%s'
        """ % login)

    def clear(self):
        self.database.send_query("""
        DELETE FROM employee
        """)