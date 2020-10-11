from datetime import date, datetime

from rest_framework.reverse import reverse

from tests.factories import AuthorFactory


def test_authors_create_empty_data(api_client):
    url = reverse('book:authors')
    response = api_client.post(url, data={}, format='json')
    assert response.status_code == 400

    assert response.json() == {
        'first_name': ['This field is required.'],
        'last_name': ['This field is required.'],
        'date_of_birth': ['This field is required.'],
        'country': ['This field is required.'],
        'language': ['This field is required.'],
    }


def test_authors(api_client):
    url = reverse('book:authors')

    data = {
        'first_name': 'FirstName',
        'last_name': 'LastName',
        'date_of_birth': datetime.now().date(),
        'country': 'ukraine',
        'language': 'ua',
    }

    response = api_client.post(url, data=data, format='json')
    assert response.status_code == 201
    assert response.json()

    response = api_client.get(url)
    assert response.status_code == 200
    assert response.json()['results']

    last_record_id = response.json()['results'][-1]['id']

    url = reverse('book:author', args=(last_record_id, ))
    response = api_client.get(url)
    assert response.status_code == 200
    response_data = response.json()
    assert response_data['first_name']
    assert response_data['last_name']
    assert response_data['id']

    data = {'first_name': 'NewFirstName'}
    response = api_client.patch(url, data=data)
    assert response.status_code == 200
    assert response.json()['first_name'] == data['first_name']

    response = api_client.delete(url)
    assert response.status_code == 204
    assert response.content == b''

    author = AuthorFactory()
    url = reverse('book:author', args=(author.id,))
    response = api_client.delete(url)
    assert response.status_code == 400
    assert response.json() == {'error': 'Cannot delete Author created by system'}


def test_authors_wrong_date_of_birth(api_client):
    url = reverse('book:authors')
    year = date(2100, 1, 1)

    data = {
        'first_name': 'FirstName',
        'last_name': 'LastName',
        'date_of_birth': year,
        'country': 'ukraine',
        'language': 'ua',
    }
    response = api_client.post(url, data=data, format='json')
    assert response.status_code == 400
    assert response.json() == {'date_of_birth': ['2100-01-01 should be in past!']}
