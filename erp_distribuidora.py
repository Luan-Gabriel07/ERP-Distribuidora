estoque = []
pedidos = []
historico = []

def cadastrar_produto (estoque):
    codigo = int(input("Código do produto: "))
    nome = input("Nome do produto: ")
    quantidade = int(input("Quantidade: "))
    preco = float(input("Preço do produto (uni): R$"))
    produto = [codigo,nome,quantidade,preco]
    estoque.append(produto)
    return produto

def remover_produto (estoque):
    if estoque == []:
        print ("Estoque vazio!")
        return
    for produto in estoque:
        print (f"Código: {produto [0]} - Nome {produto [1]} - Quantidade: {produto [2]} - Preço: {produto [3]}")
    print ("")
    remocao = int(input("Insira o código do produto que você deseja remover: "))
    for indice, produto in enumerate(estoque): # enumerando os indices da lista
        if remocao == produto[0]:
            produto_removido = estoque.pop(indice)
            print (f"Produto {produto_removido[1]} removido!")
            return produto_removido
    print ("Produto não encontrado!")
   
def ver_estoque (estoque):
    if estoque == []:
        print ("Estoque vazio")
        return
    for produto in estoque:
            print (f"Código: {produto [0]}")
            print (f"Nome: {produto [1]}")
            print (f"Quantidade: {produto [2]}")
            print (f"Preço: {produto [3]:.2f}")
            print ('-'*20)

def cadastrar_pedido (pedidos,estoque):
    if estoque == []:
        print("Estoque vazio! Não é possível cadastrar um pedido.")
        return
    numero = int(input("Número do pedido: "))
    cliente = input("Nome do cliente: ")
    print ('-=-'*20)
    print("\nProdutos disponíveis:")
    print ('-=-'*20)
    for produto in estoque:
        print(f"Código: {produto[0]} - Nome: {produto[1]} - Quantidade: {produto[2]}")

    codigo_produto = int(input("Código do produto desejado: "))
    produto_encontrado = None
    for produto in estoque:
        if codigo_produto == produto[0]:
            produto_encontrado = produto
            break
    if produto_encontrado == None:
        print("Produto não encontrado!")
        return
    quantidade = int(input("Quantidade desejada: "))
    if quantidade > produto_encontrado[2]:
        print("Quantidade indisponível no estoque!")
        return
    opc_prioridade = int(input("Prioridade do pedido: [1-Alta / 2-Média / 3-Baixa] "))
    if opc_prioridade == 1:
        prioridade = 1
    elif opc_prioridade == 2:
        prioridade = 2
    elif opc_prioridade == 3:
        prioridade = 3
    else:
        print ("Opão inválida!")
        return
    pedido = [numero, cliente, codigo_produto, quantidade, prioridade]
    pedidos.append(pedido)
    return pedido

def visualizar_pedidos (pedidos):
    if pedidos == []:
        print ("Nenhum pedido para entregar")
    for pedido in pedidos:
        print (f"Pedido {pedido[0]}")  
        print (f"Cliente: {pedido[1]}")   
        print (f"Código do produto: {pedido[2]}")   
        print (f"Quantidade: {pedido[3]}")   
        print (f"Prioridade {pedido [4]}")
        print('-'*20)

def pedidos_prioridade (pedidos): #fila prioridade
    if pedidos == []:
        print ("Lista de pedidos vazia")
        return
    indice_prioridade = 0
    for indice, pedido in enumerate(pedidos):
        if pedido[4] < pedidos [indice_prioridade][4]:
            indice_prioridade = indice
    return indice_prioridade
''' 
Comparamos a prioridade do pedido atual com a prioridade do pedido
que estamos considerando como prioritário. Se encontrarmos uma
prioridade maior, atualizamos o índice do pedido prioritário.
'''

def visualizar_pedidos_prioridade(pedidos):

    if pedidos == []:
        print("Lista de pedidos vazia")
        return

    indice = pedidos_prioridade(pedidos)

    pedido = pedidos[indice]

    print(f"Pedido prioritário: {pedido[0]}")
    print(f"Cliente: {pedido[1]}")
    print(f"Código do produto: {pedido[2]}")
    print(f"Quantidade: {pedido[3]}")
    print(f"Prioridade: {pedido[4]}")

def processar_pedido (pedidos,estoque):
    if pedidos == []:
        print ("Lista de pedidos vazia")
        return
    indice = pedidos_prioridade(pedidos) # recebe o índice do pedido prioritário.
    pedido = pedidos[indice] # recebe o pedido que está no índice
    for produto in estoque:
        if produto[0] == pedido[2]: # Compara se o código do produto é igual ao código do pedido
            produto[2] = produto[2] - pedido[3] # Diminui a quantidade de produtos no estoque
            pedido = pedidos.pop(indice)
            print (f"Pedido processado: Cliente {pedido[1]} - Pedido {pedido[0]} - Código do produto: {pedido[2]} - Quantidade: {pedido[3]} - Prioridade {pedido[4]} ")
            return pedido
    print("Produto do pedido não encontrado no estoque!")

def ordenar_estoque(estoque):
    for i in range(len(estoque)): # "range" serve para controlar quantas vezes os o for vai se repetir
        for j in range(0, len(estoque) - i - 1): # controla quais elementos serão comparados em cada passagem
            if estoque[j][0] > estoque[j + 1][0]:
                estoque[j], estoque[j + 1] = estoque[j + 1], estoque[j] # trocar dois produtos de posição na lista.
    print ("Ordenação feita!")

def buscar_produto (estoque): # Busca Binaria
    if estoque == []:
        print ("Lista de estoque vazia")
        return
    codigo_busca = int(input("Código do produto: "))
    inicio = 0
    fim = len(estoque) - 1
    while inicio <= fim:
        meio = (inicio + fim) // 2 # o "//" realiza a divisão inteira, descartando a parte decimal
        if codigo_busca == estoque[meio][0]:
            print ("Produto encontrado!")
            print (f"Código: {estoque[meio][0]}")
            print (f"Produto: {estoque[meio][1]}")
            print (f"Quantidade: {estoque[meio][2]}")
            print (f"Preço: R${estoque[meio][3]:.2f}")
            return
        elif codigo_busca > estoque[meio][0]:
            inicio = meio + 1
        elif codigo_busca < estoque[meio][0]:
           fim = meio - 1
    print ("Produto não encontrado!")

def registrar_acao(historico,acao):
    historico.append(acao)

def desfazer_acao(historico):
    if historico == []:
        print ("Não há ações para desfazer")
    else: 
        remocao = historico.pop()
        print (f"Ação removida {remocao}")

def ver_historico (historico):
    if historico == []:
        print ("Histórico vazio")
    for acao in historico:
        print (f"Ação: {acao[0]}")
        print (f"Dados: {acao[1]}")
opcao = 1
while opcao != 10:
    print('-=-'*20)
    print("                      DISTRIBUIDORA")
    print('-=-'*20)
    print ("1- Cadastrar produto")
    print ("2- Remover produto")
    print ("3- Ver estoque")
    print ("4- Cadastrar pedido")
    print ("5- Processar próximo pedido")
    print ("6- Ver pedidos prioritários")
    print ("7- Buscar produto")
    print ("8- Ver históricos de ações")
    print ("9- Desfazer última ação")
    print ("10- Sair")
    print ("")
    opcao = int(input("Escolha o que deseja: "))  
    print ('-'*20)   
    match opcao:
        case 1: 
            produto = cadastrar_produto(estoque)
            acao = ["cadastrar_produto", produto] # descrição da ação
            registrar_acao(historico,acao)
        case 2: 
            produto_removido = remover_produto(estoque)
            if produto_removido != None:
                acao = ["remover_produto", produto_removido]
                registrar_acao(historico,acao)
        case 3:
            ver_estoque(estoque)
        case 4:
            pedido = cadastrar_pedido(pedidos,estoque)
            if pedido != None:
                acao = ["cadastrar_pedido", pedido]
                registrar_acao(historico,acao)
        case 5:
            pedido = processar_pedido(pedidos,estoque)
            if pedido != None:
                acao = ["processar_pedido", pedido]
                registrar_acao (historico,acao)
        case 6:
            visualizar_pedidos_prioridade(pedidos)
        case 7:
            ordenar_estoque(estoque)
            buscar_produto(estoque)
        case 8: 
            ver_historico(historico)
        case 9:
            desfazer_acao(historico)
     