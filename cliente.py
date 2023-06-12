import socket
import time

# Configurações do cliente
HOST = 'localhost'  # Endereço IP do servidor
PORT = 50000  # Porta utilizada pelo servidor

rtt_min = 0
rtt_max = 0
rtt_total = 0
pacotes = 0

# Criação do socket UDP
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
timeout = 1
sock.settimeout(timeout) #1 segundo de timeout

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
        rtt_total += rtt
        print(f'RTT do pacote {i}: {rtt:.15f} ms')
        if (rtt < rtt_min or rtt_min == 0):
            rtt_min = rtt
        if (rtt > rtt_max or rtt_max == 0):
            rtt_max = rtt
        pacotes = pacotes + 1
    except:
        print(f"TIMEOUT do pacote {i}")
    i = i+1
print("")
print(f"Maior RTT: {rtt_max:.7f} ms")
print(f"Menor RTT: {rtt_min:.7f} ms")
print(f"RTT Médio: {(rtt_total/10):.7f} ms")
print(f"Taxa de perda de pacotes: {100-((pacotes/10)*100)}%")

print("Fechando conexão com o servidor...")
sock.close()

#https://github.com/selbyk/python-udp-ping