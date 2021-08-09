print("\n ==== Colégio Nova Esperança - Evento Literário ====")

# * Variáveis iniciais

contador = 0
listaRm = []
listaNome = []
listaSerie = []
alunos = []

# * Menu Principal

while True:

  print("\n--- Menu de Opções ---")
  print("\n1 - Cadastrar alunos ")
  print("2 - Fazer Incrições")
  print("3 - Listar Inscrições")
  print("4 - Sair")
  menu = int(input("\nQual operação você deseja realizar? "))

# * Opção 1

  if menu == 1:

    print("\n --- 1 - Cadastrar Aluno ---")
    qtdAlunos = int(input("Quantos alunos serão cadastrados? "))
    print(f"OK! Iremos cadastras {qtdAlunos} alunos, vamos começar: ")

    for contador in range(0, (qtdAlunos)):
      print("\n==== Cadastro ====")
      nomeAluno = input("Qual o nome do aluno? ")
      listaNome.append(nomeAluno)
      alunos.append(nomeAluno[:])
      print(alunos)

      while True:
        rm = int(input("Digite o RM do aluno: "))
      
        if rm not in listaRm:
          listaRm.append(rm)
          alunos.append(rm[:])
          print(alunos)
          break

        else:
          print("\nRm Duplicado! Valor não adicionado.")
          continue

      if rm == 0:
        break

    
      else:
        serie = str(input("Qual a série que o aluno esta cursando: (2ª, 3ª, 4ª e 5ª) "))
        
        while serie != "2ª" and serie != "3ª" and serie != "4ª" and serie != "5ª":
          print("Informação inválida, digite a série corretamente (2ª, 3ª, 4ª e 5ª) ")
          serie = str(input("Qual a série que o aluno esta cursando: (2ª, 3ª, 4ª e 5ª) "))


        listaSerie.append(serie)
        alunos.append(serie[:])
        print(alunos)

      contador =+ 1

# * Opção 2

  if menu == 2:
    print("\n --- 2 - Fazer Inscrições ---")
    rmInscricao = int(input("Digite o RM do aluno: "))
    print(listaRm)



    if rmInscricao in listaRm:
      print("\n ====== Lista das oficinas ====== ")

      print(listaSerie)

      if serie == "2ª":
        print("\n1 - Segunda | Criar e contar histórias | Matutino")
        print("2 - Quarta | A língua de sinais | Matutino")
        print("3 - Quarta | O mundo da imaginação | Vespertino")
        print("4 - Sexta | Criando e recriando com emojis | Vespertino")
        oficina = int(input("\nQual oficina deverá ser cadastrada? "))

      if serie == "3ª":
        print("\n1 - Segunda | Criar e contar histórias | Matutino")
        print("2 - Terça | Teatro: Luz, Câmera e Ação | Matutino")
        print("3 - Quarta | A língua de sinais | Matutino")
        print("4 - Terça | O corpo fala | Vespertino")
        oficina = int(input("\nQual oficina deverá ser cadastrada? "))

      if serie == "4ª":
        print("\n1 - Terça | Teatro: Luz, Câmera e Ação | Matutino")
        print("2 - Quarta | A língua de sinais | Matutino")
        print("3 - Quinta | Expressão Artística | Matutino")
        print("4 - Segunda | Leitura drámatica | Vespertino")
        oficina = int(input("\nQual oficina deverá ser cadastrada? ")) 

      if serie == "5ª":
        print("\n1 - Quarta | A língua de sinais | Matutino ---")
        print("2 - Quinta | Expressão Artística | Matutino ---")
        print("3 - Sexta | Soletrando | Matutino ---")
        print("4 - Quinta | Leitura dinâmica | Vespertino")
        oficina = int(input("\nQual oficina deverá ser cadastrada? "))
        

    else:
      print("Aluno não cadastrado. Favor procurar a coordenação do Fundamental I")
    continue

# * Opção 

  if menu == 3:
    print("\n --- 3 - Listar Inscrições ---")
    continue

# * Opção 4

  if menu == 4:
    print("FIM")
    break
