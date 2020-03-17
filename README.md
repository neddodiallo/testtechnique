# Web project with Django

This little project has three page, add employee, list employee and details of on employee

## Installation

To run this project, you will need to install [docker](https://docs.docker.com/install/) 
and [docker-compose](https://docs.docker.com/compose/install/).

create .env file in the root directory and add in the following content
```file
    POSTGRES_DB_NAME="diallo"
    POSTGRES_DB_USER="diallo"
    POSTGRES_DB_PASSWORD="admin"
    POSTGRES_DB_HOST="db"
    POSTGRES_DB_PORT="5432"
```
Go to the root project and run this command
```bash
    docker-compose run
```
## Usage

List employees: http://localhost:8000/employee/list/

Detail employee: click on details after  displaying employee

Add employee: http://localhost:8000/employee/add/

The data can be visualize by using:
    url: http://localhost:8081/

    password: admin
    user: diallo