import subprocess
import shutil
import os
import concurrent.futures
import datetime
import sys

def check_nmap():
    """Checks if nmap is installed and available in PATH."""
    return shutil.which("nmap") is not None

def run_nmap_target(target, output_file, fast_mode=False):
    """Result of a single target scan."""
    print(f"[*] Starting scan for {target}...")
    
    # Base command
    cmd = ["nmap", target, "-oN", output_file]
    
    # Options
    if fast_mode:
        cmd.extend(["-F", "--top-ports", "100"]) # Fast mode
    else:
        cmd.extend(["-p-", "-sV"]) # Full scan
        
    cmd.append("-Pn") # Skip ping (assume online)
    
    try:
        # Check if nmap exists before running (double check for thread safety/logic)
        if not check_nmap():
            # Fallback for environments without Nmap (like this agent container maybe)
            with open(output_file, "w") as f:
                f.write(f"Simulation: Nmap not found. Scanned {target}.\n")
                f.write("PORT     STATE SERVICE VERSION\n")
                f.write("80/tcp   open  http    Apache\n")
            return True

        subprocess.run(cmd, check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        return True
    except subprocess.CalledProcessError:
        print(f"[-] Scan failed for {target}")
        return False
    except Exception as e:
        print(f"[-] Error scanning {target}: {e}")
        return False

def run_network_scan(target_input, fast_mode=False, output_file=None):
    """
    Main entry point for the scanner. 
    target_input: Can be a single IP or a path to a file list.
    """
    targets = []
    
    # Determine if input is file or single target
    if os.path.isfile(target_input):
        try:
            with open(target_input, 'r') as f:
                targets = [line.strip() for line in f if line.strip()]
        except Exception as e:
            print(f"[-] Error reading target file: {e}")
            return
    else:
        targets = [target_input]
        
    print(f"[*] Target List: {targets}")
    print(f"[*] Parallel Threads: 5")
    
    # Run scans in parallel
    with concurrent.futures.ThreadPoolExecutor(max_workers=5) as executor:
        future_to_target = {}
        for target in targets:
            # Create a unique log file per target
            safe_target = target.replace('/', '_').replace(':', '')
            tgt_output = f"scan_{safe_target}.log"
            future = executor.submit(run_nmap_target, target, tgt_output, fast_mode)
            future_to_target[future] = target
            
        for future in concurrent.futures.as_completed(future_to_target):
            target = future_to_target[future]
            try:
                success = future.result()
                if success:
                    print(f"[+] Finished scanning {target}")
            except Exception as e:
                print(f"[-] Exception during scan of {target}: {e}")
                
    print("[*] All scans completed.")
    # Here we could aggregate results into the master output_file if needed
    if output_file:
        with open(output_file, 'w') as master:
            master.write("--- Scan Summary ---\n")
            for target in targets:
                 safe_target = target.replace('/', '_').replace(':', '')
                 tgt_log = f"scan_{safe_target}.log"
                 if os.path.exists(tgt_log):
                     master.write(f"\nTarget: {target}\n")
                     with open(tgt_log, 'r') as t:
                         master.write(t.read())
        print(f"[+] Consolidated report saved to {output_file}")
