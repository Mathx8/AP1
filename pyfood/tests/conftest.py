import pytest

@pytest.fixture(params=[
    {
        "endereco_entrega": "Rua das Flores, 123",
        "itens": []
    },
    {
        "endereco_entrega": "Rua das Flores, 123",
        "itens": 
        [
            {"nome": "Hamburguer", "preco": 15.00},
            {"nome": "Refrigerante", "preco": 4.00}
        ]
    },
    {
        "endereco_entrega": "Rua das Flores, 123",
        "itens": 
        [
            {"nome": "Hamburguer", "preco": 15.00},
            {"nome": "Refrigerante", "preco": 90.00}
        ]
    }
]) 
def pedidos(request):
    return request.param

@pytest.fixture()
def arquivo_log_temporario():
    arquivo = open("log.txt", "w") 
    yield arquivo 
    arquivo.close()