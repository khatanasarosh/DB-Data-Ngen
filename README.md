# DB-Data-Ngen
Standing for Database Data Analyser and Generator, this program will analyse data in a DB and produce fake data based on that.

## Behaviour
- Connects with PostgreSQL, MySQL, MariaDB databases
- Uses SQLAlchemy to get data from source database
- Passes each table and row through randomiser and randomises the data in it
    - For strings, it replaces each character replacing capital letters with capital characters, lowercase with lowercase, numbers with numbers and keeps symbols the same
    - For integers, replaces each digit with another, keeping length of original and fake integer same
    - Keeps dates same as they are
    - Keeps primary and foreign keys the same to maintain relations between data
- Saves data to target database

## Requirements
- Docker with docker-compose

## How to use
- clone the repo
- copy the db.env.example file to db.env and add source and destination DB credentials
- build the docker container using ```docker-compose up -d --build```
- run ```docker-compose exec db-ngen /bin/bash```
- in the docker container run ```python src/main.py```

## For development purpose
For development, run the following command:
- ```docker-compose -f docker-compose.yml -f docker-compose-dev.yml -up --build```

This will create a separate docker container with postgresql installed which can be connected to for testing


## To Do
- Remove usage of main.py file to command
- Add logging and error handling
- Add tests

## Note
This is just a sample project to get up and running with Github. Please feel free to create issues, improvements in PRs and I will review and merge them in.
