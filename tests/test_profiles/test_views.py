from django.urls import reverse
import pytest
from django.contrib.auth.models import User

from profiles.models import Profile


@pytest.mark.django_db
def test_index_view_title(client):
    url = reverse('profiles:index')
    response = client.get(url)
    assert response.status_code == 200
    assert "<title>Profiles</title>" in str(response.content)

@pytest.mark.django_db
def test_profile_view_specific_title(client):
    test_user = User.objects.create(username="testuser", email="testuser@test.fr", password="159487263")
    Profile.objects.create(user=test_user, favorite_city="Lyon")
    url = reverse('profiles:profile', args=["testuser"])
    response = client.get(url)
    assert response.status_code == 200
    assert "<title>testuser</title>" in str(response.content)
