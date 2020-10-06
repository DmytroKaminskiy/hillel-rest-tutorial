from django.urls import reverse

import pytest


@pytest.mark.parametrize('status_code', (
    101,
    200,
    302,
    404,
    500,
))
def test_status_info_get(status_code, api_client):
    url = reverse('basic:status-info', args=(status_code, ))
    response = api_client.get(url)
    assert response.status_code == 200

    assert len(response.json()) == 1  # only one key exists
    assert response.json()['data']


def test_status_info_get_not_found(api_client):
    status_code = 600
    url = reverse('basic:status-info', args=(status_code, ))
    response = api_client.get(url)
    assert response.status_code == 404

    assert len(response.json()) == 1  # only one key exists
    assert response.json() == {'detail': f'Status Code "{status_code}" not found.'}


@pytest.mark.parametrize('method', (
        'post',
        'put',
        'delete',
))
def test_hello_world_methods(method, api_client):
    url = reverse('basic:status-info', args=(200, ))
    response = getattr(api_client, method)(url)
    assert response.status_code == 405
    assert response.json() == {'detail': f'Method "{method.upper()}" not allowed.'}
