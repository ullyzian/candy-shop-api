# Candy shop
![alt text](https://secretldn.com/wp-content/uploads/2018/08/Wall-of-sweets-e1535647968627.jpg)

## Setup application and database

### Choose application mode ("dev", "prod", "docker") in .flaskenv file

`FLASK_ENV="your_mode"`

Note:

- "dev" run application without docker with sqlite database
- "prod" run docker-compose with postgresql
- "docker" run docker-compose with postgresql with DEBUG=True

For more info visit config.py file

### Recreate database sqlite

`$ poetry run flask manage.py recreate_db`

### Run server

`$ poetry run flask manage.py runserver`

### To run any other command in virtual enviroment then type:

`$ poetry run your_command`
