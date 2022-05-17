# Yatube - простая социальная сеть для блоггеров.


## Особенности
Yatube представляет простую и удобную социальную сеть для публикации личных заметок.  
Зарегистрированные пользователи могут вести свою страницу, наполняя её текстовым и графическим контентом.  
Можно отслеживать публикации других авторов и оформлять подписку на тех, что Вам понравились больше всего.
Схожие по смыслу/тематике публикации могут быть объединены в группы.  
На странице любого сообщения Вы можете оставить свой комментарий.

#### Возможности приложения:
- зарегистрированным пользователям публиковать свои заметки, редактировать их и удалять;
- прикреплять изображения к своим публикациям;
- публиковать заметки как с привязкой к определенной группе, так и без неё; 
- оформлять подписку на любимых авторов, чтобы всегда иметь быстрый доступ к их публикациям;
- комментировать заметки других авторов.

<br>

## Как запустить приложение

#### Запустить командную строку:
<details>
    <summary>Windows</summary>
    Скачайте и установите Git Bash. Подробная инструкция и дистрибутив можно найти на <a href="https://gitforwindows.org/">сайте</a>. Затем в меню пуск найдите и запустите приложение Git Bash.
</details>
<details>
    <summary>macOS или Linux</summary>
    Откройте главное меню приложений и выберите приложение "Терминал".
</details>

<br>

#### Настроить интепретатор Python:
Проверьте, настроена ли ваша среда Python. Рекомендуемая версия Python не ниже 3.7.
```
python3 --version
pip3 --version
```
Если эти пакеты уже установлены, эти команды должны отображать номера версий для каждого пакета, и вы можете перейти к следующему шагу. Если версии не отображаются, то необходимо установить интепретатор Python. Подробную информацию об установке Вы найдете на официальном <a href="https://www.python.org/">Python</a>.

<br>

#### Клонировать репозиторий и перейти в него в командной строке:
```
git clone https://github.com/Whitenz/api_final_yatube.git
```

```
cd api_final_yatube
```

<br>

#### Cоздать и активировать виртуальное окружение:
<details>
    <summary>Windows</summary>
    <pre>python3 -m venv ./venv<br>source ./venv/Scripts/activate</pre>
</details>
<details>
    <summary>macOS или Linux</summary>
    <pre>python3 -m venv ./venv<br>source ./venv/bin/activate</pre>
</details>

<br>

#### Установить зависимости из файла requirements.txt:
```
pip3 install -r requirements.txt
```

<br>

#### Выполнить миграции:
```
python3 manage.py migrate
```

<br>

#### Запустить проект:
```
python3 manage.py runserver
```

<br>

## Взаимодействие через API
- работа с моделью Post - получить список всех заметок, детали одной заметки, опубликовать/отредактировать/обновить/удалить свою заметку
```
    /api/v1/posts/ - GET, POST
    /api/v1/posts/1/ - GET, PUT, PATH, DELETE
```
- работа с моделью Group - получить список всех групп, детали одной группы
```
  /api/v1/groups/ - GET
  /api/v1/groups/1/ - GET
```
- работа с моделью Comment - получить список всех комментариев к заметкам, опубликовать/отредактировать/обновить/удалить свой комментарий
```
  /api/v1/posts/{post_id}/comments/ - GET, POST
  /api/v1/posts/{post_id}/comments/1/ - GET, PUT, PATH, DELETE
```
- работа с моделью Follow - получить список своих подписок на других авторов, оформить новую подписку
```    
    /api/v1/follow/ - GET, POST
```
- работа с JWT-токеном - получить, обновить, проверить токен
```
/api/v1/jwt/create/ - POST
/api/v1/jwt/refresh/ - POST
/api/v1/jwt/verify/ - POST
```

Доступ для чтения возможен с моделью Post, Group, Comment. В ином случае доступ через JSON Web Token.

<br>

#### Работа с API на примере модели Post:

Список всех постов
```
$ curl http://127.0.0.1:8000/api/v1/posts/
```
Ответ
```
[
    {
        "id": 1,
        "author": "Ilya",
        "text": "Тестовый пост №1",
        "pub_date": "2022-05-12T16:29:40.879969Z",
        "image": null,
        "group": null
    }
]
```

Детали одного поста
```
$ curl http://127.0.0.1:8000/api/v1/posts/1/
```
Ответ
```
{
    "id": 1,
    "author": "Ilya",
    "text": "Тестовый пост №1",
    "pub_date": "2022-05-12T16:29:40.879969Z",
    "image": null,
    "group": null
}
```

Добавить новый пост
```
$ curl --location --request POST 'http://127.0.0.1:8000/api/v1/posts/' \
--header 'Authorization: Bearer YOUR_TOKEN' \
--header 'Content-Type: application/json' \
--data-raw '{
    "text": "Тестовое сообщение."
}'
```
Ответ
```
{
    "id": 2,
    "author": "Ilya",
    "text": "Тестовый пост №2",
    "pub_date": "2022-05-17T13:28:57.215016Z",
    "image": null,
    "group": "Тестовая группа"
}
```

Удалить свой пост
```
$ curl --location --request DELETE 'http://127.0.0.1:8000/api/v1/posts/1/' \
--header 'Authorization: Bearer YOUR_TOKEN' \
--data-raw ''
```

<br>

## Стек технологий
- Django
- djangorestframework
- PyJWT
- djoser

<br>

## Лицензия
BSD 3-Clause License

<br>

## Автор
Ilya Kolesnikov