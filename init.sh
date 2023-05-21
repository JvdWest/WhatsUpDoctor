#!/bin/bash
python manage.py migrate
python manage.py load_seed_data