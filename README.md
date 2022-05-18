# DJANGO STRIPE PAYMENTS

# Как запустить проект:
- Установите Docker, инструкция:
https://docs.docker.com/get-docker/

- Установите docker-compose, инструкция:
https://docs.docker.com/compose/install/

- Клонируйте репозиторий:
```
git clone git@github.com:ilyarogozin/djangostripe.git
```

- Создайте файл окружения .env, который будет содержать:
```
SECRET_KEY='mlm-f6@nj48d4icz398^0q)jer2-cno%a2xqdvnp*m9e$=(m&!'
DB_ENGINE=django.db.backends.postgresql
DB_NAME=postgres
POSTGRES_USER=postgres
POSTGRES_PASSWORD=postgres
DB_HOST=db
DB_PORT=5432
ALLOWED_HOSTS='127.0.0.1 localhost'
STRIPE_PUBLISHABLE_KEY='pk_test_51L01abLTHZwUh0U3a4yzp3Ndbi8CLCvkjMoPpQci3vaCY3CWumi3BhtdwGRI8MpL2EbgffnvYFdjpvUjMRuMhKsg00zlVyHIAK'
STRIPE_SECRET_KEY='sk_test_51L01abLTHZwUh0U3J7j4VlHcTnlNxReM6hWIYV1fboJgpJ84YAaTZ73iNr0dpSGV9ojlzN1hxEK3F7ONaWLkSSRj00lIfEVp6S'

```

- Соберите контейнеры и запустите их:
```
docker-compose up -d --build
```

- Выполните миграции:
```
docker-compose exec web python manage.py makemigrations
docker-compose exec web python manage.py migrate
```

- Создайте суперпользователя, чтобы зайти в админку:
```
docker-compose exec web python manage.py createsuperuser
```

- Соберите статику:
```
docker-compose exec web python manage.py collectstatic --no-input
```

- Заполните БД начальными данными:
```
docker-compose exec web python manage.py loadjson --path 'data/items.json'
```
В БД сейчас только один предмет с id=1

## Адрес тестирования:
http://localhost/item/1/

## Админка:
http://localhost/admin/

## Проект запущен на удалённом сервере, адреса для тестирования:
http://51.250.70.25/item/1/
http://51.250.70.25/admin/

### Логин и пароль админки:
login: admin
password: admin
