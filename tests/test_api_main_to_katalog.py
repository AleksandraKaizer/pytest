import requests
import pytest

url = "https://stapi.technodom.kz/menu/api/v1/menu/katalog?city_id=5f5f1e3b643d490d8a416164&Content-Type=application/json; charset=utf-8"
#payload = {}
#response = requests.request("GET", url, data=payload)
header_kaz = {'Content-Language': 'kk-KK'}

#Проверки на код 200 (на обоих языках)

def test_code_ok_kaz():

  response = requests.get(url, headers=header_kaz)

  print(response.status_code)
  #print(response.json())

  assert response.status_code == 200

def test_code_ok_rus():

  response = requests.get(url)
  #print(response.status_code)

  assert response.status_code == 200

#Проверки на города

def test_city_id_ok():

  params = {'city_id': '5f5f1e3b643d490d8a416164'} #Алматы
  response = requests.get(url, params=params)

  assert response.status_code == 200

#Проверки языка

def test_language_rus():

  response = requests.get(url)
  language = response.json()["items"][0]["title"]

  assert language == "Смартфоны и гаджеты"
  #print(response.json())

def test_language_kaz():

  response = requests.get(url, headers=header_kaz)
  language = response.json()["items"][0]["title"]

  assert language == "Смартфондар және гаджеттер"







