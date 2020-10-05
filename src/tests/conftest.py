# import os

# from django.conf import settings
# from django.core.management import call_command

from faker import Faker

import pytest

from pytest_django.fixtures import _django_db_fixture_helper

from rest_framework.test import APIClient


@pytest.fixture(scope='session', autouse=True)
def db_session(request, django_db_setup, django_db_blocker):
    """
    Changed scope to 'session'
    """
    if 'django_db_reset_sequences' in request.funcargnames:
        request.getfixturevalue('django_db_reset_sequences')
    if 'transactional_db' in request.funcargnames \
            or 'live_server' in request.funcargnames:
        request.getfixturevalue('transactional_db')
    else:
        _django_db_fixture_helper(request, django_db_blocker, transactional=False)


# @pytest.fixture(scope='session', autouse=True)
# def fixtures():
#     for fixture in ('category', 'book'):
#         call_command('loaddata', os.path.join(settings.BASE_DIR, 'tests', 'fixtures', f'{fixture}.json'))


@pytest.fixture(scope="session")
def fake():
    yield Faker()


@pytest.fixture(scope='function')
def api_client():
    yield APIClient()
