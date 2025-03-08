import socket

def scan(target):
    print(f"\n[+] Scanning target: {target}")
    
    ip, port = target.split(":") if ":" in target else (target, None)

    if port:
        ports = [int(port)]  # If a specific port is given, scan only that
    else:
        ports = range(20, 1025)  # Scan common ports

    for port in ports:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(0.5)
        result = s.connect_ex((ip, port))
        if result == 0:
            print(f"[*] Port {port} is OPEN on {ip}")
        s.close()
