# FastAPI Project
A sample project built with FastAPI, PostgreSQL, and SQLAlchemy.

## Requirements
- Python 3.7+
- FastAPI
- Psycopg2
- SQLAlchemy
- Pydantic
- Datetime
- OS

## Environment Variables
The following environment variable must be set:
- `DATABASE_PASSWORD`

## Getting Started
1. Clone the repository
    ```
    $ git clone https://github.com/<your-username>/FastAPI-project.git
    ```
2. Create a virtual environment and activate it
    ```
    $ python -m venv env
    $ source env/bin/activate
    ```
3. Install the dependencies
    ```
    $ pip install -r requirements.txt
    ```
4. Set the `DATABASE_PASSWORD` environment variable
    ```
    $ export DATABASE_PASSWORD=<your-password>
    ```
5. Run the project
    ```
    $ python main.py
    ```

## Project Structure
The project is structured as follows:

.
├── database.py
├── main.py
├── models.py
├── routers
│   ├── auth.py
│   ├── post.py
│   └── user.py
├── schemas.py
└── utils.py


- `main.py`: The entry point of the application.
- `database.py`: Contains functions to interact with the database (PostgreSQL).
- `models.py`: Defines the SQLAlchemy models for the project.
- `routers`: Contains the routers for different parts of the application (post, user, auth).
- `schemas.py`: Defines the Pydantic schemas for the project.
- `utils.py`: Contains utility functions for the project.

## API Endpoints
The following API endpoints are available:
- `/posts`: For managing posts.
- `/users`: For managing users.
- `/auth`: For authentication.
