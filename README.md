# Candy shop
![alt text](https://secretldn.com/wp-content/uploads/2018/08/Wall-of-sweets-e1535647968627.jpg)

Recommendation
: Use Terminal (Unix-base systems) or GitBash (Windows)


## Setup enviroment

### Create virtula enviroment

`$ python -m venv env`

### Activate enviroment

Bash: `$ source env/bin/activate/`  
Powershell: `> env\Scripts\Activate.ps1`

### Install depedencies (while enviroment activated)

`$ pip install -r requirements.txt`

Note
: If you have problem with pip, then install or reinstall it by downloading:
[get-pip.py](https://bootstrap.pypa.io/get-pip.py)

### Deactivate enviroment

`$ deactivate`

## Setup application and database

### Choose application mode ("dev", "prod", "docker") in .flaskenv file

`FLASK_ENV="your_mode"`

Note:
- "dev" run application without docker with sqlite database
- "prod" run docker-compose with postgresql
- "docker" run docker-compose with postgresql with DEBUG=True

##### For more info visit config.py file

### Recreate database sqlite

`$ flask manage.py recreate_db`

### Run server

`$ flask manage.py runserver`
