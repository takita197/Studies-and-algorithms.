# Grafo de amigos
grafo_amigos = {
    "Alice": ["Bob", "Carlos"],
    "Bob": ["Alice", "David"],
    "Carlos": ["Alice", "David", "Eva"],
    "David": ["Bob", "Carlos", "Eva"],
    "Eva": ["Carlos", "David","Jeffersson"]
}

# Função para mostrar os amigos de uma pessoa
def mostrar_amigos(nome):
    amigos = grafo_amigos.get(nome)
    if amigos:
        print(f"Amigos de {nome}: {', '.join(amigos)}")
    else:
        print(f"{nome} não está no grafo.")

# Exemplos
mostrar_amigos("Alice")
mostrar_amigos("David")
mostrar_amigos("Jeffersson")
mostrar_amigos("Sofia") # Pessoa que não está no grafo