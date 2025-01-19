import socket
import ssl

def vpn_client(proxy_host, proxy_port, target_host, target_port, message):
    context = ssl.create_default_context(ssl.Purpose.SERVER_AUTH)
    context.load_verify_locations("server.crt")

    raw_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    raw_socket.connect((proxy_host, proxy_port))
    conn = context.wrap_socket(raw_socket, server_hostname=proxy_host)

    try:
        # Отправляем прокси-серверу информацию о цели
        conn.send(f"{target_host}:{target_port}".encode('utf-8'))

        # Отправляем сообщение через прокси
        conn.send(message.encode('utf-8'))

        # Получаем ответ от целевого сервера (через прокси)
        data = conn.recv(1024)
        print(f"Received from server: {data.decode('utf-8')}")
    finally:
        conn.close()

if __name__ == "__main__":
    proxy_host = 'c3.play2go.cloud'
    proxy_port = 20057
    target_host = 'www.google.com'  # Пример целевого хоста
    target_port = 80             # Пример целевого порта
    message = "GET / HTTP/1.1\r\nHost: www.google.com\r\nConnection: close\r\n\r\n" # Простой HTTP-запрос
    vpn_client(proxy_host, proxy_port, target_host, target_port, message)