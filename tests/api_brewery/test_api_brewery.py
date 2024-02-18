import pytest
import requests
import allure


@allure.severity(allure.severity_level.CRITICAL)
def test_api_url_status_code(api_url):
    "Проверяем, что List Breweries выдает ответ 200"
    r = requests.get(api_url)   # https://api.openbrewerydb.org/v1/breweries
    assert r.status_code == 200


@pytest.mark.parametrize("endpoint", ('meta', 'random'))
@allure.severity(allure.severity_level.CRITICAL)
def test_api_endpoint_status_code(endpoint, api_url):
    "Проверяем, что List Breweries выдает ответ 200"
    endpoint = {'endpoint': f'{endpoint}'}
    r = requests.get(api_url, params=endpoint)
    assert r.status_code == 200


@pytest.mark.parametrize("obdb_id, name", [("b54b16e1-ac3b-4bff-a11f-f7ae9ddc27e0", "MadTree Brewing 2.0"),
                                           ("ef970757-fe42-416f-931d-722451f1f59c", "10 Barrel Brewing Co")])
def test_obdb_id(obdb_id, name, api_url):
    "Проверяем, что по нужному айди возвращается верное название пивнухи"
    r_name = requests.get(api_url + f"/{obdb_id}")
    assert r_name.status_code == 200
    json_name = r_name.json()
    assert json_name["name"] == name


@pytest.mark.parametrize("name", ('dog', 'boss', 'dream'))
def test_get_names_with_word(name, api_url):
    "Делаем поиск по dog в названии пивнухи и проверяем, что в ответе все названия с dog"

    r_dog = requests.get(api_url + f"/autocomplete?query={name}")
    assert r_dog.status_code == 200
    json_dog = r_dog.json()
    for json_dog in json_dog:
        text = json_dog["name"]
        assert f"{name}" in text.lower()


def test_get_by_sity(api_url):
    "Делаем поиск по городу и проверяем, что в ответе только этот город"
    r_san_diego = requests.get(api_url + "?by_city=san_diego")
    assert r_san_diego.status_code == 200
    json_san_diego = r_san_diego.json()
    for json_san_diego in json_san_diego:
        text = json_san_diego["city"]
        assert "san diego" in text.lower()


def test_get_by_state(api_url):
    "Делаем поиск по штату и проверяем, что в ответе только этот штат"
    r_сolorado = requests.get(api_url + "?by_state=Colorado")
    assert r_сolorado.status_code == 200
    json = r_сolorado.json()
    for j in json:
        text = j["state"]
        assert "Colorado" in text


def test_size_3(api_url):
    "Проверяем, что в ответе в json 3 пивнухи"
    r_size = requests.get(api_url + "/random?size=3")
    assert r_size.status_code == 200
    json_r_size = r_size.json()
    assert len(json_r_size) == 3


@pytest.mark.parametrize("by_name", ('3cross Fermentation Cooperative', '(512) Brewing Co'))
def test_by_name(by_name, api_url):
    "Проверяем поиск по названию пивнухи"
    query = {'by_name': f'{by_name}'}
    r = requests.get(api_url, params=query)
    assert r.status_code == 200
    json_names = r.json()
    assert json_names[0]['name'] == by_name   # Доступ к элементам списка осуществляется по индексу, без [0] не работает


@pytest.mark.parametrize("by_type", ('micro', 'nano', 'regional', 'brewpub', 'large'))
def test_by_type(by_type, api_url):
    "Проверяем поиск по типу"
    query = {'by_type': f'{by_type}'}
    r = requests.get(api_url, params=query)
    assert r.status_code == 200
    json_types = r.json()
    assert json_types[0]['brewery_type'] == by_type  # json_types[0] - первая пивоварня в списке


@pytest.mark.parametrize("by_country", ('south_korea', 'germany'))
def test_meta_by_country(by_country, api_url):
    "Проверяем поиск метаданных по стране"
    r = requests.get(api_url + f"/meta?by_country={by_country}")
    assert r.status_code == 200
    json_types = r.json()
    assert all(key in json_types for key in ["total", "page", "per_page"])
