main_menu = '''\nГлавное меню:
    1. Открыть файл
    2. Сохранить файл
    3. Показать контакты
    4. Добавить контакт
    5. Найти
    6. Изменить
    7. Удалить
    8. Выход\n'''

input_choice = 'Выберите пункт меню: '

load_successful = 'Телефонная книга успешно открыта!'
save_successful = 'Телефонная книга сохранена'
pb_empty = 'Телефонная книга пуста или не загружена!'
input_new_contact = ['Введите данные нового контакта']
new_contact = {'name': 'Введите имя: ',
                'phone': 'Введите телефон: ',
               'comment': 'Введите коментарий: '}
input_search = 'Что будем искать: '
def new_contact_successful(name: str):
    return f'Контакт {name} успешно добавлен'
def empty_search(word) -> str:
    return f'Контакты содержащие слово "{word} не найдены!'

input_change = 'Какой контакт будем менять: '

input_index = 'Введите индекс контакта: '

change_contact = 'Введите новые данные или оставьте поле пустым, чтобы не менять: '

def change_successful(name: str) -> str:
    return f'Контакт {name} успешно изменен!'