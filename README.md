# Weather-API


This project is a Django-based application that retrieves and stores current weather data <br/>
for multiple cities using a [weatherAPI](https://www.weatherapi.com/) for getting current weather <br/>
The application uses Celery and Redis to process background tasks,<br/>
dockerized for easy deployment , and uses swagger for API Testing 




## Table of Contents

- [Features](#features)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Usage](#usage)
- [Functions and Classes](#functions-and-classes)
- [URLs Map](#urls-map)
- [Installation Notes](#installation-notes)

<br/><br/>
## Features

- Retrieves current weather data for multiple cities.
- Stores weather data in a PostgreSQL database.
- Uses Celery and Redis for asynchronous task processing.
- Dockerized setup for easy deployment.
- Using swagger for API testing

<br/><br/>



## Prerequisites

Before you begin, ensure you have the following installed on your system:

- [Python 3.8+](https://www.python.org/downloads)
- [Docker](https://www.docker.com/get-started/)
- [Docker Compose](https://docs.docker.com/compose/install/)

<br/><br/>

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/Ahmed-Elatar/weather_api.git
    cd weather_api
    ```

2. Build the Docker containers:
    ```bash
    sudo docker-compose build
    ```
    
3. Create a superuser to access the Django admin:
    ```bash
    sudo docker-compose run web python manage.py createsuperuser
    ```

4. Start the Docker containers:
    ```bash
    sudo docker-compose up
    ```

<br/><br/>
## Usage

Once the application is up and running, you can access it in your web browser at `http://0.0.0.0:8000/`. <br/> 

### Access the Django Admin

Go to `http://0.0.0.0:8000/admin` and log in using the superuser credentials you created during the setup. <br/>
for full access to weather data, periodic tasks, etc...

<br/><br/>
## Functions-and-Classes


1. def `get_weather(loc)` : <br/>
     
    Fetch and process current weather data for a specific location.
    
    This function retrieves the current weather data for a given location using the WeatherAPI
    and uses nested_to_flastten() function to flattens nested JSON data into a single dictionary. 
    It also extracts and reformats the date and time from the weather data.
    
    Parameters:
        loc (str): The location for which to fetch weather data. 
                    Example: 'Cairo'
    
    Example:
        weather_data = get_weather('Alexandria')
    
    Returns:
        dict: A dictionary containing flattened weather data with keys such as 'temp_c', 
                'humidity', 'wind_kph', 'pressure_mb', 'date', 'time', etc.
    
                Example:
                {
                    "temp_c": 27.3,
                    "humidity": 78,
                    "wind_kph": 13.7,
                    "pressure_mb": 1009.0,
                    "date": datetime.date(2024, 8, 11),
                    "time": datetime.time(2, 15),
                    ...
                }
    
    
    Notes:
        - The function uses an API-Token key to access the WeatherAPI service. Make sure your key is valid.



 
2. def `nested_to_flastten(nested_data)` : <br/>
    This function flattens nested JSON data into a single dictionary.

    Parameters:
        nested_data ( dict(dict) ): The location for which to fetch weather data. 
                Example: 'nested_data'

                   nested_data={
                                "location": {
                                    "name": "Austin",
                                    "region": "Texas",
                                    "country": "United States of America",
                                    "lat": 30.27,
                                    "lon": -97.74,
                                    "tz_id": "America/Chicago",
                                    "localtime_epoch": 1723631062,
                                    "localtime": "2024-08-14 05:24"
                                },
                                "current": {
                                    "last_updated": "2024-08-14 05:15",
                                    "temp_c": 26.7,
                                    "wind_kph": 6.8,
                                    "wind_dir": "S",
                                    "pressure_mb": 1017,
                                    "cloud": 25
                                }
                            }

    Example:
        weather_data = nested_to_flastten(nested_data)

    Returns:
        dict: A dictionary containing flattened weather data with keys such as 'temp_c', 
              'name', 'wind_kph', 'pressure_mb', 'date', 'time', etc.

              Example:
                      {
                        
                        "name": "Austin",
                        "region": "Texas",
                        "country": "United States of America",
                        "lat": 30.27,
                        "lon": -97.74,
                        "tz_id": "America/Chicago",
                        "date": "2024-08-13",
                        "time": "06:45:00",
                        "temp_c": 26.8,
                        "wind_kph": 10.4,
                        "wind_dir": "S",
                        "pressure_mb": 1015.0,
                        "cloud": 54
                    }




4. def `get_cities_weather()` : <br/>
    - get_cities_weather Background Task
    
    This Celery task call get_weather() function from views and send the parameter ( city name ) to get city weather data
    The function uses a global counter (`cnt`) to keep track of which cities have been processed 
    note :
        - he task processes 10 cities per run ( from the cities list )
        
    Then save the data returned from  get_weather() in database using  WeatherDataSerializer
    
    
    
    Parameters:
        None
    
    Returns:
        None

 
5. class `WeatherListView(ListCreateAPIView)` : <br/>

    - API view to retrieve a list of weather data or create a new record.
    This view have 2 methods:
    
    - GET : Returns a list of all weather data records .
    - POST : Allows clients to create a new record in JSON format .
    
    Attributes:
        queryset: A Django QuerySet that retrieves all WeatherData objects from the database.
        serializer_class: The serializer class which used to convert WeatherData instances to and from JSON.

      
6. class `WeatherDetailView(RetrieveUpdateDestroyAPIView)` : <br/>
    
    -  API view to retrieve a single record of weather data or update a record or delete a record.
    This view have 3 methods:

    - GET : Retrieves a specific weather data record by its primary key (ID).
    - PATCH : Partially or fully updates a specific weather data record.
    - DELETE : Deletes a specific weather data record.

    Attributes:
        queryset: A Django QuerySet that retrieves all WeatherData objects from the database.
        serializer_class: The serializer class which used to convert WeatherData instances to and from JSON.


<br/><br/>
##  URLs Map

- `http://0.0.0.0:8000/admin`

- `http://0.0.0.0:8000/`

- `http://0.0.0.0:8000/{id}`

-  `http://0.0.0.0:8000/swagger`




<br/><br/>
## Installation Notes

- edit the .env file : <br/>
      - Add your Postgres database Name, User, and password
- And do the same step in the docker-compose file
   
