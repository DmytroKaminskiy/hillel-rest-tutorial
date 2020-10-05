from django.urls import reverse

import pytest


def test_statuses_get(api_client):
    url = reverse('basic:statuses')
    response = api_client.get(url)
    assert response.status_code == 200

    assert len(response.json()) == 1  # only one key exists

    data = response.json()['data']

    assert len(data) == 5  # only 5 groups exist in status codes
    assert len(data['informational']) == 5
    assert len(data['success']) == 10
    assert len(data['redirection']) == 9
    assert len(data['client_error']) == 33
    assert len(data['server_error']) == 11


@pytest.mark.parametrize('method', (
        'post',
        'put',
        'delete',
))
def test_hello_world_methods(method, api_client):
    url = reverse('basic:statuses')
    response = getattr(api_client, method)(url)
    assert response.status_code == 405
    assert response.json() == {'detail': f'Method "{method.upper()}" not allowed.'}
