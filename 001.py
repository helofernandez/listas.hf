
# Definindo as listas de comida e bebida
itens_de_comida_do_cardapio = ['pizza', 'bolo', 'salgado', 'hamburguer']
itens_de_bebida_do_cardapio = ['suco', 'refrigerante', 'agua', 'café']

# Juntando as duas listas em uma só
cardapio_completo = itens_de_comida_do_cardapio + itens_de_bebida_do_cardapio

def exibir_cardapio():
    print("=== CARDÁPIO COMPLETO ===")
    for item in cardapio_completo:
        print(f"- {item}")
    print()

def exibir_comidas():
    print("=== COMIDAS ===")
    for item in itens_de_comida_do_cardapio:
        print(f"- {item}")
    print()

def exibir_bebidas():
    print("=== BEBIDAS ===")
    for item in itens_de_bebida_do_cardapio:
        print(f"- {item}")
    print()

# Exemplo de execução das funções
if __name__ == "__main__":
    exibir_cardapio()
    exibir_comidas()
    exibir_bebidas()