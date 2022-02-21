from django.urls import reverse
import pytest
from django.contrib.auth.models import User
from django.template import Template, Context
from mock import patch





@pytest.mark.django_db
def test_index_view_title(client):
    url = reverse('lettings:index')
    response = client.get(url)
    assert response.status_code == 200
    assert "<title>Holiday Homes</title>" in str(response.content)

"""def test_dummy():
    assert 1"""

