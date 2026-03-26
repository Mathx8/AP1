def validar_pedido(pedido: dict) -> bool:
    if pedido["endereco_entrega"] and pedido["itens"]:
        soma = 0
        for p in pedido["itens"]:
            soma += p["preco"]
        if soma <= 20:
            return "Preço menor que 20 reais"
        else:
            return soma
    else:
        return "Pedido sem endereço ou item"