# Candy shop

![alt text](https://secretldn.com/wp-content/uploads/2018/08/Wall-of-sweets-e1535647968627.jpg)

## Virtual enviroment setup

### First install poetry

`$ pip install poetry` or
`$ curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python`

### Then activate enviroment and install dependencies

`$ poetry shell`
`$ poetry install`

## Setup application and database

### Choose application mode ("dev", "prod", "docker") in .flaskenv file

`FLASK_ENV="your_mode"`

Note:

- "dev" run application without docker with sqlite database
- "prod" run docker-compose with postgresql
- "docker" run docker-compose with postgresql with DEBUG=True

For more info visit config.py file

### Recreate database sqlite

`$ poetry run python manage.py recreate_db`

### Run server

`$ poetry run python manage.py runserver`

### To run any other command in virtual enviroment then type:

`$ poetry run your_command`
