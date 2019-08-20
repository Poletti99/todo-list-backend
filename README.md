# ToDo List Back-end

### Technologies

-   Python;
-   Flask;
-   SQLAlchemy;
-   Marshmallow;
-   Gunicorn;

### How to use?

Install the dependencies with the following command

```sh
pip install -r requirements.txt
```

Export the following environment variables

```sh
export FLASK_APP=app
export FLASK_ENV=Development
export FLASK_DEBUG=True
```

Execute the migrations

```sh
flask db init
flask db migrate
flask db upgrade
```

Execute the server with the following command

```sh
gunicorn "app:create_app()"
```

To change the default port, export the environment variable `PORT` with the desired value.

Default Port is `8000`
