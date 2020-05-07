import storage
import random


class generator:
    program = {
        'ФАИ': {
            'Архитектура': ['Архитектура', 'Строительство', 'Ландшафтный дизайн', 'Планирование'],
            'Искусстово и дизайн': ['Изобразительное искусство', 'Исследования в области дизайна', 'Музыка', 'Театр и драматическое искусство', 'Танец и хореография', 'Кинематография и фотография', 'Творческое письмо', 'Ремесла']
        },
        'ИО': {
            'Бизнес и менеджмент': ['Бизнес', 'Маркетинг', 'Менеджмент', 'Управление кадровыми ресурсами', 'Финансы', 'Бухгалтерский учёт', 'Туризм', 'Гостиничное дело', 'Рекреация', 'Транспорт', 'Канцелярия и делопроизводство'],
            'История и философия': ['История по периодам', 'История по географическим регионам', 'История по темам', 'Археология', 'Философия', 'Теология и религиозные исследования']
        },
        'ИЕН': {
            'Биологические науки': ['Биология', 'Зоология', 'Генетика', 'Микробиология', 'Молекулярная биология', 'Ботаника', 'Спортивная биология', 'Медицина', 'Психология'],
            'Естественные науки': ['Химия', 'Физика', 'Астрономия', 'Геология', 'Материаловедение'],
            'Здравоохранение': ['Медицина', 'Стоматология', 'Анатомия', 'Физиология', 'Патология', 'Фармакология', 'Токсикология', 'Фармацевтика', 'Медсестринское дело', 'Нетрадиционная медицина', 'Диетология', 'Офтальмология', 'Медицинские технологии']
        },
        'ТИ': {
            'Математика и вычислительная техника': ['Математика', 'Статистика', 'Исследования операций', 'Компьютерные науки', 'Информационные системы', 'Системное программирование', 'Искусственный интеллект']
        }
    }

    first_names = [
        ['Адам', 'Аарон', 'Авраам', 'Богдан', 'Вит', 'Генрих', 'Гамлет', 'Герман', 'Давид', 'Добрыня', 'Евдоким', 'Елисей', 'Жерар', 'Зигмунд', 'Иероним', 'Игнатий', 'Ираклий', 'Ким', 'Кузьма', 'Коре', 'Леон', 'Людвиг', 'Лука'],
        ['Ава', 'Аврора', 'Бажена', 'Беатрис', 'Бела', 'Бьянка', 'Виталина', 'Варвара', 'Галия', 'Грета', 'Гульнара', 'Диана', 'Дина', 'Домника', 'Ева', 'Зара', 'Искра', 'Кира', 'Лия', 'Люция', 'Сара']
    ]

    last_names = [
        ['Иванов', 'Смирнов', 'Кузнецов', 'Попов', 'Васильев', 'Петров', 'Соколов', 'Михайлов', 'Алексеев', 'Семенов', 'Козлов', 'Зайцев', 'Лебедев', 'Орлов', 'Фролов', 'Киселёв', 'Навальный', 'Сорокин', 'Белов', 'Антонов', ],
        ['Иванова', 'Смирнова', 'Кузнецова', 'Попова', 'Васильева', 'Петрова', 'Соколова', 'Михайлова', 'Алексеева', 'Семенова', 'Козлова', 'Зайцева', 'Лебедева', 'Орлова', 'Фролова', 'Килесёва', 'Навальная', 'Сорокина', 'Белова', 'Антонова', ]
    ]

    patronymic = [
        ['Александрович', 'Алексеевич', 'Вольфович', 'Ильич', 'Львович', 'Юрьевич', 'Ярославович', 'Станиславович', 'Семенович', 'Леонидович', 'Денисович', 'Борисович'],
        ['Александровна', 'Алексеевна', 'Вольфовна', 'Ильина', 'Львовна', 'Юрьевна', 'Ярославовна', 'Станиславовна', 'Семеновна', 'Леонидовна', 'Денисовна', 'Борисовна']
    ]

    logins = ['bar', 'sai', 'tomi', 'faem', 'vorn', 'barg', 'fegal', 'gromi', 'bazel', 'vogis', 'bobor']

    positions = ['Лаборант', 'Ассистент', 'Младший преподаватель', 'Преподаватель', 'Старший преподаватель', 'Заведующий кафедрой']

    def __init__(self, group_count=100):
        storage.discipline.clear()
        storage.employee.clear()
        storage.groups.clear()
        storage.statement_exam.clear()
        storage.statement_test.clear()
        storage.student.clear()

        self.__employees_set()
        self.disciplines = self.__disciplines_add()
        for i in range(group_count):
            self.__group_set()

    def __gen_full_name(self):
        sex = random.randint(0, 1)
        return '%s %s %s' % (
                random.choice(self.first_names[sex]),
                random.choice(self.last_names[sex]),
                random.choice(self.patronymic[sex])
            )

    def __employees_set(self):
        for login in self.logins:
            password = '000000'
            full_name = self.__gen_full_name()
            position = random.choice(self.positions)
            storage.employee.add(login, password, full_name, position)

    def __disciplines_add(self):
        for faculty in self.program:
            for specialty in self.program[faculty]:
                for discipline in self.program[faculty][specialty]:
                    semester = random.randint(1, 5)
                    for n in range(random.randint(1, 3)):
                        storage.discipline.add(discipline, semester + n)
        return storage.discipline.get_all()

    def __group_set(self, min_year=2016, max_yer=2020):
        faculty = random.choice(list(self.program))
        specialty = random.choice(list(self.program[faculty]))
        year = random.randint(min_year, max_yer)
        group_id = storage.groups.add(faculty, specialty, year)[0][0]
        for i in range(random.randint(15, 30)):
            full_name = self.__gen_full_name()
            student_id = storage.student.add(group_id, full_name, random.choice([True, False]))[0][0]
            for discipline in self.program[faculty][specialty]:
                for db_discipline in self.disciplines:
                    if db_discipline[1] == discipline:
                        if random.choice([True, False]):
                            mark = random.choice(['Null', True, False])
                            storage.statement_test.add(student_id, db_discipline[0], mark)
                        else:
                            mark = random.choice(['Null', random.randint(2, 5)])
                            storage.statement_exam.add(student_id, db_discipline[0], mark)

