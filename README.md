# Weather-API


This project is a Django-based application that retrieves and stores current weather data <br/>
for multiple cities using a weather API. <br/>
The application uses Celery and Redis for background task processing.




## Table of Contents

- [Features](#features)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Usage](#usage)
- [Celery Task: get_cities_weather](#celery-task-get_cities_weather)
- [Docker Setup](#docker-setup)
- [Contributing](#contributing)
- [License](#license)

## Features

- Retrieves current weather data for multiple cities.
- Stores weather data in a PostgreSQL database.
- Uses Celery and Redis for asynchronous task processing.
- Dockerized setup for easy deployment.

## Prerequisites

Before you begin, ensure you have the following installed on your system:

- [Python 3.8+](https://www.python.org/downloads)
- [PostgreSQL](https://www.postgresql.org/download/)
- [Docker](https://www.docker.com/get-started/)
- [Docker Compose](https://docs.docker.com/compose/install/)



## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/Ahmed-Elatar/weather-data-aggregator.git
    cd weather-data-aggregator
    ```

2. Build the Docker containers:
    ```bash
    sudo docker-compose build
    ```

3. Apply the Django migrations:
    ```bash
    sudo docker-compose run web python manage.py migrate
    ```

4. Create a superuser to access the Django admin:
    ```bash
    sudo docker-compose run web python manage.py createsuperuser
    ```

5. Start the Docker containers:
    ```bash
    sudo docker-compose up
    ```

## Usage

Once the application is up and running, you can access it in your web browser at `http://localhost:8000`. 

### Access the Django Admin

Go to `http://localhost:8000/admin` and log in using the superuser credentials you created during the setup.

### Fetching Weather Data

The `get_cities_weather` Celery task fetches weather data for a set of cities and stores it in the database. This task runs every 30 minutes and processes 10 cities per run.

## Celery Task: `get_cities_weather`

The `get_cities_weather` task is responsible for retrieving and saving weather data for a list of cities. It works as follows:

1. The task fetches the current weather data for a list of cities using an external weather API.
2. The fetched data is flattened and stored in the PostgreSQL database.
3. The task processes 10 cities in each run and automatically cycles through the list of cities.

Example usage:
```python
from .tasks import get_cities_weather

get_cities_weather.delay()
