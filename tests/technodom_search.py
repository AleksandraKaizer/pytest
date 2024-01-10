import requests
import json
import pytest


@pytest.mark.parametrize('search_item', ['холодильник', 'кофе', 'смартфон', 'Смартфондар', 'samsung', '456', '!@', ',,,'])
def test_search(search_item):
    url = "https://stapi.technodom.kz/katalog/api/v1/products/search"

    payload = {
        "city_id":"5f5f1e3b4c8a49e692fefd70",
        "client_id":"81fA2rlZbS",
        "query": search_item,
        "exact_field_match":"",
        "extended":"",
        "referer":"https://next-stage.technodom.kz/search?recommended_by=instant_search&recommended_code=%D0%BA%D0%BE%D1%84%D0%B5&r46_search_query=%D0%BA%D0%BE%D1%84%D0%B5&r46_input_query=%D0%BA%D0%BE%D1%84%D0%B5",
        "segment":"",
        "session_id":"wt5kG0mpKy",
        "type":"instant_search",
        "categories":[],
        "subquery": False
        }
    
    headers = {
    'accept': 'application/json, text/plain, */*',
    'accept-language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
    'content-language': 'ru-RU',
    'Content-Type': 'text/plain'
    }

    response = requests.request("POST", url, headers=headers, json=payload)

    #print(response.text)
    assert response.status_code == 200

#done Проверка Technodom
#done Проверка AirbaFresh

#done Проверка рус
#done Проверка каз
#done Проверка англ

#done Проверка цифры
#done Проверка символы
#done Проверка нулевой поиск
#g
#Проверка эмодзи ???

#Поиск по бренду - открывается CMS