DEBUG = True
ALLOWED_HOSTS = []

SECRET_KEY = ""

# Also, configure your database here.
# For instance, for a Postgres database:
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql_psycopg2",
        "NAME": "unilogin",
        "USER": "unilogin",
        "PASSWORD": "averysecurepassword",
        "HOST": "localhost",
        "PORT": "",
    }
}

# Allow users to modify their personal details (name, email)?
ALLOW_USERS_MODIFY_DETAILS = True

# What fields users can modify.
# Only relevant if ALLOW_USERS_MODIFY_DETAILS is set to True.
# The possible values are "first_name", "last_name", "username", and "email".
USERS_MODIFY_FIELDS = ["first_name", "last_name", "username", "email"]

# Path to a GeoLite database
# See https://docs.djangoproject.com/en/3.1/ref/contrib/gis/geoip2
# for more details.
GEOIP_PATH = "unilogin/geolite/"
