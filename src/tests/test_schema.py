from django.urls import reverse

import pytest


@pytest.mark.parametrize('url_name', (
        'schema-swagger-ui',
        'schema-redoc',
))
def test_docs(url_name, client):
    url = reverse(url_name)
    response = client.get(url)
    assert response.status_code == 200


@pytest.mark.parametrize('response_format', (
        '.json',
        '.yaml',
))
def test_schema_json(response_format, client):
    url = reverse('schema-json', args=(response_format, ))
    response = client.get(url)
    assert response.status_code == 200
