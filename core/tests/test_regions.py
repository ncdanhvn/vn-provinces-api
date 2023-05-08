from rest_framework.test import APIClient
from rest_framework import status
import pytest


@pytest.mark.django_db
class TestRegions:
    def test_if_list_regions_return_200(self):
        client = APIClient()
        response = client.get('/api/regions/')
        
        assert response.status_code == status.HTTP_200_OK
        assert len(response.data) == 8  # There are 8 regions in test db
