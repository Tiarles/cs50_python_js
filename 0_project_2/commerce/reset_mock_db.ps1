python manage.py flush --noinput

$env:DJANGO_SUPERUSER_USERNAME="tiarles"
$env:DJANGO_SUPERUSER_EMAIL="tiarles@example.com"
$env:DJANGO_SUPERUSER_PASSWORD="david12345"

python manage.py createsuperuser --noinput

python manage.py makemigrations
python manage.py migrate

python manage.py shell -c "exec(open('mock_db_data.py').read())"

# python .\manage.py dumpdata -o db_copy.json

# python .\manage.py loaddata db_copy.json
