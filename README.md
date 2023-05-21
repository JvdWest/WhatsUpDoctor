# WhatsUpDoctor

This is a Django project that is able to store patient and practitioner information in a relational 
database, linked in a many-to-many relationship. One API is expose in order to get patient information.

## Docker Compose Run

To start Postgres, Postgres Adminer, and the WhatsUpDoctor API in Docker containers, run the following command

`docker-compose up --build -d`

In order to initialize the database and populate it with seed data, run the following commands

`docker exec whatsupdoctor-whatsupdoctor-1 python manage.py migrate`

`docker exec whatsupdoctor-whatsupdoctor-1 python manage.py load_seed_data`

Patients have fixed assignments to practitioners. Please see `backoffice/managememnt/commands/load_seed_data.py` 
to view these assignments.

If you are using Windows, you can execute the init.bat file to execute all commands above.

Powershell: `.\init.bat`

Windows Command Prompt: `init.bat`

## Test locally

To get all patients in the system

`GET http://localhost:8000/backoffice/patients`

To only get patients linked to a specific practitioner, add `hpcsanumber` query parameter

`GET http://localhost:8000/backoffice/patients?hpcsanumber=B9876543`

## Requirements

1. Python 3.11.0 
1. pipenv, version 2023.4.29

## Running App Without Docker

To run the API without Docker, update the `host` field in settings.py to 'localhost'. Then run the following command.

`python manage.py runserver`

## Add new Django app

`python manage.py startapp appname`

## General Django Commands

Create migration

`python manage.py makemigrations`

View SQL

`python manage.py sqlmigrate app_name MigrationFile`

Apply Migration

`python manage.py migrate`

Create Database User

`python manage.py createsuperuser`

Show migrations

`python manage.py showmigrations`

To undo a migration or to apply to a specific migration

`python manage.py migrate app_name migration_name`

Ignore unapplied migration

`python manage.py migrate myapp migration_name --fake`

Load seed data

`python manage.py load_seed_data`
