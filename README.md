# unilogin

SSO using Django and OAuth

## How to run

```bash
git clone https://github.com/etnguyen03/unilogin
cd unilogin
pipenv install --deploy
```

At this point, you will want to copy `unilogin/settings/secret.sample.py`
to `unilogin/settings.secret.py` and fill in as necessary. Take care of the following:

* Set `DEBUG` to `False` in a production environment.
* Add your hostname to `ALLOWED_HOSTS`.
* Generate a Django secret key and set it in `SECRET_KEY`. This can be done with:
  ```python
  from django.core.management.utils import get_random_secret_key
  print(get_random_secret_key())
  ```
* Configure your database, see [this](https://docs.djangoproject.com/en/3.1/ref/databases/).
  The libraries included allow for the following databases, but only PostgreSQL and SQLite3
  will be "officially" endorsed. However, I discourage the use of an SQLite3 database in production.
  * PostgreSQL
  * SQLite
  * MariaDB
  * MySQL
  * Oracle
  * Microsoft SQL
* Configure other settings, whose options and instructions are located in `secret.sample.py`.

Then, run:

```bash
pipenv run python3 manage.py collectstatic
pipenv run python3 manage.py migrate
pipenv run gunicorn unilogin.wsgi 
```

The last line starts a `gunicorn` server.

In production, you should use a reverse proxy (Nginx?) that sets the
`X_FORWARDED_FOR` header to the client's actual IP.

---

Copyright © 2020 Ethan Nguyen and contributors. All rights reserved.

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU Affero General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU Affero General Public License for more details.

You should have received a copy of the GNU Affero General Public License
along with this program.  If not, see <https://www.gnu.org/licenses/>.