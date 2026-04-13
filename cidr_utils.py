import ipaddress

def is_ip_in_cidr(ip, cidr):
    if not isinstance(ip, str) or not isinstance(cidr, str):
        raise ValueError("Both IP and CIDR must be strings.")
    try:
        net = ipaddress.ip_network(cidr, strict=False)
        addr = ipaddress.ip_address(ip)
        return addr in net
    except ValueError as e:
        raise ValueError(f"Invalid IP address or CIDR format: {e}")