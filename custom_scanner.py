import socket
import sys

def scan_and_log(target_ip, ports, output_file="scan_results.txt"):
    print(f"[*] Starting Custom Recon on: {target_ip}")
    
    # Open file in write mode ('w')
    with open(output_file, "w") as f:
        f.write(f"--- Recon Report for {target_ip} ---\n\n")
        
        for port in ports:
            try:
                # Create a TCP socket
                s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                s.settimeout(1.5)
                
                result = s.connect_ex((target_ip, port))
                
                if result == 0:
                    status_line = f"[+] Port {port} is OPEN"
                    print(status_line)
                    f.write(status_line + "\n")
                    
                    # Attempt Banner Grabbing
                    try:
                        s.send(b"HEAD / HTTP/1.1\r\nHost: " + target_ip.encode() + b"\r\n\r\n")
                        banner = s.recv(1024).decode(errors="ignore").strip()
                        if banner:
                            banner_line = f"    [->] Banner: {banner}"
                            print(banner_line)
                            f.write(banner_line + "\n")
                    except:
                        pass
                else:
                    status_line = f"[-] Port {port} is CLOSED or FILTERED"
                    f.write(status_line + "\n")
                    
                s.close()
            except Exception as e:
                error_line = f"[-] Error scanning port {port}: {e}"
                print(error_line)
                f.write(error_line + "\n")
                
    print(f"\n[✓] Scan finished! Results saved to {output_file}")

if __name__ == "__main__":
    target = "192.168.1.100"
    target_ports = [21, 22, 80, 443, 8080]
    scan_and_log(target, target_ports)
