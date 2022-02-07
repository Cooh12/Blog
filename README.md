# Привет гость!!

Перед тобой мой первый учебный проект выполненый на Django, да и первый в принипе😅

## О проекте
Данный проект представляет из себя чатоблогосоциальную сеть🙂 
 
 В проекте реализованы следующие функции:

- Регистрация пользователей
- Регестрация через соц.сети(vk, google, github)
- Редактирование профиля пользователя
- Публикация/редактирование постов
- Реализована система лайков/закладок/комментариев постов(система может распространяться на любую желаюмую модель, но пока не распространяется🙃) 
- Реализована система отправки сообщений между пользователями(в дальнийшем мб сделаю чаты)

## Устновка проекта
Python 3.8
1. Устанавливаем виртуалку-  `python -m venv venv`
2. Активируем вируталку - `source venv/Scripts/activate`
3. Аппгрейд pip - `python -m pip install --upgrade pip`(на всякий случай)
4. Установить зависимости - `pip install -r requirements.txt`
5. Запустить - `python manage.py migrate`
6. Запустить -`python manage.py loaddata db.json`(чтобы предзаполнить БД)

логин: admin
пасс:12345
от одной учетки из БД

i
