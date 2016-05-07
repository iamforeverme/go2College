# go2College
Web application for PRC College Entry Registration

There are several steps to initialize dockers to work with this web application:

1. edit Dockerfile and docker-compose.yml
2. vim requirements.txt
3. Use the django admin script to set up a new project: docker-compose run web django-admin.py startproject djangoProj .
  a) Create related images
  b) Create a new project
4. For docker created files, the ownership should be transfered to a user :sudo chown -R $USER:$USER .
5. Update djangoProj/settings.py as follows:
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'postgres',
        'USER': 'postgres',
        'HOST': 'db',
        'PORT': 5432,
    }
}


6. docker-compose up

PS: sudo chown -R $USER:$USER .
Confirm localhost:8000 is accessible.
