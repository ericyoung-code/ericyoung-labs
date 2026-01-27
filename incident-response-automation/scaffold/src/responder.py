import datetime

def run_response(ip_address, reason):
    """
    Simulates an automated response action, such as blocking an IP address
    on a firewall.
    """
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    action = f"BLOCK {ip_address}"
    log_entry = f"[{timestamp}] ACTION: {action} | REASON: {reason}\n"
    
    print(f"[*] Initiating automated response for {ip_address}...")
    print(f"[*] Reason: {reason}")
    
    # Simulate adding a rule to a firewall configuration file
    firewall_file = "firewall_rules.txt"
    try:
        with open(firewall_file, "a") as f:
            f.write(log_entry)
        print(f"[+] Successfully added blocking rule to {firewall_file}")
        print(f"[+] Action logged: {log_entry.strip()}")
    except Exception as e:
        print(f"[-] Failed to update firewall rules: {e}")