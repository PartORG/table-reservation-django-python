# table-reservation-django
Table reservation website made in Python/Django

## RUN:
In order to run on localhost:

First, create a superuser:
__<directory of solution>/python manage.py createsuperuser__

Next, run a local server:
__<directory of solution>/python manage.py runserver__

For sending emails with localhost SMTP server, open a new command line window and run:
__python -m smtpd -n -c DebuggingServer localhost:6000__