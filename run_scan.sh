#!/bin/bash



mkdir -p scan_results



if [ ! -f "targets.txt" ]; then

    echo "[-] Error: targets.txt not found!"

    exit 1

fi



while IFS= read -r domain; do

    [ -z "$domain" ] && continue



    timestamp=$(date +"%Y%m%d_%H%M%S")

    output_file="scan_results/${domain}_${timestamp}.txt"



    echo "[*] Starting automated scan for target: $domain on Ubuntu"

    python3 scanner.py -d "$domain" -w subdomains.txt -o "$output_file" -t 20

    echo "[+] Finished scan for $domain. Saved to $output_file"

    echo "--------------------------------------------------"

done < targets.txt
