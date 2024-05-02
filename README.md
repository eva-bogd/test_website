[![Built with Django](https://img.shields.io/badge/Built_with-Django-32CD32.svg)](https://www.djangoproject.com/)

## Тестовое задание для Python-разработчика, вариант № 2

Сайт с админ панелью и 2-мя кабинетами (Заказчика и Исполнителя) на Django.
Реализованы следующие функции:
- Регистрация пользователя;
- Обновление/изменение данных профиля пользователя;
- Восстановление пароля (через эмуляцию почтового сервера);
- Просмотр моих услуг и моих заказов в профиле пользователя;
- Создание услуги в профиле Исполнителя;
- Редактирование/удаление услуги при переходе на страницу услуги;
- Заказ выбранной услуги при переходе на страницу услуги;
- Изменение статуса заказа Исполнителем/Заказчиком при переходе на страницу заказа.

### Установка и запуск:

Проект можно запустить в контейнерах с помощью Docker Compose, для этого должен быть установлен Docker Compose.
Чтобы запустить проект локально в контейнерах Docker, выполните следующие шаги:

1. Склонируйте репозиторий с помощью команды:

```
git clone https://github.com/eva-bogd/test_website.git
```

2. В папке проекта infra/ создайте файл .env со следующим содержимым:

```
DB_ENGINE=django.db.backends.postgresql
DB_NAME=testtaskdb
POSTGRES_USER=postgres
POSTGRES_PASSWORD=postgres
DB_HOST=db
DB_PORT=5432
ALLOWED_HOSTS=web,localhost,127.0.0.1
```

3. Запустите контейнеры Docker из папки infra/:

```
docker-compose up --build -d
```

4. Введите команду для сбора статичных файлов:

```
docker-compose exec web python manage.py collectstatic --no-input
```

5. Создайте пустую базу и загрузите туда бэкап с тестовой базой:

```
docker compose exec -T -u postgres db psql -c "CREATE DATABASE testtaskdb"
```
```
cat testtaskdb_backup.dump | docker compose exec -T -u postgres db psql -d testtaskdb
```

6. Логин и пароль для доступа в админку:
```
Логин: admin
Пароль: 123
```
Тестовый пользователь:
```
Логин: tima
Пароль: fdsa4321
```
Ссылка на сайт при локальном запуске: http://localhost/
Ссылска на админ панель при локальном запуске: http://localhost/admin/


### Технологии:

* Python 3.10
* Django 4.2
* Nginx
* Docker
* PostgresQL

#### Автор: [Богданова Евгения](https://github.com/eva-bogd)