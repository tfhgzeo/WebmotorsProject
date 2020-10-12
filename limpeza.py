import json


def Limpeza():
    print("Iniciando Limpeza do arquivo Links.tzt")
    with open('files/links.txt', 'r') as fileLinks:
        novoLink = ""
        todosNovosLinks = []
        for linha in fileLinks:
            link = linha
            if link != novoLink:
                novoLink = link
                todosNovosLinks.append(novoLink)


    print("passando conteudo do arquivo links.txt para o todos.txt")
    with open('files/todos.txt', 'w') as file:
        links = ''
        file.write(links.join(todosNovosLinks))


def limpezaOld():
    
    with open("files/old.json", 'r') as old:
        oldLinks = json.load(old)
        tamanho = len(oldLinks)

    links = []
    for y in range(tamanho):
        links.append(oldLinks['link{0}'.format(y)] + '\n')

    linksstr = ''
    with open('files/old.old', 'w') as oldOld:
        oldOld.write(linksstr.join(links))
