
# ![alternative text](/static/images/fav_icon.png) Vietnam Provinces API

 ![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)![Django](https://img.shields.io/badge/django%20rest-ff1709?style=for-the-badge&logo=django&logoColor=white)![MySQL](https://img.shields.io/badge/MySQL-005C84?style=for-the-badge&logo=mysql&logoColor=white)![Html](https://img.shields.io/badge/HTML5-E34F26?style=for-the-badge&logo=html5&logoColor=white)![CSS](https://img.shields.io/badge/CSS3-1572B6?style=for-the-badge&logo=css3&logoColor=white)![VueJS](https://img.shields.io/badge/Vue.js-35495E?style=for-the-badge&logo=vue.js&logoColor=4FC08D)

VN Provinces API is an open API that provides information about administrative units in Vietnam across four levels:

- Region
- Provinces
- Districts
- Wards

For more information about API usecases, documentation, please visit links below:

- [Homepage](https://vnprovinces.pythonanywhere.com)
- [Documentation](https://vnprovinces.pythonanywhere.com/docs)

## Tech Stack

**Server:** Django, Rest Framework, MySQL

**Databases:** MySQL

**Client:** Html, Vanilla CSS, VueJS, Vuetify

**Documentation:** OpenAPI, drf-spectacular

## Contributing

Contributions are always welcome!

Please fork the repo then start pull requests.

## Installation

- Firstly clone this repository

```bash
  git clone https://github.com/ncdanhvn/vn-provinces-api.git
  cd vn-provinces-api
```

- This project uses pipenv to manage virtual environment. Let's install pipenv first, then install project dependencies.

```bash
  pip install pipenv 
  pipenv install
```

- To run API local on your machine, you need a SQL server. Download and install MySQL [here](https://dev.mysql.com/downloads/mysql/)

- After install MySQL server, you will have a root user with password. Let's enter these information in development settings file at this address: `province > settings > dev.py`

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'province',
        'HOST': 'localhost',
        'USER': 'YOUR_USERNAME',
        'PASSWORD': 'YOUR_PASSWORD'
    }
}
```

- The last step to setup our database is create `province` database on the server we've just installed. Open mysql shell and run create database command.

```mysql
  CREATE DATABASE myshop;
```

- Congratulation now everything set and we are ready to run API on our machine

```bash
  pipenv shell
  python manage.py migrate
  python manage.py runserver
```

- Checkout the homepage of API at default url: <http://127.0.0.1:8000/>

- At this point, everything should work, but if you visit the api endpoint like <http://127.0.0.1:8000/api/provinces>, the response results would be empty, since there is nothing on our database. So let's populate database with some demo data.

```bash
  python manage.py seed_test_db
```

## Running Tests

Repository already has all tests to test endpoint behaviours, there are total 9 tests for 9 endpoints. To run tests, please do following steps:

First install necessary development packages:

```bash
  pipenv install --dev
```

Then run tests:

```bash
  pytest
```

## License

[MIT](https://choosealicense.com/licenses/mit/)
