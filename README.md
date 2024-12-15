# PlanningPoker
Learning the python Django framework by creating a planning poker app.

I built this as an adaptation of the tutorial posted [here](https://docs.djangoproject.com/en/5.1/intro/tutorial01/).  I'm also interested in looking at a hybrid python javascript approach as described [here](https://www.geeksforgeeks.org/integrating-django-with-reactjs-using-django-rest-framework/).

Initial setup:

- 'python -m venv venv'
- './venv/bin/activate'
- 'pip install -r requirements.txt'


When I make changes to `game/models.py` I'm changing the database and need to do a migration.

- 'python manage.py makemigrations game'
- 'python manage.py migrate'