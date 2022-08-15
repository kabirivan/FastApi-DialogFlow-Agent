# FastApi-DialogFlow-Agent



## Run project using Docker compose

```sh
docker-compose -f docker-compose-dev.yml up --build
```

## Run Alembic migrations (Only if you change the DB model)

```sh
docker-compose -f docker-compose-dev.yml exec fastapi_server alembic revision --autogenerate
docker-compose -f docker-compose-dev.yml exec fastapi_server alembic upgrade head
```
