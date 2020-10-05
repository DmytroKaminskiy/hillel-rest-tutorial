from django.urls import reverse

import pytest


def test_hello_world_get(api_client):
    url = reverse('basic:hello-world')
    response = api_client.get(url)
    assert response.status_code == 200
    assert response.json() == {"data": "Hello, world!"}


@pytest.mark.parametrize('method', (
        'post',
        'put',
        'delete',
))
def test_hello_world_methods(method, api_client):
    url = reverse('basic:hello-world')
    response = getattr(api_client, method)(url)
    assert response.status_code == 405
    assert response.json() == {'detail': f'Method "{method.upper()}" not allowed.'}
