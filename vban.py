import atexit
import socket
import os
import time

# Define the VBAN port
VBAN_PORT = 6980

# Create a socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Function to be called at exit
def cleanup():
    print(f"Cleaning up and releasing port {VBAN_PORT}")
    try:
        sock.close()
    except Exception as e:
        print(f"Error during cleanup: {e}")

# Register the cleanup function to be called at exit
atexit.register(cleanup)


from scapy.all import *

def process_packet(pkt):
    if pkt.haslayer(UDP) and pkt[UDP].dport == 6980:
        source_ip = pkt[IP].src
        print(f"Detected VBAN stream from {source_ip}")
        for _ in range(3):  # Try to connect 3 times
            os.system(f'/usr/local/bin/vban_receptor -i {source_ip} -p 6980 -s StereoPi -q 4')
            time.sleep(5)  # Wait for a few seconds between attempts

        # If unable to connect after 3 attempts, terminate the script
        print("Unable to connect. Terminating script.")
        os._exit(0)

# Check if the port is in use and terminate conflicting processes
def check_port_in_use(port):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        return s.connect_ex(('localhost', port)) == 0

if not check_port_in_use(VBAN_PORT):
    print(f"Port {VBAN_PORT} is already in use. Terminating conflicting process.")
    os.system(f'sudo kill $(sudo lsof -t -i:{VBAN_PORT})')

# Start sniffing for packets
sniff(filter="udp and port 6980", prn=process_packet)

