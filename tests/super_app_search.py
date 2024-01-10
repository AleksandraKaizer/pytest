import requests

url = 'https://superapp-dev.technodom.kz/gsearch/v1/search'

headers = {
    'Content-Type': 'application/json'
}

data = {
    "city_id": "5f5f1e3b4c8a49e692fefd70",
    "client_id": "W6iNPybHhZ",
    "query": "кофе",
    "exact_field_match": "",
    "extended": "",
    "referer": "https://www.technodom.kz/",
    "segment": "",
    "session_id": "4nsN13eqDV",
    "type": "full_search",
    "categories": [],
    "subquery": False
}

response = requests.post(url, headers=headers, json=data)

#Проверка на код 200
def test_code_ok():
    
    response = requests.get(url, headers, data)
    print(response.status_code)
    #print(response.json())
     
    assert response.status_code == 200
    
 #Проверка Technodom
 #Проверка AirbaFresh
 #Проверка Airba одежда

#Проверка рус
#Проверка каз
#Проверка англ

#Проверка цифры
#Проверка символы
#Проверка нулевой поиск
#Проверка эмодзи ???