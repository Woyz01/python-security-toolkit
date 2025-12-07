import socket
from typing import List, Dict


def scan_port(host: str, port: int, timeout: float = 1.0) -> bool:
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(timeout)

    # sock ağ bağlantısı kurmaya yarayan bir uç noktadır.
    # bilgisayarlar arası bağlantı kurmaya yarar.
    try:
        result = sock.connect_ex((host, port))
        # connect_ex 0 dönerse bağlantı başarılı (port açık)
        return result == 0
    except socket.error:
        #herhangi bir ağ hatasında kapalı varsay
        return False
    finally:
        sock.close()

def scan_ports(host: str, ports: list[int], timeout: float = 1.0) -> dict[int, bool]:
    results: dict[int, bool] = {}

    for port in ports:
        is_open = scan_port(host, port, timeout)
        results[port] = is_open

    return results


