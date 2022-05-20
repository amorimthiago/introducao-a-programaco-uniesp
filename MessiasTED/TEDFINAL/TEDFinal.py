#Desenvolva um programa utilizando os recursos que já vimos: if, elif, else, while, for, listas, dicionários.
#Não precisa utilizar todos, apenas os que julgar necessários.

#Desenvolva um algoritmo que apresente as seguintes opções ao usuário:
#1 - Cadastrar um funcionário
#2 - Alterar um funcionário
#2 - Listar (imprimir) todos os funcionários
#3 - Excluir um funcionário
#4 - Adicionar um aumento de salário


controle = 1
cadastros = []

while controle != 0:
    
    print("1 - Cadastrar")
    print("2 - Listar")
    print("0 - Sair")
    controle = int(input("Digite a opção: "))
    
    # Cadastro
    if controle == 1:
        
        pessoa = []
        
        nome = input("Digite o nome da pessoa: ")
        pessoa.append(nome)
        
        email = input("Digite o e-mail: ")
        pessoa.append(email)
        
        idade = int(input("Digite a idade: "))
        pessoa.append(idade)
        
        cadastros.append(pessoa)
        
        
    # Listar pessoas cadastradas
    elif controle == 2:
        
        if cadastros is None:
            
            print("Não temos registros")
        
        else:
            
            for p in cadastros:
                
                print(p)
    
    elif controle == 0:
        
        print("Obrigado! Gostei de interagir com você :\)")