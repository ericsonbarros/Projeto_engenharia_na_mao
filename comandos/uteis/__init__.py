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
    return f'A a area do revestimento é {resp:.2f}m²'.replace('.', ',')
    print(linha())



