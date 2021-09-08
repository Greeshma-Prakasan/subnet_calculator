def to_binary(ip):
    b = bin(ip).replace("0b","")
    r = (8-len(b))*'0'+b if len(b) != 8 else b
    return r


def get_ip(ip):
    lip = ip.split(".")
    l = [to_binary(int(x)) for x in lip]
    ip = ".".join(l)
    ip1 = "".join(l)
    return ip,ip1

# print(get_ip("192.168.0.0"))

def get_subnet_mask(s):
    if "." in s:
        ret = get_ip(s)
    else:
        r = int(s)*'1'+(32-int(s))*'0'
        x = 8
        ret = [r[i: i + x] for i in range(0, len(r), x)]
        ret = ".".join(ret), "".join(ret)
    return ret

# print(get_subnet_mask("16"))

def get_nw_address(ip,sub):
    x = 8
    ip = get_ip(ip)[1]
    sub = get_subnet_mask(sub)[1]
    c = sub.count("1")
    res = ip[:c]+(32-c)*"0"
    res = [res[i: i + x] for i in range(0, len(res), x)]
    res = ".".join([str(int("0b"+x,2)) for x in res])
    return res

# print(get_nw_address("192.168.0.0","16"))

def get_broadcast_address(ip,sub):
    x = 8
    ip = get_ip(ip)[1]
    sub = get_subnet_mask(sub)[1]
    c = sub.count("1")
    res = ip[:c] + (32 - c) * "1"
    res = [res[i: i + x] for i in range(0, len(res), x)]
    res = ".".join([str(int("0b"+x,2)) for x in res])
    return res

# print(get_broadcast_address("192.168.0.0","16"))

def get_no_of_ips(sub):
    if "." in sub:
        sub = get_ip(sub)[1]
        c1 = sub.count("1")
        c = sub.count("0")
        n = 2**c - 2
    else:
        n = 2**(32 - int(sub)) - 2
    return n


# print(get_no_of_ips("30"))



