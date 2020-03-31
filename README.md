# Candy shop
![alt text](https://secretldn.com/wp-content/uploads/2018/08/Wall-of-sweets-e1535647968627.jpg)

Recommendation
: Use Terminal (Unix-base systems) or GitBash (Windows)


## Setup enviroment

### First move to api directory
`$ cd api`

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

## Setup sqlite database

### Initialization

`$ flask db init`

### Migrate database

`$ flask db migrate -m "your migration message"`

### Apply migrations to database

`$ flask db upgrade`

## Run scripts

### Run React
`$ npm start`

### Run Flask
`$ npm start-api`
