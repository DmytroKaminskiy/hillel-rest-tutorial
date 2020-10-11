from django.utils import timezone

from rest_framework.reverse import reverse

from tests.factories.book import BookFactory


def test_books_create_empty_data(api_client):
    url = reverse('book:books')
    response = api_client.post(url, data={}, format='json')
    assert response.status_code == 400

    assert response.json() == {
        'author': ['This field is required.'],
        'title': ['This field is required.'],
        'publish_year': ['This field is required.'],
    }


def test_books(api_client, author):
    url = reverse('book:books')

    data = {
        'author': author.id,
        'title': 'Book Title',
        'publish_year': 1992,
    }

    response = api_client.post(url, data=data, format='json')
    assert response.status_code == 201
    assert response.json()

    response = api_client.get(url)
    assert response.status_code == 200
    assert response.json()['results']

    last_record_id = response.json()['results'][-1]['id']

    url = reverse('book:book', args=(last_record_id, ))
    response = api_client.get(url)
    assert response.status_code == 200
    response_data = response.json()
    assert response_data['title']
    assert response_data['publish_year']
    assert response_data['id']

    data = {'title': 'New Book Title'}
    response = api_client.patch(url, data=data)
    assert response.status_code == 200
    assert response.json()['title'] == data['title']

    response = api_client.delete(url)
    assert response.status_code == 204
    assert response.content == b''

    book = BookFactory()
    url = reverse('book:book', args=(book.id,))
    response = api_client.delete(url)
    assert response.status_code == 400
    assert response.json() == {'error': 'Cannot delete Book created by system'}


def test_books_wrong_publish_date(api_client, author):
    url = reverse('book:books')
    year = timezone.now().year + 100

    data = {
        'author': author.id,
        'title': 'Book Title',
        'publish_year': year,
    }
    response = api_client.post(url, data=data, format='json')
    assert response.status_code == 400
    assert response.json() == {'publish_year': [f'{year} is not a correct year!']}
