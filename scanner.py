
import socket

import sys

from datetime import datetime



def check_port(ip, port):

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    s.settimeout(2)  

    try:

        result = s.connect_ex((ip, port))

        if result == 0:

            print(f"[+] SUCCESS: {ip}:{port} is OPEN")

        else:

            print(f"[-] CLOSED: {ip}:{port} is closed")

    except Exception as e:

        print(f"[!] ERROR: {e}")

    finally:

        s.close()



if __name__ == "__main__":

    target_ip = "8.8.8.8"

    target_port = 53

    print(f"[*] Starting scan on {target_ip}:{target_port} at {datetime.now()}")

    check_port(target_ip, target_port)

