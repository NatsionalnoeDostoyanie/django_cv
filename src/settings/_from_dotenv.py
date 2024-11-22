import os
from distutils.util import strtobool

from dotenv import load_dotenv


load_dotenv()

# ----------------------------------------------------------------------------------------------------------------------


# Django

_DEBUG = strtobool(os.getenv("DEBUG"))

_SECRET_KEY = os.getenv("SECRET_KEY")

# ----------------------------------------------------------------------------------------------------------------------


# PostgreSQL

_PG_DATABASE_NAME = os.getenv("PG_DATABASE_NAME")

_PG_HOST = os.getenv("PG_HOST")

_PG_PORT = os.getenv("PG_PORT")

_PG_USER_NAME = os.getenv("PG_USER_NAME")

_PG_USER_PASSWORD = os.getenv("PG_USER_PASSWORD")

# ----------------------------------------------------------------------------------------------------------------------
