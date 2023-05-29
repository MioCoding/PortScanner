import socket

def scan_port(target_host, target_port):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM); sock.settimeout(2); result = sock.connect_ex((target_host, target_port))
        
        if result == 0: print(f"Port {target_port} is open")
        else: print(f"Port {target_port} is closed")
        
        sock.close()
    
    except socket.error: print(f"Could not connect to {target_host}")

def main():
    target_host = "localhost"; port_range = range(1, 100)
    
    for target_port in port_range: scan_port(target_host, target_port)

if __name__ == "__main__":
    main()
