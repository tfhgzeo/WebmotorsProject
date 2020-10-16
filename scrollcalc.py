# coding: utf-8

import requests
import time
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from crawler import Crawler
import json


def CalculaScroll(num):
    srt_num = num

    quantidade = srt_num.replace('.', '')

    quantidade = int(quantidade)

    s = quantidade/24

    string = str(s)

    v = ""
    x = 0
    z = 0
    while x != 1:
        i = string[z]

        if i != '.':
            v = v + ''.join(i)
        else:
            x = 1
        z = z + 1

    valor = int(v) + 1

    segundos = valor*10

    horas = segundos // 3600
    sobra = segundos % 3600

    minutos = sobra // 60
    sobra = sobra % 60

    print('O código vai ser executado em aproximadamente {0}:{1}:{2}'.format(
        horas, minutos, sobra))

    return valor


def ScrollsCalc():
    url = 'https://www.webmotors.com.br/carros/sp/de.2015/ate.2021?estadocidade=São%20Paulo&tipoveiculo=carros&anoate=2021&anode=2015&kmate=250000&precoate=50000&anunciante=Pessoa%20Física'

    option = Options()
    # Defina a opção Headless (Segundo plano) para o firefox
    option.headless = True
    # coloca o firefox para iniciar em segundo plano
    driver = webdriver.Firefox(options=option)

    # faz o get da url que sera usada para pegar as informações

    driver.get(url)
    time.sleep(5)

    element = driver.find_element_by_xpath("//div[@class='FoundCars']")

    html_content = element.get_attribute("outerHTML")

    driver.quit()

    soup = BeautifulSoup(html_content, 'html.parser')  # parsea o conteudo HTML

    tag = soup.find('strong')
    posts = tag.find(text=True)

    scrolls = CalculaScroll(posts)

    with open('data.json', 'r') as file:
        data = json.load(file)

    old_posts = data['posts']

    data['scroll'] = scrolls

    if posts != old_posts:
        with open('data.json', 'w') as file:
            data['posts'] = posts
            file.write(json.dumps(data))

        Crawler()
    else:
        print('Não tem novos posts')


ScrollsCalc()
