# personal-travel-planner
*WIP: This project contains the files required*

## Travel App
Building and running

Pre-requisites: Python 3

To run the server do you need install these dependencies:

```pip install fastapi```

```pip install "uvicorn[standard]"```

```pip install sqlalchemy```

Please be sure you are locate in the personal-travel-planner directory before to execute: 

```uvicorn travel_app.main:app reload```

## RESTful API
```POST /users```

<img width="1013" alt="Screen Shot 2022-08-01 at 4 31 12 AM" src="https://user-images.githubusercontent.com/13652517/182139132-68964331-d64a-4d0e-887e-bf2d9e7657ac.png">

```POST /users/{user_id}/travels```

<img width="1015" alt="Screen Shot 2022-08-01 at 4 34 24 AM" src="https://user-images.githubusercontent.com/13652517/182139423-1974da9f-9b5b-4312-9a2b-6932f6ad575d.png">

```GET /travels```

<img width="1013" alt="Screen Shot 2022-08-01 at 4 35 54 AM" src="https://user-images.githubusercontent.com/13652517/182139653-1b33ea2f-a2c6-4eb1-ab44-9aa9c7eb3735.png">



## Database
Why I should use a relational database for this project? 
At my first impression, when I knew that I will need to have a relationship between travel and user you think about a relational database this is because is more easy thinking about the process to relationships inherent in the data. But also I know that a non-relational database can be use it for this propouse because we don't have a big querys with a lot of relations of columns that isn't we need to do. The quick answer is because I thinking in that way very quickly, and also because if we want to grow up this kind of database is more easy, the thing we change if we want to make a lot of searches in our data probably I would choose a non-relational database.

#### Openweather API

_Notes: I couldn't make works the communication with the openweathermap to retrieve the data I have read about issues with the API in forums about they are delays to activate the API Key but I never I couldn't connect it._

```APIKey: 6699b00d287394d685c560e5492db52c```

```Response: 
  {
    "cod": 401,
    "message": "Invalid API key. Please see http://openweathermap.org/faq#error401 for more info."
  }
 ```
 <img width="1008" alt="Screen Shot 2022-08-01 at 4 19 49 AM" src="https://user-images.githubusercontent.com/13652517/182138093-d6d17e7c-c2e7-4c0a-82e6-0043c47c81b6.png">
 
