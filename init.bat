docker-compose up --build -d
docker exec whatsupdoctor-whatsupdoctor-1 python manage.py migrate
docker exec whatsupdoctor-whatsupdoctor-1 python manage.py load_seed_data