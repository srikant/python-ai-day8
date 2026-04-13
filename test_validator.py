import pytest
from cidr_utils import is_ip_in_cidr

def test_ip_in_range_simple():
    ip = "192.168.1.10"
    cidr = "192.168.1.0/24" # 192.168.1.x (0-255)
    result = is_ip_in_cidr(ip, cidr)
    assert result is True

def test_ip_not_in_range():
    assert is_ip_in_cidr("10.0.0.1","192.168.1.0/24") is False

def test_edge_cases():
    assert is_ip_in_cidr("192.168.1.0", "192.168.1.0/24") is True
    assert is_ip_in_cidr("192.168.1.255", "192.168.1.0/24") is True

def test_invalid_ip():
    with pytest.raises(ValueError):
        is_ip_in_cidr("invalid_ip", "192.168.1.0/24")

def test_invalid_cidr():
    with pytest.raises(ValueError):
        is_ip_in_cidr("192.168.1.10", "invalid_cidr")