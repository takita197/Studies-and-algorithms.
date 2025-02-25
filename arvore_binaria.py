class Arvore:
    def __init__(self, valor=None):
        self.valor = valor
        self.esquerda = None
        self.direita = None

# Função para calcular a soma de todos os valores na árvore
def soma_arvore(raiz):
    if raiz is None:
        return 0
    return raiz.valor + soma_arvore(raiz.esquerda) + soma_arvore(raiz.direita)

# Função para adicionar um valor à árvore (organizado)
def adicionar(raiz, valor):
    if raiz is None:
        return Arvore(valor)
    
    if valor < raiz.valor:
        raiz.esquerda = adicionar(raiz.esquerda, valor)
    else:
        raiz.direita = adicionar(raiz.direita, valor)
    
    return raiz

# Função para imprimir a árvore em ordem
def imprimir_em_ordem(raiz):
    if raiz is None:
        return
    
    imprimir_em_ordem(raiz.esquerda)
    print(raiz.valor, end=" ")
    imprimir_em_ordem(raiz.direita)

# Exemplo de uso
if __name__ == "__main__":
    # Criar uma árvore
    raiz = None
    valores = [10, 5, 15, 2, 7, 12, 20]
    
    for valor in valores:
        raiz = adicionar(raiz, valor)
    
    # Imprimir a árvore em ordem (do menor para o maior)
    print("Árvore em ordem:")
    imprimir_em_ordem(raiz)
    print()
    
    # Calcular a soma dos valores
    total = soma_arvore(raiz)
    print(f"Soma de todos os valores: {total}")
    
    # Exemplo de busca de um valor
    def buscar(raiz, valor):
        if raiz is None or raiz.valor == valor:
            return raiz
        
        if valor < raiz.valor:
            return buscar(raiz.esquerda, valor)
        return buscar(raiz.direita, valor)
    
    # Buscar o valor 7
    resultado = buscar(raiz, 7)
    if resultado:
        print(f"Valor 7 encontrado!")
    else:
        print("Valor 7 não encontrado.")