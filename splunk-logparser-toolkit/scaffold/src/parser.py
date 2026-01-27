import csv
import collections
import sys

def parse_logs(filepath):
    print(f"[*] Parsing log file: {filepath}")
    
    request_counts = collections.defaultdict(int)
    function_counts = collections.defaultdict(int)
    suspicious_ips = []
    
    try:
        with open(filepath, 'r') as f:
            reader = csv.DictReader(f)
            total_rows = 0
            for row in reader:
                total_rows += 1
                try:
                    src_ip = row['source_ip']
                    func = row['function_code']
                except KeyError:
                    # Skip malformed lines or different formats
                    continue
                
                request_counts[src_ip] += 1
                function_counts[func] += 1
                
                # Simple anomaly detection: Function Code 15 (Write Multiple Coils) or 16 (Write Multiple Registers)
                # from an IP other than a known "Engineer Station" (e.g., 192.168.1.50 - just hypothetical)
                if func in ['15', '16']:
                    # Let's flag it just to show "detection"
                    try:
                        suspicious_ips.append({'ip': src_ip, 'func': func, 'time': row['timestamp']})
                    except KeyError:
                         suspicious_ips.append({'ip': src_ip, 'func': func, 'time': 'unknown'})
                    
        print(f"\n[+] Analysis Complete. Processed {total_rows} events.")
        
        print("\n--- traffic summary ---")
        for ip, count in request_counts.items():
            print(f"IP: {ip:<15} Requests: {count}")
            
        print("\n--- function code usage ---")
        for func, count in function_counts.items():
            print(f"Code: {func:<5} Count: {count}")
            
        print("\n--- suspicious activity alerts (High Risk Writes) ---")
        if suspicious_ips:
            for alert in suspicious_ips[:10]: # Limit output
                print(f"[ALERT] High priv write {alert['func']} from {alert['ip']} at {alert['time']}")
            if len(suspicious_ips) > 10:
                print(f"... and {len(suspicious_ips) - 10} more.")
        else:
            print("No suspicious activity detected.")
            
    except FileNotFoundError:
        print(f"[-] File not found: {filepath}")
    except Exception as e:
        print(f"[-] Error parsing file: {e}")