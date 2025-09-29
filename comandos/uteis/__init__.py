def linha(tam=50):
    return '-' * tam


def cabeçalho(txt):
    print(linha())
    print(txt.center(50))
    print(linha())


def piso(area,rendimento):
    resp = ((area + (area * 15 / 100)) / rendimento)
    return f'{resp:.2f}'.replace('.', ',')


def areaRevestimmento():
    print('Vamos calcular a area do revestimento, por favor informe a largura e comprimento(em metros) da peça que sera utilizada:')
    l = float(input('Largura: '))
    c = float(input('Comprimento: '))
    resp = l * c
    return f'{resp:.2f}'

def area():
    print('Vamos calcular a area do piso, por favor informe a largura e comprimento(em metros) do piso:')
    l = float(input('Digite a Largura: '))
    c = float(input('Digite o comprimento: '))
    resp = l * c
    return f'{resp:.2f}'




