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

    def add(self, login, password, full_name, position):
        self.database.send_query("""
        INSERT INTO 
            employee (login, password, full_name, position)
        VALUES
            ('%s', '%s', '%s', '%s')
        """ % (login, password, full_name, position))


    def clear(self):
        self.database.send_query("""
        DELETE FROM employee
        """)