# coding: utf-8

import requests
from bs4 import BeautifulSoup
import re
from limpeza import Limpeza
import time
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from procuranovos import Links as novosLinks
from enviaEmail import enviaEmail
import json


def Json(valor):
    with open('data.json', 'r') as file:
        data = json.load(file)
    print(data[valor])
    return data[valor]


def Crawler():
    # Define a URL que sera usada para o Crawler
    #url = 'https://www.webmotors.com.br/carros/sp-sao-paulo/de.2015/ate.2021?estadocidade=São%20Paulo%20-%20São%20Paulo&tipoveiculo=carros&anoate=2021&anode=2015&kmate=50000&precoate=250000&anunciante=Pessoa%20Física'
    url = "https://www.webmotors.com.br/carros/sp/de.2015/.ate.2021?estadocidade=São%20Paulo&tipoveiculo=carros&anoate=2021&anode=2015&kmate=250000&precoate=50000&anunciante=Pessoa%20Física"

    option = Options()
    # Defina a opção Headless (Segundo plano) para o firefox
    option.headless = True
    # coloca o firefox para iniciar em segundo plano
    driver = webdriver.Firefox(options=option)

    # faz o get da url que sera usada para pegar as informações

    driver.get(url)

    print("Headless Firefox Initialized")
    time.sleep(5)

    scrolls = Json('scroll')

    print("Iniciando o scroll da pagina")
    for i in range(1, scrolls):

        carros = driver.execute_script(
            "window.document.getElementsByClassName('ResultZero_header')")

        if carros == "none":
            i = scrolls
        else:
            try:
                # clica no botão para carregar mais informações caso o botão exista
                driver.execute_script(
                    "window.document.getElementById('ButtonCarriesMoreCars').click();")
                time.sleep(5)
                # da um scroll até o final da pagina caso o botão exista
                driver.execute_script(
                    "window.scrollTo(0, document.body.scrollHeight);")
                time.sleep(5)
            except:
                # Da um scroll até o final da pagina caso o botão não exista
                driver.execute_script(
                    "window.scrollTo(0, document.body.scrollHeight);")
                time.sleep(5)
        
            element = driver.find_element_by_xpath(
                "//div[@class='ContainerCardVehicle  ']")
                
        print(i)

    print("capturando o HTML")
    # encontra todos os posts de carros dentro da pagina
    element = driver.find_element_by_xpath(
        "//div[@class='ContainerCardVehicle  ']")

    # transforma o conteudo capturado em um elemento HTML
    html_content = element.get_attribute("outerHTML")

    print("Parseando conteudo HTML capturado")
    soup = BeautifulSoup(html_content, 'html.parser')  # parsea o conteudo HTML

    links = []
    # Encontra os links dentro do conteudo capturado da pagina
    for link in soup.findAll('a', attrs={'href': re.compile("^https://")}):
        # Passa o link encontrado para o Array Links
        links.append(link.get('href') + "\n")

    print("Colocando Informações parseada no arquivo Links.txt")

    # Abre o arquivo links.txt em modo de escrita
    with open('files/links.txt', 'w') as file:
        links_str = ''
        # grava informações do Array links dentro de links_str e salva no arquivo links.txt
        file.write(links_str.join(links))

    driver.quit()  # fecha o Browser

    Limpeza()  # Inicia Limpeza do arquivo links.txt

    novosLinks()  # Separa os novos links em no arquivo novos.txt

    enviaEmail()  # envia email com os novos links no arquivo novos.txt
