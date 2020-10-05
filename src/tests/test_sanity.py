from django.urls import reverse


def test_sanity():
    assert 200 == 200


def test_admin_get(client):
    response = client.get(reverse('admin:index'))
    assert response.status_code == 302
