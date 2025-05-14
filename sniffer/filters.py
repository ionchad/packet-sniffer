def build_filter(tcp=False, udp=False, icmp=False, port=None):
    filters = []
    if tcp:
        filters.append("tcp")
    if udp:
        filters.append("udp")
    if icmp:
        filters.append("icmp")
    if port:
        filters.append(f"port {port}")
    return " and ".join(filters)
