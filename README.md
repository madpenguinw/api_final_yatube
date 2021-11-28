# API для Yatube
## Технологии 
- Python 3.9
- Django 2.2.16
- DRF 3.12.4
- JWT
- Joser
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
```
- в той же папке запустите проект
```
python manage.py runserver
```
## Автор
Соколов М.А.
