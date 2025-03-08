from scapy.all import sniff

def sniff_packets():
    print("[+] Starting packet sniffing... (Press Ctrl+C to stop)")
    
    def process_packet(packet):
        print(packet.summary())

    sniff(prn=process_packet, store=False)  # Capture packets and print summary
