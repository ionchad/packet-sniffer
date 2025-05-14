from sniffer.capture import capture_packets
from sniffer.display import format_packet
from sniffer.filters import build_filter
from sniffer.save import store_packet, save_to_file

def packet_callback(packet):
    format_packet(packet)
    store_packet(packet)

def main():
    import argparse

    parser = argparse.ArgumentParser(description="Python Packet Sniffer")
    parser.add_argument("--tcp", action="store_true")
    parser.add_argument("--udp", action="store_true")
    parser.add_argument("--icmp", action="store_true")
    parser.add_argument("--port", type=int, help="Filter by port")
    parser.add_argument("--interface", default="eth0")
    parser.add_argument("--count", type=int, default=0)
    parser.add_argument("--save", action="store_true")

    args = parser.parse_args()
    filter_exp = build_filter(args.tcp, args.udp, args.icmp, args.port)

    try:
        capture_packets(
            interface=args.interface,
            packet_count=args.count,
            filter_exp=filter_exp,
            callback=packet_callback
        )
    except KeyboardInterrupt:
        print("[yellow]Interrupted by user[/yellow]")

    if args.save:
        save_to_file()

if __name__ == "__main__":
    main()
