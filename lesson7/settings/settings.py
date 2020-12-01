class Settings:
    def __init__(self):
        self.create_student_table = """
            CREATE TABLE IF NOT EXISTS students(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            first_name TEXT NOT NULL,
            last_name TEXT NOT NULL,
            group_id INTEGER NOT NULL,
            ticket_id INTEGER NOT NULL,
            FOREIGN KEY(ticket_id) REFERENCES tickets(id),
            FOREIGN KEY(group_id) REFERENCES groups(id)
            )
        """
        self.create_ticket_table = """
            CREATE TABLE IF NOT EXISTS tickets(
            id INTEGER PRIMARY KEY AUTOINCREMENT
            )
        """
        self.create_group_table = """
            CREATE TABLE IF NOT EXISTS groups(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                faculty_id INTEGER NOT NULL,
                FOREIGN KEY(faculty_id) REFERENCES faculty(id)
            )
        """
        self.create_faculty_table = """
            CREATE TABLE IF NOT EXISTS faculty(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL                
            )
        """
        self.create_grade_table = """
            CREATE TABLE IF NOT EXISTS grade(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                score INTEGER NOT NULL,
                ticket_id INTEGER NOT NULL,
                FOREIGN KEY(ticket_id) REFERENCES tickets(id)
                CHECK (score > 0 AND score <= 12)
            )
        """

        self.db_name = 'students.db'

        self.faculty = {
            'Mathematic': ['mat_1', 'mat_2'],
            'Economic': ['eco_1'],
            'Biologic': ['bio_1', 'bio_2'],
            'Programing': ['prg_1', 'prg_2', 'prg_3'],
            'Building': ['bld_1'],
        }
        self.students = [
            ['Alan', 'A', 'Mathematic', 'mat_1'],
            ['Dilan', 'D', 'Economic', 'eco_1'],
            ['Rebecca', 'R', 'Economic', 'eco_1'],
            ['Anita', 'A', 'Biologic', 'bio_1'],
            ['Jack', 'J', 'Biologic', 'bio_1'],
            ['Michel', 'M', 'Biologic', 'bio_2'],
            ['Nona', 'N', 'Programing', 'prg_1'],
            ['Vanessa', 'V', 'Programing', 'prg_1'],
            ['Erich', 'E', 'Building', 'bld_1'],
            ['John', 'J', 'Mathematic', 'mat_2'],
        ]

