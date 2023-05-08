from rest_framework.test import APIClient
from rest_framework import status
import pytest


@pytest.mark.django_db
class TestRegions:
    def test_if_list_regions_return_200_and_correct_regions_count(self):
        client = APIClient()
        response = client.get('/api/regions/')
        
        assert response.status_code == status.HTTP_200_OK
        assert len(response.data) == 8  # There are 8 regions in test db

    def test_if_retrieve_region_return_200_and_correct_content(self):
        client = APIClient()
        response = client.get('/api/regions/3/')
        
        assert response.status_code == status.HTTP_200_OK
        assert response.data['name_en'] == 'Red River Delta'    
        assert response.data['provinces_count'] == 2    # This region has 2 provinces


@pytest.mark.django_db
class TestProvinces:
    def test_if_list_provinces_return_200_and_correct_provinces_count(self):
        client = APIClient()
        response = client.get('/api/provinces/')
        
        assert response.status_code == status.HTTP_200_OK
        assert response.data['count'] == 6  # There are 6 provinces in test db

    def test_if_retrieve_province_return_200_and_correct_content(self):
        client = APIClient()
        response = client.get('/api/provinces/1/')
        
        assert response.status_code == status.HTTP_200_OK
        assert response.data['name_en'] == 'Ha Noi'
        assert len(response.data['districts']) == 3    # Ha Noi has 3 districts in test db 
        assert response.data['wards_count'] == 2    # Ha Noi has 2 wards in test db 


@pytest.mark.django_db
class TestDistricts:
    def test_if_list_districts_return_200_and_correct_districts_count(self):
        client = APIClient()
        response = client.get('/api/districts/')
        
        assert response.status_code == status.HTTP_200_OK
        assert response.data['count'] == 10  # There are 10 districts in test db

    def test_if_retrieve_district_return_200_and_correct_content(self):
        client = APIClient()
        response = client.get('/api/districts/1/')
        
        assert response.status_code == status.HTTP_200_OK
        assert response.data['name_en'] == 'Ba Dinh'    
        assert len(response.data['wards']) == 2    # This district has 0 wards in test db 
        

@pytest.mark.django_db
class TestWards:
    def test_if_list_wards_return_200_and_correct_wards_count(self):
        client = APIClient()
        response = client.get('/api/wards/')
        
        assert response.status_code == status.HTTP_200_OK
        assert response.data['count'] == 2  # There are 2 wards in test db

    def test_if_retrieve_ward_return_200_and_correct_content(self):
        client = APIClient()
        response = client.get('/api/wards/1/')
        
        assert response.status_code == status.HTTP_200_OK
        assert response.data['name_en'] == 'Phuc Xa'    
        assert response.data['province']['id'] == 1   