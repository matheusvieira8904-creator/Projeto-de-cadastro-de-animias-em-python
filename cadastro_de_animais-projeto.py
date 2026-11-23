animais = []

def linha():
    print('-'*30)

#Primeiro a função de cadastrar como inicio que cadastra especie, idade do animal, peso e cor.
def cadastrar():
    while True:
        print("Area de cadastro:")
        linha()
        especie = input("Digite a especie do animal: ")
        idade = int(input("Idade do animal: "))
        peso = float(input("Digite o peso do animal: "))
        cor = input("Digite a cor do animal: ")
        habitat = input("Digite o habitat do animal: ")
        animais_cadastro = {
                            "Especie" : especie,
                            "idade" : idade,
                            "peso" : peso,
                            "cor": cor, 
                            "Habitat" : habitat
                            }
        animais.append(animais_cadastro)
        linha()
        # Ajustado para aceitar input de texto diretamente sem o int()
        sair = input("Deseja continuar? (Se não digite 0, mas se quiser aperte ENTER): ")
        if sair == "0":
            break

#a função de listar contem todos os animais listados e se não existir nenhum animal ele fala também que não tem.
def listar():
    print("Listar os animais cadastrados")
    linha()
    #Nessa parte do len ele verifica a lista e se não tiver nenhuma possição ele diz que a lista é vazia.
    if len(animais) == 0:
        print("Lista vazia, não a animais aqui!")
        return
    else:
        for a in animais:
            print(f"Especie : {a['Especie']}")
            print(f"Idade : {a['idade']}")
            print(f"peso : {a['peso']}")
            print(f"cor : {a['cor']}")
            print(f"Habitat : {a['Habitat']}")
            linha()

#pesquisar a segui, primeiro ele transforma primeiro em minusculas para manter esse padrão de escrita e de pesquisa para não dar um erro no codigo.
def pesquisar():
    print("Função de pesquisar animais: ")
    linha()
    #roda na lista o len e se não encontrar ele vai exibir a mensagem
    if len(animais) == 0:
        print("Nenhum animal cadastrado para pesquisa.")
        return
        
    procurar = input("Digite a espécie que deseja buscar: ")
    
    for a in animais:
        if procurar.lower() in a["Especie"].lower():
            print("Animal Encontrado:")
            print(f"Especie : {a['Especie']}")
            print(f"Idade : {a['idade']}")
            print(f"peso : {a['peso']}")
            print(f"cor : {a['cor']}")
            linha()
            break  # Para o programa aqui se achar o animal que voce uqer ewncontrar
    else:
        print(f"Nenhum animal da espécie '{procurar}' foi encontrado.")

# a de alterar é simples e primeiro encontra para dps dar os dados denovo
def alterar():
    print("Função de alterar os animais")
    linha()
    procurar = input("Digite a espécie do animal que quer alterar: ")
    
    for a in animais:
        if procurar.lower() == a["Especie"].lower():
            # se ele encontrar ele vai botar para você botar os dados denovo
            a["Especie"] = input("Nova espécie: ")
            a["idade"] = int(input("Nova idade: "))
            a["peso"] = float(input("Novo peso: "))
            a["cor"] = input("Nova cor: ")
            print("Animal alterado com sucesso!")
            return # Sai da função e volta para o menu
    print("Animal não encontrado.")

#excluir vai pesquisar e deletar
def excluir():
    procurar = input("Digite o animal que você quer excluir: ")
    
    for a in animais:
        if procurar.lower() == a["Especie"].lower():
            animais.remove(a) 
            print("Animal excluído com sucesso!")
            break  #o laço vai encerrar pois encontrou e excluiu
    else:
        print("Animal não encontrado.")

#a seguir o menu bem simples para ser facil de funcionar.
def menu():
    while True:
        linha()
        print("PROJETO DE CADASTRAR ANIMAIS")
        print("Zoloogico do IFRN - projeto")
        linha()
        print("1 - Cadastrar animal")
        print("2 - Listar animais")
        print("3 - Pesquisar animal")
        print("4 - Alterar animal")
        print("5 - Excluir animal")
        print("0 - Sair")
        linha()
        
        opcao = input("Escolha uma opção: ")
        linha()

        if opcao == "1":
            cadastrar()
        elif opcao == "2":
            listar()
        elif opcao == "3":
            pesquisar()
        elif opcao == "4":
            alterar()
        elif opcao == "5":
            excluir()
        elif opcao == "0":
            print("Encerrado!   ")
            break
        else:
            print("Opção inválida, tente novamente.")


menu()