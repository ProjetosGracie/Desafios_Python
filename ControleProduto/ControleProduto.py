# Lista de dicionarios 

produtos = []
## ou usa True

def menu():
    opcao = 0
    while opcao !=5:
     print("\n--------MENU--------")
     print("1 - ARMAZENAR ")
     print("2 - DADOS")
     print("3 - VENDAS")
     print("4 - ESTOQUE")
     print("5 - ENCERRAR\n")
     opcao = int(input("Digite a opcao: "))
     if opcao == 1:
         inicio()
     elif opcao == 2:
         dadosProduto()
     elif opcao == 3:
         vendas()
     elif opcao == 4:
         informarEstoque()
     elif opcao == 5:
         print("Sistema Encerrado")
         break
     else:
         print("opcao errada") 

def inicio():
     codigo = int(input("Informe o codigo: "))
     nome = input("Informe o nome do produto: ")
     preco = float(input("Informe o preco: "))
     estoque = int(input("Informe o estoque: "))
     
     produto = { "codigo": codigo,
                 "nome": nome,
                 "preco":preco,
                 "estoque":estoque  }
    
     produtos.append(produto)
     return 

def dadosProduto():
    numero = 0 
    # Percorre a lista primeiro 

    for produto in produtos:

        print(f"\n===== {numero + 1}º Produto =====")
        numero = numero + 1
        #Percorre o dicionario 
        for titulo, valor in produto.items():
         print(titulo," - ",valor)

def vendas():
    if produtos == 0:
        print("\nNao ha produtos")
        return 

    nomeProduto = input("\nInforme o nome do produto vendido: ")

    # Percorre para achar o nome do produto 
    for produto in produtos:
        for valor in produto.values():
         # aqui ele ja sabe qual/ o que é o estoque 
         if valor == nomeProduto: # ---> achou o nome 
             vendidos = int(input("Informe as vendas: "))
             produto["estoque"] = produto["estoque"] - vendidos
    else:
        print("Produto inexistente") 

def informarEstoque():
 for produto in produtos:
    # 1. Pega o valor do estoque diretamente
    estoque = produto["estoque"]
    
    if estoque == 0:
        # saber de quem é o estoque
        print(f"{produto['nome']}: Não há produtos no estoque")
        
    elif estoque <= 3:
        print(f"{produto['nome']}: Estoque baixo ")
        
    else:
        print(f"{produto['nome']}: Estoque normal - Quantidade no estoque {estoque}")
menu()
