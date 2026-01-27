import time
import random
import csv
import sys

def generate_ip():
    """Generates a random internal IP address."""
    return f"192.168.1.{random.randint(2, 254)}"

def run_sim(duration, output_file):
    print(f"[*] Starting simulation for {duration} seconds...")
    print(f"[*] Logging to {output_file}")
    
    start_time = time.time()
    
    # Define some Modbus function codes and typical registers
    function_codes = [1, 2, 3, 4, 5, 6, 15, 16]
    
    with open(output_file, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['timestamp', 'source_ip', 'dest_ip', 'protocol', 'function_code', 'register_address', 'value'])
        
        try:
            while time.time() - start_time < duration:
                # Simulate a packet
                timestamp = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
                src = generate_ip()
                dst = "192.168.1.100" # PLC Address
                proto = "MODBUS/TCP"
                func = random.choice(function_codes)
                reg = random.randint(1000, 2000)
                val = random.randint(0, 65535)
                
                writer.writerow([timestamp, src, dst, proto, func, reg, val])
                f.flush()
                
                # Sleep a tiny bit to not flood effectively infinite speed
                time.sleep(random.uniform(0.01, 0.5))
                
        except KeyboardInterrupt:
            print("[!] Interrupted.")
    
    print(f"[+] Simulation finished. Data written to {output_file}")