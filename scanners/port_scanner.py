import socket

def scan_ports(target_host, port_range):
    """
    Scans a range of ports on a target host to identify open ports.
    
    Args:
        target_host (str): The IP address or hostname of the target host.
        port_range (tuple): A tuple containing the start and end port numbers to scan (e.g., (1, 1000)).
    
    Returns:
        list: A list of open ports on the target host.
    """
    open_ports = []
    
    try:
        target_ip = socket.gethostbyname(target_host)
    except socket.gaierror:
        return f"Could not resolve hostname: {target_host}"
    
    for port in range(port_range[0], port_range[1] + 1):
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(1)  # Set a timeout to prevent the scan from hanging
            result = sock.connect_ex((target_ip, port))
            
            if result == 0:
                open_ports.append(port)
            
            sock.close()
        except socket.error as e:
            return f"Could not connect to {target_host}:{port}. Error: {e}"
    
    return open_ports