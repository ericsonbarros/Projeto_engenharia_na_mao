def linha(tam=50):
    return '-' * tam


def cabeçalho(txt):
    print(linha())
    print(txt.center(50))
    print(linha())


def piso(area,rendimento):
    resp = ((area + (area * 15 / 100)) / rendimento)
    return f'{resp:.2f}'.replace('.', ',')


