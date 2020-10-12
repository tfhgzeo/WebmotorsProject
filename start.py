from crawler import Crawler
import time

def start():

    i = 0
    x = 1
    while i == 0:
        ini = time.time()
        print("iniciando A execução {0} do Crawler".format(x))
        Crawler()
        fim = time.time()
        print("Execução {0} finalizada em {1}".format(x, fim-ini))
        x = x + 1

start()
