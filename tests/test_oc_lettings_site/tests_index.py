from django.urls import reverse


def test_index_view_title(client):
    url = reverse('index')
    response = client.get(url)
    assert response.status_code == 200
    assert "<title>Holiday Homes</title>" in str(response.content)
