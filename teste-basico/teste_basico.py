import html5lib, requests

# python -m mypy --install-types .\
# pip install html5lib
# pip install requests
# pip install types-requests

def validar_get(url: str) -> None:
    parser = html5lib.HTMLParser(strict = True)
    r = requests.get(url)
    if r.status_code != 200: raise Exception(f"A URL {url} deu um código de status {r.status_code}")
    parser.parse(r.text)

def validar_post(url: str, corpo: str) -> None:
    parser = html5lib.HTMLParser(strict = True)
    r = requests.post(url, data = corpo)
    if r.status_code != 200: raise Exception(f"A URL {url} deu um código de status {r.status_code}")
    parser.parse(r.text)

def menu():
    url = input("Digite a URL que você quer testar: ")
    metodo = input("Qual é o método [GET ou POST]? ")
    try:
        if metodo.upper() == "POST":
            corpo = input("Digite o conteúdo corpo da requisição (tem mesmo formato de uma query string após o '?'): ")
            validar_post(url, corpo)
            print("Sucesso! ;)")
        elif metodo.upper() == "GET":
            validar_get(url)
            print("Sucesso! ;)")
        else:
            print(f"Mas porque diabos você quer testar {metodo}, meu Deus? Esta aplicação não devia usar isso!")
    except Exception as x:
        print("OPS. Deu chabu:")
        print(x)

menu()