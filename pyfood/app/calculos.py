def calcular_total_com_desconto(pedido: dict) -> float:
    if pedido["itens"]:
        soma = 0
        for p in pedido["itens"]:
            soma += p["preco"]
        if soma > 100:
            valor_total = soma * 0.90
            return valor_total
        else:
            return soma
    else:
        return "Pedido não pode está sem item"

def dividir_conta(pedido: dict, numero_pessoas: int) -> float:
    total = calcular_total_com_desconto(pedido)
    if isinstance(total, str):
        total = 0
    return total/numero_pessoas