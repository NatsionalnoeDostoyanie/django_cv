from settings._from_dotenv import (
    _PG_DATABASE_NAME,
    _PG_HOST,
    _PG_PORT,
    _PG_USER_NAME,
    _PG_USER_PASSWORD,
)


PG_DATABASE_NAME = _PG_DATABASE_NAME
PG_HOST = _PG_HOST
PG_MAX_BIGINT = 9_223_372_036_854_775_807
PG_PORT = _PG_PORT
PG_USER_NAME = _PG_USER_NAME
PG_USER_PASSWORD = _PG_USER_PASSWORD

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql_psycopg2",
        "HOST": PG_HOST,
        "NAME": PG_DATABASE_NAME,
        "PASSWORD": PG_USER_PASSWORD,
        "PORT": PG_PORT,
        "USER": PG_USER_NAME,
    }
}
