[![Built with Django](https://img.shields.io/badge/Built_with-Django-32CD32.svg)](https://www.djangoproject.com/)

## Тестовое задание для Python-разработчика, вариант № 2

Сайт с админ панелью и 2-мя кабинетами (Заказчика и Исполнителя) на Django.

### Установка и запуск:

Чтобы запустить проект локально в контейнерах Docker, выполните следующие шаги:

1. Склонируйте репозиторий с помощью команды:

```
git clone https://github.com/eva-bogd/test_website.git
```

2. В папке проекта infra/ создайте файл .env со следующим содержимым:

```
DB_ENGINE=django.db.backends.postgresql
DB_NAME=postgres
POSTGRES_USER=postgres
POSTGRES_PASSWORD=postgres
DB_HOST=db
DB_PORT=5432
ALLOWED_HOSTS=test_website, localhost, 127.0.0.1
```

3. Запустите контейнеры Docker:

```
docker-compose up --build
```

4. Введите команду для сбора статичных файлов:

```
docker-compose exec test_website python manage.py collectstatic --no-input
```

5. Выполните миграции:

```
docker-compose exec test_website python manage.py makemigrations
docker-compose exec test_website python manage.py migrate
```

6. Создайте суперпользователя:

```
docker-compose exec test_website python manage.py createsuperuser
```

### Технологии:

* Python 3.10
* Django 4.2
* Nginx
* Docker
* PostgresQL

#### Автор: [Богданова Евгения](https://github.com/eva-bogd)