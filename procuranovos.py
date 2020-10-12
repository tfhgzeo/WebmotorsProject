import json


def convert(a):
    it = iter(a)
    convert_dict = dict(zip(it, it))
    return convert_dict


def newLink(link):
    novoLink = link
    with open("files/old.json", "r") as old:
        oldLinks = json.load(old)
        tamanho = len(oldLinks)
    for y in range(tamanho):
        if novoLink == oldLinks['link{0}'.format(y)]:
            print('Link Antigo encontrado')
            return False
    return True


def addMoreOld():
    with open('files/old.json', 'r') as old:
        obj_old = json.load(old)

    allLinks = []

    for k, v in obj_old.items():
        allLinks.append(v)
        k.split(' ')

    with open("files/new.txt", "r") as new:
        linhas = new.readlines()
        for linha in linhas:
            allLinks.append(linha)

    final_array = []
    
    with open('files/old.json', 'w') as now:
        x = 0
        for link in allLinks:
            name = "link{0}".format(x)
            value = link.rstrip()
            final_array.append(name)
            final_array.append(value)
            x = x+1

        final_obj = convert(final_array)
       
        json.dump(final_obj, now, indent=4)


def getNewLinks():
    print("Passando novos links para o arquivo new.txt")
    with open('files/links.json', 'r') as file:
        links = json.load(file)

    tamanho = len(links)
    novosLinks = []
    for x in range(tamanho):
        link = links['link{0}'.format(x)]
        if newLink(link):
            novosLinks.append(link)

    with open('files/new.txt', "w") as new:
        for link in novosLinks:
            new.write(link + "\n")

    addMoreOld()


def Links():
    print("iniciando a procura por novos links")
    with open('files/todos.txt', 'r') as links:
        x = 0
        links_array = []

        for linha in links:
            name = "link{0}".format(x)
            value = linha.rstrip()
            links_array.append(name)
            links_array.append(value)
            x = x + 1

    with open("files/links.json", 'w') as links_json:
        obj = convert(links_array)
        json.dump(obj, links_json, indent=4)

    getNewLinks()