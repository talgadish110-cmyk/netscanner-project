import socket
import sys
import json
import argparse
import threading
from datetime import datetime

parser = argparse.ArgumentParser(description="Multi-Target Network Port Scanner with Threading")
parser.add_argument("-t", "--targets", default="targets.txt", help="Path to the targets file")
parser.add_argument("-p", "--ports", nargs="+", type=int, default=[21, 22, 80, 443, 8080], help="List of ports to scan")
args = parser.parse_args()

targets_file = args.targets
ports_to_scan = args.ports

scan_results = {
    "timestamp": str(datetime.now()),
    "scans": []
}


print("-" * 50)
print("Starting Multi-Target Threaded Network Scanner...")
print(f"Target file: {targets_file}")
print(f"Ports to scan: {ports_to_scan}")
print(f"Time started: {scan_results['timestamp']}")
print("-" * 50)

def scan_port(target_host, port, target_data):
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(1.0)
        result = s.connect_ex((target_host, port))
        if result == 0:
            status = "OPEN"
        else:
            status = "CLOSED"
        target_data["ports"][port] = status
        print(f"  Port {port}: {status}")
        s.close()
    except socket.error:
        target_data["ports"][port] = "ERROR"
try:
    with open(targets_file, "r") as f:
        targets = [line.strip() for line in f if line.strip()]
except FileNotFoundError:
    print(f"[-] Error: The file {targets_file} was not found.")
    sys.exit(1)

for target_host in targets:
    print(f"\nScanning target: {target_host}")
    target_data = {
        "target": target_host,
        "ports": {}
    }
    
    threads = []
    for port in ports_to_scan:
        t = threading.Thread(target=scan_port, args=(target_host, port, target_data))
        threads.append(t)
        t.start()
        
    for t in threads:
        t.join()
        
    scan_results["scans"].append(target_data)

try:
    with open("results.json", "w") as json_file:
        json.dump(scan_results, json_file, indent=4)
    print("\n[+] All results successfully saved to results.json")
except KeyboardInterrupt:
    print("\nExiting script.")
    sys.exit()
