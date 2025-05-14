from scapy.utils import wrpcap

captured_packets = []

def store_packet(packet):
    captured_packets.append(packet)

def save_to_file(filename="capture.pcap"):
    if captured_packets:
        wrpcap(filename, captured_packets)
        print(f"[bold green]Saved to {filename}[/bold green]")
    else:
        print("[red]No packets to save[/red]")
