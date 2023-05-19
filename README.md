## Requirements

1. Python 3.11.0 
1. pipenv, version 2023.4.29

## Running App

`python manage.py runserver`

## Add new Django app

`python manage.py startapp appname`

## Docker Compose

`docker-compose up`

## Database Migrations

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