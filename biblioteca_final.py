import os
import mysql.connector
from datetime import date


##realizando conexão com o Banco biblioteca (host: local)
con = mysql.connector.connect(host='localhost', database='biblioteca', user='root', password='suporte')

#verifica a conexão
#if con.is_connected():
#    db_info = con.get_server_info( )
#    print ("Conectado ao banco de dados = ", db_info)

    
######################################################  -------------- Encerra a conexão com banco de dados ------------- #######################
def encerra():
#fechamento de conexão
    try:
        if con.is_connected():
            cursor.close()
            con.close()
            exit()

    except NameError:
        if con.is_connected():
            con.close()
            exit()

##############################  -------------- funcao quando o usuário digita uma opção que não é válida ------------- ##########################
def invalido():
    print("Informe uma opção válida\n")
    print("Direcionado ao menu principal\n\n")
    os.system("pause")
    menu()


######################################################  -------------- Menu de opção principal ------------- ####################################
def opcao(case):
    if case == "1":
        print("-----Informe a opção desejada-----\n")
        print("1 - Cadastrar novo usuário\n")
        print("2 - Editar usário cadastrado\n")
        print("3 - Remover usário cadastrado\n")
        print("0 - Voltar ao Menu\n")
        opcao= int(input())
        if opcao == 1:
            inserir()
        elif opcao == 2:
            atualizar()
        elif opcao == 3:
            remove_user()
        elif opcao == 0:
            menu()
        else:
            invalido()
            
    elif case == "2":
        print("-----Informe a opção desejada-----\n")
        print("1 - Cadastrar novo Livro\n")
        print("2 - Editar Livro cadastrado\n")
        print("3 - Remover Livro cadastrado\n")
        print("0 - Voltar ao Menu\n")
        opcao= int(input())
        if opcao == 1:
            inserir_livro()
        elif opcao == 2:
            atualizar_livro()
        elif opcao == 3:
            remove_livro()
        elif opcao == 0:
            menu()
        else:
            invalido()
    elif case == "3":
        cadastrar_empres()
    elif case == "4":
        consultar()
    elif case == "0":
        sair()
    else:
        invalido()

######################################################  -------------- FUNÇÃO DE CADASTRO EMPRESTIMO------------- ####################################

##funcção para cadastrar empréstimo
def cadastrar_empres():
    print("Preencha os dados para cadastrar novo empréstimo\n\n")
    cpf = input("Informe o cpf do usuário: ")
    id_livro = input("Informe o ID do livro: ")
    dia_retirada = input("Informe a dia de retirada: ") ##usar função datetime para coletar a data
    mes_retirada = input("Informe o mes de retirada: ")
    ano_retirada = input("Informe o ano de retirada: ")
    dia_devolucao = input("Informe a dia de devolução: ")
    mes_devolucao = input("Informe o mes de devolução: ")
    ano_devolucao = input("Informe o ano de devolução: ")
    retirada=ano_retirada+mes_retirada+dia_retirada
    entrega=ano_devolucao+mes_devolucao+dia_devolucao

    print("\n")
    comando = "INSERT INTO emprestimo VALUES(NULL,'"+cpf+"',"+id_livro+","+retirada+"," +entrega+");"
    print("Empréstimo cadastrado com sucesso\n"),
    #print(comando)
    cursor = con.cursor()
    cursor.execute(comando)
    con.commit()
    os.system("pause")
    menu()
    

##Função e remover funcionário
def remove_user():
    cod = input("Informe o cpf do usuário que deseja excluir: ")
    try:  
        comando = "DELETE from clientes where cpf='"+cod+"';"
        cursor = con.cursor()
        #print(comando)
        cursor.execute(comando)
        con.commit()
        os.system("pause")
        menu()
        
    except:
        comando = "DELETE from emprestimo where cpf='"+cod+"';"
        cursor = con.cursor()
        cursor.execute(comando)
        con.commit()
        comando = "DELETE from clientes where cpf='"+cod+"';"
        cursor = con.cursor()
        cursor.execute(comando)
        con.commit()
        os.system("pause")
        menu()

#Função que remove livro
def remove_livro():
    cod = input("Informe o ID do livro que deseja excluir: ")
    try:     
        comando = "DELETE from livros where id="+cod;
        cursor = con.cursor()
        #print(comando)
        cursor.execute(comando)
        con.commit()
        os.system("pause")
        menu()
    except:
        comando = "DELETE from emprestimo where id="+cod;
        cursor = con.cursor()
        cursor.execute(comando)
        con.commit()
        comando = "DELETE from livros where id="+cod;
        cursor = con.cursor()
        cursor.execute(comando)
        con.commit()
        os.system("pause")
        menu()
    
######################################################  -------------- FUNÇÃO DE CADASTRO USUÁRO ------------- ####################################
 
def inserir():

    try:
        print("Preencha os dados para cadastrar novo usuário\n\n")
        cpf = input("Informe o cpf do usuário: ")
        nome = input("Informe o nome do usuário: ")
        telefone = input("Informe o Telefone do usuário: ")
        endereco = input("Informe o Endereço do usuário: ")
        dia = input("Informe a dia de nascimento: ")
        mes = input("Informe o mes de nascimento: ")
        ano = input("Informe o ano de nascimento: ")
        nascimento=ano+mes+dia
        sexo = input("Informe o sexo do usuário ('M' ou 'F'): ")
        print("\n")
        comando = "INSERT INTO clientes VALUES('"+cpf+"', '"+nome+"','"+telefone+"', '"+endereco+"',"+nascimento+", '"+sexo+"');"   
        #print(comando)
        cursor = con.cursor()
        cursor.execute(comando)
        con.commit()
        print("Usário cadastrado com sucesso\n")
        os.system("pause")
        menu()

    except mysql.connector.errors.IntegrityError:
        print("Usuário já cadastrado\n")

    except mysql.connector.errors.DataError:
        print("Algum dado foi inserido incorreto!!!\n Insira o CPF (apenas números)\n Data de nascimento o dia, depois o mês e o ano\n O sexo apenas uma  letra (M ou F) conforme solicitado\n") 

    except:
        print("erro ao cadastrar usuário, tente novamente!")
    
    ##funcao que edita usuário no BD
def atualizar():
    iden = input("Informe o CPF da pessoa que você deseja alterar: ")
    print("Informe qual campo você deseja alterar: \n")
    print("1 - Nome\n")
    print("2 - Telefone\n")
    print("3 - Endereço\n")
    print("0 - Voltar ao Menu\n")
    op = int(input())
  
    if op == 0:
        menu()

    elif op == 1:
        nome=input("Informe o nome correto da pessoa: \n")
        comando = "UPDATE clientes set nome='"+nome+"' where cpf="+iden;

    elif op == 2:
        tel=input("Informe o novo Telefone da pessoa: \n")
        comando = "UPDATE clientes set telefone='"+tel+"' where cpf="+iden;

        
    elif op == 3:
        end=input("Informe o novo endeço da pessoa: \n")
        comando = "UPDATE clientes set endereco'"+end+"' where cpf="+iden;
        
    elif op == 0:
        print("Você desejou sair\n Direcionando ao Menu Principal\n")
        menu()

    #print(comando)
    cursor = con.cursor()
    cursor.execute(comando)
    con.commit()
    print("dado alterado com sucesso\n")
    os.system("pause")
    menu()


##funcao para cadastrar ou editar livros
    ##funcao que insere livro no BD
def inserir_livro():
    print("Preencha os dados para cadastrar novo livro\n\n")
    nome = input("Informe o nome do livro: ")
    autor = input("Informe o nome do autor: ")
    ano = input("Informe o ano de publicação: ")
    print("\n")
    comando = "INSERT INTO livros VALUES(NULL, '"+nome+"', '"+autor+"',"+ano+");"
    print("Usário cadastrado com sucesso\n"),
    #print(comando)
    cursor = con.cursor()
    cursor.execute(comando)
    con.commit()
    os.system("pause")
    menu()
    
    ##funcao que edita livro no BD
def atualizar_livro():
    iden = input("Informe o ID do livro que você deseja alterar: ")
    print("Informe qual campo você deseja alterar: \n")
    print("1 - Nome do livro\n")
    print("2 - Nome do autor\n")
    print("3 - Ano de publicação\n")
    print("0 - Voltar ao Menu\n")
    op = int(input())
  
    if op == 0:
        menu()

    elif op == 1:
        nome=input("Informe o nome correto do livro: \n")
        comando = "UPDATE livros set nome='"+nome+"' where id="+iden;

    elif op == 2:
        autor=input("Informe o nome correto do autor: \n")
        comando = "UPDATE livros set autor='"+autor+"' where id="+iden;

    elif op == 3:
        ano=input("Informe o ano correto de publicação do livro: \n")
        comando = "UPDATE livros set idade'"+ano+"' where id="+iden;
    elif op == 0:
        print("Você desejou sair\n Direcionando ao Menu Principal\n")
        menu()
    else:
        invalido()

    #print(comando)
    cursor = con.cursor()
    cursor.execute(comando)
    con.commit()
    print("dado alterado com sucesso\n")
    os.system("pause")
    menu()



########################################################  -------------- FUNÇOES DOS RELATÓRIOS ------------- ####################################

def consultar():
    print("------Consulta de Relatório------\n")
    print("Informe a opção correspondente ao relatório que deseja consultar: \n")
    print(" 1- Todos os usuários cadastrados\n")
    print(" 2- Todos os livros cadastrados\n")
    print(" 3- Todos os empréstimos cadastrados\n")
    print(" 4- Buscar um usuário específico\n")
    print(" 5- Buscar um livro específico\n")
    print(" 0 - Voltar ao Menu\n")
    op = int(input())

    #Relatório de todos usuários cadastrados
    if op == 1:
        print("teste\n")
        consulta_sql = "select * from clientes;"
        cursor = con.cursor( )
        cursor.execute(consulta_sql)
        linhas = cursor.fetchall()
        print ("Numero total de pessoas cadastradas: \n", cursor.rowcount)
        print ("--------------------------------------\n")
        print("Exibindo as pessoas cadastradas: \n")

        for linha in linhas:
            print("cpf........... = ", linha[0])
            print("nome.......... = ", linha[1])
            print("telefone...... = ", linha[2])
            print("Endereço...... = ", linha[3])
            print("Nascimento.... = ", linha[4])
            print("sexo.......... = ", linha[5])
            print("\n")



    #Relatório de todos livros cadastrados
    elif op == 2:
        consulta_sql = "select * from livros;"
        cursor = con.cursor( )
        cursor.execute(consulta_sql)
        linhas = cursor.fetchall()
        print ("Numero total de livros cadastrados: \n", cursor.rowcount)
        print ("--------------------------------------\n")
        print("Exibindo livros cadastradas: \n")

        for linha in linhas:
            print("id....... = ", linha[0])
            print("nome..... = ", linha[1])
            print("autor.... = ", linha[2])
            print("ano...... = ", linha[3])
            print("\n")

    #Relatório de todos empréstimos cadastrados
    elif op == 3:
        print("------Consulta de Empréstimos------\n")
        print("Informe a opção de consulta: \n")
        print(" 1 - Consultar todos os empréstimos\n")
        print(" 2 - Consultar 1 empréstimo específico\n")
        print(" 0 - Voltar ao Menu\n")
        op_empre= int(input())
        

        if op_empre == 1:
            consulta_sql = "select * from emprestimo join clientes on emprestimo.cpf=clientes.cpf join livros on emprestimo.id=livros.id;"
            cursor = con.cursor( )
            cursor.execute(consulta_sql)
            linhas = cursor.fetchall()
            print ("Numero total de empréstimos realizados: \n", cursor.rowcount)
            print ("--------------------------------------\n")
            print("Exibindo empréstimos: \n")

            for linha in linhas:
                print("id do emprestimo...... = ", linha[0])
                print("data de retirada...... = ", linha[3])
                print("data de entrega....... = ", linha[4])
                print("CPF do Cliente........ = ", linha[5])
                print("Nome do Cliente....... = ", linha[6])
                print("Nome do livro......... = ", linha[12])
                print("Autor do Livro........ = ", linha[13])
                print("\n")



        elif op_empre == 2:
            print("Informe o CPF do usuário: ");
            cpf=input()
    
            consulta_sql = "select * from emprestimo join clientes on emprestimo.cpf=clientes.cpf join livros on emprestimo.id=livros.id where clientes.cpf='"+cpf+"';"
            cursor = con.cursor( )
            cursor.execute(consulta_sql)
            linhas = cursor.fetchall()
            print ("--------------------------------------\n")
            print("Exibindo empréstimos: \n")

            for linha in linhas:
                print("id do emprestimo...... = ", linha[0])
                print("data de retirada...... = ", linha[3])
                print("data de entrega....... = ", linha[4])
                print("CPF do Cliente........ = ", linha[5])
                print("Nome do Cliente....... = ", linha[6])
                print("Nome do livro......... = ", linha[12])
                print("Autor do Livro........ = ", linha[13])
                print("\n")        

        elif op_empre == 0:
            menu()

        else:
            invalido()


    #Buscar um usuário especifico
    elif op == 4:
        #try:
            cpf=input("informe o cpf do usuário: ")
            consulta_sql = "select * from clientes where cpf='"+cpf+"';"
            cursor = con.cursor( )
            cursor.execute(consulta_sql)
            linhas = cursor.fetchall()
            #print(type(linhas))
            if linhas ==[]:
                print("Usuário não encontrado\n")

            else:
                print("Exibindo dados do usuário: \n")

                for linha in linhas:
                    print("cpf........... = ", linha[0])
                    print("nome.......... = ", linha[1])
                    print("endereço...... = ", linha[2])
                    print("telefone...... = ", linha[3])
                    print("Nascimento.... = ", linha[4])
                    print("sexo.......... = ", linha[5])
                    print("\n")

        #except:
            



    #Buscar um livro especifico
    elif op == 5:
        print("Selecione qual dado deseja informar para realizar a busca: \n")
        print("1 - ID do livro\n")
        print("2 - nome do autor\n")
        print("3 - nome do livro\n")
        opcao=int(input())


        ##Buscando livro pelo ID 
        if opcao == 1:
            id1 = input("Informe o ID: ")
            consulta_sql = "select * from livros where id='"+id1+"';"
            cursor = con.cursor( )
            cursor.execute(consulta_sql)
            linhas = cursor.fetchall()
            if linhas == []:
                print("Livro não encontrado\n")
            else:
                print("Exibindo dados do livro: \n")

                for linha in linhas:
                    print("id....... = ", linha[0])
                    print("nome..... = ", linha[1])
                    print("autor.... = ", linha[2])
                    print("ano...... = ", linha[3])
                    print("\n")

        ##Buscando livro pelo Nome do livro 
        elif opcao == 2:
            id1 = input("Informe o nome do livro: ")
            consulta_sql = "select * from livros where nome='"+id1+"';"
            cursor = con.cursor( )
            cursor.execute(consulta_sql)
            linhas = cursor.fetchall()
            
            if linhas == []:
                print("Livro não encontrado\n")

            else:
                print("Exibindo dados do livro: \n")

                for linha in linhas:
                    print("id....... = ", linha[0])
                    print("nome..... = ", linha[1])
                    print("autor.... = ", linha[2])
                    print("ano...... = ", linha[3])
                    print("\n")

        ##Buscando livro pelo autor 
        elif opcao == 3:
            id1 = input("Informe o nome do autor: ")
            consulta_sql = "select * from livros where autor='"+id1+"';"
            cursor = con.cursor( )
            cursor.execute(consulta_sql)
            linhas = cursor.fetchall()
            if linhas == []:
                print("Livro não encontrado\n")

            else:
                print("Exibindo dados do livro: \n")

                for linha in linhas:
                    print("id....... = ", linha[0])
                    print("nome..... = ", linha[1])
                    print("autor.... = ", linha[2])
                    print("ano...... = ", linha[3])
                    print("\n")

        else:
            invalido()
            
        

    print("\nPrecione Enter para retornar ao menu principal")
    os.system("pause")    
    menu()


######################################################  -------------- FUNÇÃO QUE FINALIZA O PROGRAMA ------------- #######################
def sair():
    print("Programa finalizado!\n")
    print("Até logo\n")
    os.system("pause")
    encerra()
    

######################################################  -------------- funcao do menu principal ------------- #########################    
def menu():
    os.system("cls")
    print("--------------------Menu Principal-----------------")
    print("###################################################\n")
    print("Informe o número correspondente a opção desejada\n\n")
    print("1 - Cadastrar, Editar ou Remover usuário cadastrado\n")
    print("2 - Cadastrar, Editar ou Remover Livro cadastrado\n")
    print("3 - Cadastrar Novo Empréstimo\n")
    print("4 - Relatórios\n")
    print("0 - Sair\n")

    case = input()
    opcao(case)
    os.system("pause")


##após reconhecer todas as funcoes do programa, invocar a funcao incial    
######################################################  -------------- chamando a funcao menu principal ------------- #########################
menu()

