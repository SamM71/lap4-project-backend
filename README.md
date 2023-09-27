# CucinaMondo API
Repository for the back-end of our Lap 4 project. Meant to be used in conjunction with our [front-end](https://github.com/rantirules/LAP4-Yao45).

## Installation and Usage
- **Clone** this repository: `git clone <repo>`
- Move (`cd`) into repository folder
- Enter virtualenv: `pipenv shell`
- Install dependencies: `pipenv install`
- Create a SQL database instance (ideally on [ElephantSQL](https://www.elephantsql.com/))
- Create a **.env** file in the repo folder and update the values below
```sh
# .env
FLASK_APP=app
FLASK_DEBUG=1
SQLALCHEMY_DATABASE_URI=postgresql://username:password@db_location/db_name
```
- Seed the database: `pipenv run seed`
- Run the app: `pipenv run dev`

## Available endpoints
Please note that all of the `/tasks` endpoints are unavailable without an authentication token (granted by logging in via the client).
| Route | Method | Response |
| --- | --- | --- |
| `/` | `GET` | Returns a JSON object describing the API. |
| `/users` | `GET` | Returns a JSON object containing all the users. |
| `/users` | `POST` | Accepts a JSON object and uses it to create and store a new user. Use Login instead. |
| `/users/<int:id>` | `GET` | Returns a JSON object representing a single user using `id`. |
| `/users/<int:id>` | `PATCH` | Updates a user based on `id` and the sent JSON object. |
| `/users/<int:id>` | `DELETE` | Deletes a user using `id`. |
| `/users/register` | `POST` | Accepts a JSON object and uses it to create and store a new user. |
| `/users/login` | `POST` | Logs a user in and creates a token for them. |
| `/users/tokens` | `GET` | Returns a JSON object containing all of the tokens. |
| `/users/tokens/<int:id>` | `POST` | Logs a user in and creates a token for them. |
| `/recipes` | `GET` | Returns a JSON object containing all the recipes. |
| `/recipes` | `POST` | Accepts a JSON object and uses it to create and store a new recipes. |
| `/recipes/<int:id>` | `GET` | Returns a JSON object representing a single recipe using `id`. |
| `/recipes/<name>` | `GET` | Returns a JSON object representing a single recipe by using its name. |
| `/recipes/<int:id>` | `PATCH` | Updates a recipe based on `id` and the sent JSON object. |
| `/recipes/<int:id>` | `DELETE` | Deletes a recipe using `id`. |
| `/saved/<int:uid>` | `GET` | Displays a user's saved recipes using user_id. |
| `/saved/<int:uid>/<int:rid>` | `POST` | Creates a saved recipe using user_id and recipe_id. |
| `/saved/<int:uid>/<int:rid>` | `DELETE` | Deletes a saved recipe using user_id and recipe_id. |