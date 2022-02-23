from django.urls import reverse
import pytest
from django.contrib.auth.models import User

from lettings.models import Letting, Address


@pytest.mark.django_db
def test_index_view_title(client):
    url = reverse('lettings:index')
    response = client.get(url)
    assert response.status_code == 200
    assert "<title>Lettings</title>" in str(response.content)

@pytest.mark.django_db
def test_letting_view_specific_title(client):
    address_test = Address.objects.create(
                   number=100,
                   street="Rue de l'exemple",
                   city="Lyon",
                   state="Rhône",
                   zip_code=69000,
                   country_iso_code="FRA"
    )
    Letting.objects.create(title="Letting test", address=address_test)
    url = reverse('lettings:letting', args=[1])
    response = client.get(url)
    assert response.status_code == 200
    assert "<title>Letting test</title>" in str(response.content)

