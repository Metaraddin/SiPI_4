import storage
import random

disciplines = {
    'Архитектура': ['Архитектура', 'Строительство', 'Ландшафтный дизайн', 'Планирование'],
    'Бизнес и менеджмент': ['Бизнес', 'Маркетинг', 'Менеджмент', 'Управление кадровыми ресурсами', 'Финансы',
                            'Бухгалтерский учёт', 'Туризм', 'Гостиничное дело', 'Рекреация', 'Транспорт',
                            'Канцелярия и делопроизводство'],
    'Биологические науки': ['Биология', 'Зоология', 'Генетика', 'Микробиология', 'Молекулярная биология',
                            'Ботаника', 'Спортивная биология', 'Медицина', 'Психология'],
    'Естественные науки': ['Химия', 'Физика', 'Астрономия', 'Геология', 'Материаловедение'],
    'Здравоохранение': ['Медицина', 'Стоматология', 'Анатомия', 'Физиология', 'Патология', 'Фармакология',
                        'Токсикология', 'Фармацевтика', 'Медсестринское дело', 'Нетрадиционная медицина',
                        'Диетология', 'Офтальмология', 'Медицинские технологии'],
    'Искусстово и дизайн': ['Изобразительное искусство', 'Исследования в области дизайна', 'Музыка',
                            'Театр и драматическое искусство', 'Танец и хореография', 'Кинематография и фотография',
                            'Творческое письмо', 'Ремесла'],
    'История и философия': ['История по периодам', 'История по географическим регионам', 'История по темам',
                            'Археология', 'Философия', 'Теология и религиозные исследования'],
    'Математика и вычислительная техника': ['Математика', 'Статистика', 'Исследования операций', 'Компьютерные науки',
                                            'Информационные системы', 'Системное программирование',
                                            'Искусственный интеллект']
}


def disciplines_set(kit):
    for i in kit:
        for j in kit[i]:
            semester = random.randint(1, 5)
            for k in range(random.randint(1, 3)):
                storage.discipline.add(j, semester + k)
