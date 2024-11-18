from src.unitarias import Functionurl, fetch_user_by_id, mock_get_database_connection, delete_user_by_name, get_database_connection
from requests.exceptions import HTTPError
import requests
import pytest

#Prueba 1
def test_buscardatosExito(requests_mock):
    url = 'https://www.w3schools.com/data'
    data = {'key': 'value'}
    requests_mock.get(url, json=data, status_code=200)

    result = Functionurl(url)
    assert result == data

#Prueba 2
def test_buscardatos404(requests_mock):
    url = 'https://www.w3schools.com/404'
    requests_mock.get(url, status_code=404)

    result = Functionurl(url)
    assert result == "Error 404"

#Prueba 3
def test_buscardatosexception(requests_mock):
    url = 'https://www.w3schools.com/error'
    requests_mock.get(url, exc=HTTPError("HTTP Error"))

    with pytest.raises(HTTPError):
        Functionurl(url)


@pytest.fixture 
def mock_db(monkeypatch):
    # Mock de la conexión a la base de datos

    # Usar monkeypatch para reemplazar get_database_connection con mock_get_database_connection
    monkeypatch.setattr('src.unitarias.get_database_connection', mock_get_database_connection)

#Prueba 4
def test_fetch_user_by_id(mock_db):
    user = fetch_user_by_id(1)
    assert user == (1, "Alice")

@pytest.fixture(scope="module")
def db_connection():
    connection = get_database_connection()
    yield connection
    connection.close()

def test_delete_user_by_name(db_connection):
    cursor = db_connection.cursor()
    delete_user_by_name("Alice")
    cursor.execute("SELECT * FROM users WHERE name = %s", ("Alice",))
    result = cursor.fetchone()
    assert result is None







