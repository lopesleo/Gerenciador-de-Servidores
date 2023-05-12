import os
import subprocess


def main():
    listaServidores()
    while True:

        servidor = refresh()
        aux = escolha(servidor)
        if (type(aux) == int):
            create(aux)
        del aux, servidor
        print("\n")


def refresh():
    with open('C://Cirius//Servidores//Servidores.txt', 'r') as f:  # pega o conteudo do arquivo servidores.txt
        for valor in f:
            return valor.split(',')


def addNewServer():  # adiciona um novo servidor na lista
    os.system("cls")
    tipo = ["Escreva o nome do servidor: ", "Escreva o nome do banco de dados: ", "Escreva o IP do servidor: ",
            "Cole a linha do servidor.txt: "]

    x = input("""Digite 1 para adicionar o servidor colando a linha do servidor.txt ou Digite 2 para adicionar o servidor digitando os dados: 
""")
    match x:

        case '1':
            os.system("cls")
            nome = input("digite o nome do servidor: ")
            serv = input("Cole o servidor.txt: ")
            print(nome)
            with open('C://Cirius//Servidores//Lista//{}.txt'.format(nome), 'w+') as f:
                f.write(serv)
            f.close()
            with open("C://Cirius//Servidores//Servidores.txt", 'a') as f:
                f.write(nome + ",")
            f.close()

        case '2':
            os.system("cls")
            dados = [];

            while len(dados) < 3:
                x = input("{}".format(tipo[len(dados)]))
                dados.append(x)

            with open("C://Cirius//Servidores//Servidores.txt", 'a') as f:
                f.write(dados[0] + ",")
            f.close()

            with open('C://Cirius//Servidores//Lista//{}.txt'.format(dados[0]), 'a+') as f:
                f.write("C:\|root|123456|3306|{}|{}".format(dados[1], dados[2]))
            f.close()

        case _:
            addNewServer()


def error():  # reporta erro
    print("Error: Opção inválida, tente novamente. ")


def escolha(servidor):  # escolha do servidor e funcoes
    servidor = refresh()
    choice = (input("digite a opção desejada: "))

    if choice == 'add':
        addNewServer()
        del choice
        choice = 0

    if choice == 'sair':
        try:
            os._exit(os.X_OK)

        except SystemExit:
            exit()

    if choice == 0 or choice == '0':
        listaServidores()

    if choice == 'kill':
        restart()
        del choice
        choice = 0

    try:
        aux = int(choice)

        if aux in (range(1, len(servidor))):  # validação da escolha do usuário

            return aux
    except ValueError:
        error()


def listaServidores():  # exibe a lista
    servidor = refresh()
    os.system("cls")
    print("escolha o servidor desejado: \n")

    for i in range(0, len(servidor) - 1):  # escolha do servidor
        print("[{}]  - {}".format(i + 1, servidor[i]))

    print("\n[0] - Listar servidores\n[sair] - Para sair\n[add] - Adicionar novo servidor\n[kill] - finalizar o programa\n")


def restart():  # reinicia o programa
    with open("C://Cirius//versao//cirius//versao.txt", 'r') as f:
        for valor in f:
            versao = valor  # versao do servidor
    os.system("taskkill /f /im  cirius_{}.exe".format(versao))



def create(aux):  # reescreve o Servidor.txt
    print("Criando arquivo")  # copia o conteudo dos arquivos .txt
    servidor = refresh()
    with open('C://Cirius//Servidores//Lista//{}.txt'.format(servidor[aux - 1]), 'r') as f:
        for valor in f:
            arquivo = valor
        f.close()
        print(arquivo)

    with open('C://Cirius//Servidor.txt', 'w') as f:  # reescreve o Servidor.txt
        for valor in arquivo:
            f.write(valor)
        f.close()
    print("Arquivo criado com sucesso")
    subprocess.call("C://Cirius//versao//Atualizador_CIRIUS.exe")  # chama o atualizador



main()
