import pytest

from django.core.management import call_command

# Fixture to populate test databse
@pytest.fixture(scope='session')
def django_db_setup(django_db_setup, django_db_blocker):
    with django_db_blocker.unblock():
        call_command('seed_test_db')