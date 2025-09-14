import data
import requests

def test_delete_incorrect_username():
    url = f'{data.BASE_URL}/user/NoUserInSystem'
    response_delete = requests.delete(url)
    assert response_delete.status_code == 404

def test_delete_incorrect_url():
    url = f'{data.BASE_URL}/usour/NoUserInSystem'
    response_delete = requests.delete(url)
    assert response_delete.status_code == 404

def test_delete_without_username():
    url = f'{data.BASE_URL}/user/'
    response_delete = requests.delete(url)
    assert response_delete.status_code == 405