import django
import os
import sys
sys.path.append('G:/cyber knights/cybersecurity-tool/pi_armor/') 
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'pi_armor.settings')
django.setup()
from monitor.models import Alert
from scapy.all import sniff, ICMP, IP, TCP, UDP
from collections import Counter
from collections import defaultdict



def handle_packet(packet):
    if ICMP in packet:
        print("ICMP (ping) packet detected: ", packet.summary()) 
        # Here you could add logic to log this packet and/or send an alert


sniff(prn=handle_packet)

packet_counts = Counter()

def detect_ddos(packet):
    if IP in packet:
        src_ip = packet[IP].src
        packet_counts[src_ip] += 1

        # A simplistic DDoS detection algorithm
        if packet_counts[src_ip] > 100:  # Threshold value
            print(f"Potential DDoS attack detected from {src_ip}")
            log_attack("DDoS", src_ip, "High volume of packets")
                   
sniff(prn=detect_ddos)

port_scan_activity = defaultdict(set)

def detect_port_scan(packet):
    if IP in packet and (TCP in packet or UDP in packet):
        src_ip = packet[IP].src
        dst_port = packet[TCP].dport if TCP in packet else packet[UDP].dport
        
        port_scan_activity[src_ip].add(dst_port)

        # Check for port scanning (simplistic)
        if len(port_scan_activity[src_ip]) > 20:  # Threshold value
            print(f"Potential port scanning detected from {src_ip}")

sniff(prn=detect_port_scan)

def log_attack(attack_type, src_ip, details):
    Alert.objects.create(
        attack_type=attack_type,
        attacker_ip=src_ip,
        details=details
    )

