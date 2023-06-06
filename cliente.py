import socket
import time

# Configurações do cliente
HOST = 'localhost'  # Endereço IP do servidor
PORT = 50000  # Porta utilizada pelo servidor

rtt_min = 0
rtt_max = 0
rtt_total = 0

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
        rtt_total += rtt
        print(f'RTT do pacote {i}: {rtt:.4f} ms')
        if (i == 1):
            rtt_min = rtt
            rtt_max = rtt
        if (rtt <= rtt_min):
            rtt_min = rtt
        if (rtt >= rtt_max):
            rtt_max = rtt
    except:
        print("TIMEOUT")
    i = i+1

print(f"Maior RTT: {rtt_max:.4f}")
print(f"Menor RTT: {rtt_min:.4f}")
print(f"RTT Médio: {rtt_total/10}")

print("Fechando conexão com o servidor...")
sock.close()

#https://github.com/selbyk/python-udp-ping