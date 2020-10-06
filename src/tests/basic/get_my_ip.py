from django.urls import reverse

import pytest


def test_statuses_get(api_client):
    url = reverse('basic:get-my-ip')
    response = api_client.get(url)
    assert response.status_code == 200

    assert len(response.json()) == 1  # only one key exists
    ip = response.json()['data']
    assert ip == '127.0.0.1'


@pytest.mark.parametrize('method', (
        'post',
        'put',
        'delete',
))
def test_hello_world_methods(method, api_client):
    url = reverse('basic:get-my-ip')
    response = getattr(api_client, method)(url)
    assert response.status_code == 405
    assert response.json() == {'detail': f'Method "{method.upper()}" not allowed.'}
