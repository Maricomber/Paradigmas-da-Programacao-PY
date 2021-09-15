while True:
    opcao = int(input('\nVocê deseja executar quais questões? \n'
                            + '1- Questão digite: 1 \n'
                            + '2- Questão digite: 2 \n'
                            + '3- Questão digite: 3 \n'
                            + '4- Questão digite: 4 \n'
                            + '5- Questão digite: 5 \n'
                            + '0- Sair \n \n \n'))
    if opcao == 1 :
        import exercicio1
    elif opcao == 2 : 
        import exercicio2
    elif opcao == 3 : 
        import exercicio3
    elif opcao == 4 : 
        import exercicio4
    elif opcao == 5 : 
        import exercicio5
    else:
        break
    
