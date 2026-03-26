import pytest
from tests.conftest import pedidos
from app.validador import validar_pedido
from app.calculos import calcular_total_com_desconto, dividir_conta
from app.pagamento import finalizar_compra

def test_validar(pedidos):
    assert validar_pedido(pedidos)

def test_calcular_total(pedidos):
    assert calcular_total_com_desconto(pedidos)

def test_deve_falhar_ao_dividir_por_zero(pedidos):
    with pytest.raises(ZeroDivisionError):
        dividir_conta(pedidos, 0)

def test_deve_verificar_fraude_antes_de_cobrar(pedidos, mocker):
    mock_gateway = mocker.Mock()

    finalizar_compra(pedidos, mock_gateway)

    roteiro_esperado = [
        mocker.call.verificar_fraude(pedidos),
        mocker.call.cobrar(pedidos)
    ]

    mock_gateway.assert_has_calls(roteiro_esperado, any_order=False)