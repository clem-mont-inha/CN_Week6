import socket, time, threading

server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_socket.bind(('localhost', 12345))

def handle_client(client_address):
    start_time = time.time()
    data, addr = server_socket.recvfrom(1024)
    end_time = time.time()
    latency = end_time - start_time
    print(f"Received { data } from { addr } with latency: { latency } seconds")
    server_socket.sendto(data, addr)

def main():
    while True:
        threading.Thread(target=handle_client, args=(server_socket ,)).start()

if __name__ == "__main__":
    main()