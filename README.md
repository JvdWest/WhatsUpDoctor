# Docker Compose Run

To start Postgres, Postgres Adminer, and the WhatsUpDoctor API in Docker containers, run the following command

`docker-compose up --build -d`

In order to initialize the database and populate it with seed data, run the following command

`docker exec whatsupdoctor-whatsupdoctor-1 ./init.sh`

Patients have fixed assignments to practitioners. Please see `backoffice/managememnt/commands/load_seed_data.py` 
to view these assignments.

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
