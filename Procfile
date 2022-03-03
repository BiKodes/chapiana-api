release: python manage.py makemigrations --no-input
release: python manage.py migrate --no-input

release: python3 manage.py migrate
web: gunicorn.src.wsgi --log.file 