# Yatube 

_API для работы с приложением Yatube_


### Особенности

API позволяет:
- работать с моделью Post: получать список всех сообщений, детали одного сообщения, публиковать новые сообщения, удалять свои личные сообщения
- работать с моделью Group: получать список всех групп, детали одной группы
- работать с моделью Comment: получать список всех комментариев к сообщению, публиковать новые комментарии, удалять свои комментарии
- работать с моделью Follow: получать список своих подписок на других авторов, оформлять новую подписку

Доступ для чтения возможен с моделью Post, Group, Comment. В ином случае доступ через JSON Web Token.


### Стек технологий

- Django
- djangorestframework
- PyJWT
- djoser


### Как запустить приложение

# Клонировать репозиторий и перейти в него в командной строке:

```
git clone https://github.com/Whitenz/api_final_yatube.git
```

```
cd api_final_yatube
```

# Cоздать и активировать виртуальное окружение:

```
python -m venv venv
```

```
source venv/Scripts/activate
```

```
python -m pip install -U pip
```

# Установить зависимости из файла requirements.txt:

```
pip install -r requirements.txt
```

# Выполнить миграции:

```
python manage.py migrate
```

# Запустить проект:

```
python manage.py runserver
```


### Примеры работы с API

# Работа с моделью Post

Список всех постов:
```
$ curl http://127.0.0.1:8000/api/v1/posts/
```

Детали одного поста
```
$ curl http://127.0.0.1:8000/api/v1/posts/1/
```

### License
BSD 3-Clause License

### Author
Ilya Kolesnikov
