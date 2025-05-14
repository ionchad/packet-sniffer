from scapy.all import sniff

def capture_packets(interface="eth0", packet_count=0, filter_exp=None, callback=None):
    """
    Captures packets on the given interface.
    - interface: network interface name (e.g., "eth0", "Wi-Fi")
    - packet_count: 0 = unlimited
    - filter_exp: BPF filter (e.g., "tcp", "udp port 53")
    - callback: function to call on each packet
    """
    sniff(
        iface=interface,
        prn=callback,
        filter=filter_exp,
        count=packet_count,
        store=False
    )
