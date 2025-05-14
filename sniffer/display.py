from rich import print
from scapy.layers.inet import IP, TCP, UDP, ICMP

def format_packet(packet):
    if IP in packet:
        ip = packet[IP]
        proto = ip.proto
        src = ip.src
        dst = ip.dst
        if proto == 6 and TCP in packet:
            protocol = "TCP"
            sport = packet[TCP].sport
            dport = packet[TCP].dport
        elif proto == 17 and UDP in packet:
            protocol = "UDP"
            sport = packet[UDP].sport
            dport = packet[UDP].dport
        elif proto == 1 and ICMP in packet:
            protocol = "ICMP"
            sport = dport = "-"
        else:
            protocol = str(proto)
            sport = dport = "-"
        
        print(f"[cyan]{src}:{sport}[/cyan] → [magenta]{dst}:{dport}[/magenta] [green]{protocol}[/green]")
