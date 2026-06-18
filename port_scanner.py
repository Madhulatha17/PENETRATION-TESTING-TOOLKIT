import socket

def scan_ports(host):
    print(f"\nScanning {host}...\n")

    for port in range(1, 1025):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(0.5)

        result = sock.connect_ex((host, port))

        if result == 0:
            print(f"Port {port} is OPEN")

        sock.close()
