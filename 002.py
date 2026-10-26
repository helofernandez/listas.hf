# lista de itens do cardápio
cardápio = ['pastel', 'pizza', 'coxinha']

# item que o utilizador quer pedir
pedido = 'refrigerante'

# verificar se o item está presente na lista
if pedido in cardápio:
    print(f"O item '{pedido}' está no cardápio!")
else:
    print(f"'{pedido}' não está no cardápio, que tal você pedir {cardápio}?")

# Inicializando a lista antes de usá-la
lista_nomes = []

lista_nomes.append("joão")
lista_nomes.remove("joão")
lista_nomes.insert(0, "joão")
print(lista_nomes)