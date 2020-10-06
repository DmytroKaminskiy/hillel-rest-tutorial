from django.core.cache import cache
from django.urls import reverse

import pytest


def test_status_info_get(api_client):
    cache.clear()
    url = reverse('basic:save-text')

    # text not found in cache
    response = api_client.get(url)
    assert response.status_code == 404
    assert response.json() == {'detail': 'text not found.'}

    # post correct data
    text = 'hello world'
    response = api_client.post(url, data={'text': text}, format='json')
    assert response.status_code == 201
    assert response.json() == {'text': text}

    # get data from cache
    text = 'hello world'
    response = api_client.get(url)
    assert response.status_code == 200
    assert response.json() == {'text': text}


def test_invalid_post_data(api_client):
    url = reverse('basic:save-text')
    response = api_client.post(url, data={}, format='json')
    assert response.status_code == 400
    assert response.json() == {'message': 'invalid post data.'}


@pytest.mark.parametrize('method', (
        'put',
        'delete',
))
def test_hello_world_methods(method, api_client):
    url = reverse('basic:save-text')
    response = getattr(api_client, method)(url)
    assert response.status_code == 405
    assert response.json() == {'detail': f'Method "{method.upper()}" not allowed.'}
