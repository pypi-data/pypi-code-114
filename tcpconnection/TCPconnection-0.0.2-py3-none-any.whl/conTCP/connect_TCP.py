import socket
import sys

def connectTCP():
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM, 0)
    except socket.error as e:
        print("A conexão falhou.")
        print("Erro: {}'.format(e)")
        sys.exit()
    print("Socket criado com sucesso.")

    hostalvo = input("Digite o Host ou IP a ser conectado: ")
    portaalvo = input("Digite a porta a ser conectada: ")

    try:
        s.connect((hostalvo, int(portaalvo)))
        print("Cliente TPC conectado com sucesso no Host: " + hostalvo + " na Porta: " + portaalvo)
        s.shutdown(2)
    except socket.error as e:
        print("Não foi possível conectar no Host: "+ hostalvo + "na Porta" + portaalvo)
        print("Erro: {}".format(e))
        sys.exit()

if __name__ == "__main__":
    connectTCP()