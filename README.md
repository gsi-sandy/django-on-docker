# django-on-docker

#### Clone repository

````
git clone https://github.com/gsi-sandy/django-on-docker.git
````

#### Add ENV 
1. Create ENV file into project root.

2. Add into the file:

    ````
    DEBUG=1
    SECRET_KEY=secretkey
    DJANGO_ALLOWED_HOSTS=localhost 127.0.0.1 [::1]
    SQL_ENGINE=django.db.backends.postgresql
    SQL_DATABASE=hello_django_dev
    SQL_USER=hello_django
    SQL_PASSWORD=hello_django
    SQL_HOST=db
    SQL_PORT=5432
    DATABASE=postgres
    ````
    
#### Install
1. Create containers
    ````
    docker-compose up -d --build
    ````

2. Run migrations
    ````
    docker-compose exec web python manage.py migrate --noinput
    ````