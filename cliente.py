import socket
import time

# Configurações do cliente
HOST = 'localhost'  # Endereço IP do servidor
PORT = 50000  # Porta utilizada pelo servidor

# Criação do socket UDP
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
timeout = 1
sock.settimeout(timeout)

# Loop principal do cliente
i = 1
while (i <= 10):
    # Leitura da mensagem a ser enviada
    message = ("Hello, world %i" % i)
    try:
        # Envio da mensagem ao servidor
        inicio = time.time()
        sock.sendto(message.encode(), (HOST, PORT))

        # Recebimento da resposta do servidor
        response, addr = sock.recvfrom(1024)
        fim = time.time()
        print("Resposta do servidor: %s || " % response.decode(), end="")
        rtt = (fim - inicio) * 1000
        print(f'RTT do pacote {i}: {rtt:.4f} ms')
    except:
        print("TIMEOUT")
    i = i+1

print("Fechando conexão com o servidor...")
sock.close()

#https://github.com/selbyk/python-udp-ping