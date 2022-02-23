from django.urls import reverse
import pytest
from django.contrib.auth.models import User
from django.template import Template, Context


def test_index_view_title(client):
    url = reverse('index')
    response = client.get(url)
    assert response.status_code == 200
    assert "<title>Holiday Homes</title>" in str(response.content)

