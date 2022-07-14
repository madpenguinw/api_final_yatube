# API для Yatube
Социальная сеть в которой пользователи могут
публиковать записи, комментировать записи, а так же подписываться или отписываться от авторов.
## Технологии 
- Python 3.9
- Django 2.2.16
- DRF 3.12.4
- JWT
- Djoser
## Запуск проекта в dev-режиме
- установите и запустите виртуальное окружение
```
python -m venv venv
```
```
. venv/Scripts/activate
```
- установите зависимости из requirements.txt
```
pip install -r requirements.txt
```
- в папке с файлом manage.py выполните миграции:
```
python manage.py migrate
- создайте супрепользователя:
```
python manage.py createsuperuser
```
```
- в той же папке запустите проект
```
python manage.py runserver
```
### Примеры работы с API для всех пользователей
Для неавторизованных пользователей работа с API доступна в режиме чтения,
что-либо изменить или создать не получится.
```
GET api/v1/posts/ - получить список всех публикаций.
При указании параметров limit и offset выдача должна работать с пагинацией
GET api/v1/posts/{id}/ - получение публикации по id

GET api/v1/groups/ - получение списка доступных сообществ
GET api/v1/groups/{id}/ - получение информации о сообществе по id

GET api/v1/{post_id}/comments/ - получение всех комментариев к публикации
GET api/v1/{post_id}/comments/{id}/ - Получение комментария к публикации по id
```
### Примеры работы с API для авторизованных пользователей
Для создания публикации используем:
```
POST /api/v1/posts/
```
в body
{
"text": "string",
"image": "string",
"group": 0
}

Обновление публикации:
```
PUT /api/v1/posts/{id}/
```
в body
{
"text": "string",
"image": "string",
"group": 0
}

Частичное обновление публикации:
```
PATCH /api/v1/posts/{id}/
```
в body
{
"text": "string",
"image": "string",
"group": 0
}

Частичное обновление публикации:
```
DEL /api/v1/posts/{id}/
```
Получение доступа к эндпоинту /api/v1/follow/
(подписки) доступен только для авторизованных пользователей.
```
GET /api/v1/follow/ - подписка пользователя от имени которого сделан запрос
на пользователя переданного в теле запроса. Анонимные запросы запрещены.
```
- Авторизованные пользователи могут создавать посты,
комментировать их и подписываться на других пользователей.
- Пользователи могут изменять(удалять) контент, автором которого они являются.

### Добавить группу в проект нужно через админ панель Django:
```
admin/ - после авторизации, переходим в раздел Groups и создаем группы
```
Доступ авторизованным пользователем доступен по JWT-токену (Joser),
который можно получить выполнив POST запрос по адресу:
```bash
POST /api/v1/jwt/create/
```
Передав в body данные пользователя (например в postman):
```
{
"username": "string",
"password": "string"
}
```
Полученный токен добавляем в headers (postman), после чего буду доступны все функции проекта:
```
Authorization: Bearer {your_token}
```
Обновить JWT-токен:
```
POST /api/v1/jwt/refresh/ - обновление JWT-токена
```
Проверить JWT-токен:
```
POST /api/v1/jwt/verify/ - проверка JWT-токена
```
Так же в проекте API реализована пагинация (LimitOffsetPagination):
```
GET /api/v1/posts/?limit=5&offset=0 - пагинация на 5 постов, начиная с первого
```
## Автор
Соколов М.А.
