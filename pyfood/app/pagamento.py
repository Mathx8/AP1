def finalizar_compra(pedido: dict, gateway_modulo):
    gateway_modulo.verificar_fraude(pedido)
    gateway_modulo.cobrar(pedido)

    return "Compra aprovada"