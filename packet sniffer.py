from scapy.all import sniff, IP, TCP, UDP, Raw
import datetime

# =========================================================
# Network Packet Sniffer & Traffic Analyzer (Topic 3)
# This tool captures live network packets and displays:
# Type, Size, Origin, Destination, and Content
# =========================================================

def process_packet(packet):
    # 1. Check if the packet has an IP layer
    if IP in packet:
        src_ip = packet[IP].src
        dst_ip = packet[IP].dst
        size = len(packet)
        
        # Get current time
        current_time = datetime.datetime.now().strftime("%H:%M:%S")
        
        # 2. Determine the Protocol Type and Content
        protocol_type = "Other"
        content = "No Data"
        
        if TCP in packet:
            protocol_type = "TCP"
            if Raw in packet:
                # Convert payload to string, ignore errors, and show first 40 bytes
                content = repr(packet[Raw].load[:40]) 
        elif UDP in packet:
            protocol_type = "UDP"
            if Raw in packet:
                content = repr(packet[Raw].load[:40])
                
        # 3. Print the required information
        print(f"[{current_time}] --- New Packet Captured ---")
        print(f"  [+] Type:        {protocol_type}")
        print(f"  [+] Size:        {size} bytes")
        print(f"  [+] Origin:      {src_ip}")
        print(f"  [+] Destination: {dst_ip}")
        print(f"  [+] Content:     {content}")
        print("-" * 45)

# =========================================================
# Main Execution
# =========================================================
print("==================================================")
print("     Network Packet Sniffer (Traffic Analysis)    ")
print("==================================================")
print("Listening for 15 packets... Please browse the internet or wait.")
print("(Press Ctrl+C to stop early)\n")

try:
    # Sniff 15 packets and then stop. store=False means don't save in memory.
    sniff(prn=process_packet, count=15, store=False)
    print("\nFinished capturing packets successfully.")
except Exception as e:
    print(f"\n[!] Error: {e}")
    print("Make sure you run VS Code as Administrator to allow packet capturing.")