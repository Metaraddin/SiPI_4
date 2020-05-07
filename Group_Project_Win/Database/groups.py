class Groups:
    def __init__(self, database):
        self.database = database
        self.database.send_query("""
        CREATE TABLE IF NOT EXISTS groups (
            id SERIAL PRIMARY KEY,
            faculty TEXT NOT NULL,
            specialty TEXT NOT NULL,
            receipt_year INT NOT NULL)
        """)

    def get_all(self):
        return self.database.send_read_query("""
        SELECT * FROM groups
        """)

    def get_group(self, id):
        return self.database.send_read_query("""
        SELECT * FROM groups
        WHERE id = %s
        """ % id)

    def add(self, faculty, specialty, receipt_year):
        return self.database.send_read_query("""
        INSERT INTO 
            groups (faculty, specialty, receipt_year)
        VALUES
            ('%s', '%s', %s)
        RETURNING id
        """ % (faculty, specialty, receipt_year))

    def clear(self):
        self.database.send_query("""
        DELETE FROM groups
        """)