#!/bin/bash



LOG_DIR="secure_logs"

mkdir -p "$LOG_DIR"



TIMESTAMP=$(date +"%Y-%m-%d_%H-%M-%S")

LOG_FILE="$LOG_DIR/security_audit_$TIMESTAMP.log"



TARGET="target-server"

PORT_RANGE="1-80"



echo "[+] Starting Automated Security Pipeline at $TIMESTAMP" | tee -a "$LOG_FILE"



SCAN_OUTPUT=$(docker run --rm netscanner-project-security-scanner port_scanner.py -t "$TARGET" -p "$PORT_RANGE")

echo "$SCAN_OUTPUT" >> "$LOG_FILE"



if echo "$SCAN_OUTPUT" | grep -q "OPEN"; then

    echo "[!] ALERT: Open ports detected on target $TARGET!" | tee -a "$LOG_FILE"

    echo "[*] Action: Security alert logged securely in $LOG_FILE"

else

    echo "[-] Clean: No open ports found in the specified range." | tee -a "$LOG_FILE"

fi



echo "[+] Pipeline execution completed. Log saved to $LOG_FILE"


