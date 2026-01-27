import argparse
import sys
import os
import subprocess

def run_ics_sim(args):
    """Runs the ICS Sensor Simulator."""
    print(f"[*] Starting ICS Sensor Simulator for {args.duration} seconds...")
    print(f"[*] Output will be saved to {args.output}")
    
    # Construct path to the lab's main.py
    lab_path = os.path.join(os.path.dirname(__file__), 'ics-sensor-sim-lab', 'scaffold', 'main.py')
    
    cmd = [sys.executable, lab_path, '--duration', str(args.duration), '--output', args.output]
    try:
        subprocess.run(cmd, check=True)
        print("[+] Simulation complete.")
    except subprocess.CalledProcessError as e:
        print(f"[-] Error running simulation: {e}")
    except KeyboardInterrupt:
        print("\n[!] Stopped by user.")

def run_log_parser(args):
    """Runs the Log Parser Toolkit."""
    print(f"[*] Starting Log Parser on file: {args.input}...")
    
    # Construct path to the lab's main.py
    lab_path = os.path.join(os.path.dirname(__file__), 'splunk-logparser-toolkit', 'scaffold', 'main.py')
    
    cmd = [sys.executable, lab_path, '--input', args.input]
    try:
        subprocess.run(cmd, check=True)
        print("[+] Parsing complete.")
    except subprocess.CalledProcessError as e:
        print(f"[-] Error running parser: {e}")

def run_incident_response(args):
    """Runs the Incident Response Automation Tool."""
    print(f"[*] Starting Incident Responder...")
    print(f"[*] Blocking IP: {args.ip}")
    
    # Construct path to the lab's main.py
    lab_path = os.path.join(os.path.dirname(__file__), 'incident-response-automation', 'scaffold', 'main.py')
    
    cmd = [sys.executable, lab_path, '--ip', args.ip, '--reason', args.reason]
    try:
        subprocess.run(cmd, check=True)
        print("[+] Response action complete.")
    except subprocess.CalledProcessError as e:
        print(f"[-] Error running responder: {e}")

def run_compliance_audit(args):
    """Runs the Compliance Auditor."""
    print(f"[*] Starting Compliance Audit (Profile: {args.profile})...")
    
    # Construct path to the lab's main.py
    lab_path = os.path.join(os.path.dirname(__file__), 'dod-sys-hardening-benchmark', 'scaffold', 'main.py')
    
    cmd = [sys.executable, lab_path, '--profile', args.profile]
    try:
        subprocess.run(cmd, check=True)
    except subprocess.CalledProcessError as e:
        print(f"[-] Error running auditor: {e}")

def run_vpc_generator(args):
    """Runs the VPC Generator."""
    print(f"[*] Starting VPC Generator...")
    
    # Construct path to the lab's main.py
    lab_path = os.path.join(os.path.dirname(__file__), 'secure-vpc-network-deploy', 'scaffold', 'main.py')
    
    cmd = [sys.executable, lab_path, '--cidr', args.cidr, '--subnets', str(args.subnets), '--output', args.output]
    try:
        subprocess.run(cmd, check=True)
    except subprocess.CalledProcessError as e:
        print(f"[-] Error running generator: {e}")

def main():
    parser = argparse.ArgumentParser(description="EricYoung Labs - Unified Tool Runner")
    subparsers = parser.add_subparsers(dest='tool', help='Available tools')

    # ICS Simulator Subcommand
    ics_parser = subparsers.add_parser('ics-sim', help='Run Industrial Control System Traffic Simulator')
    ics_parser.add_argument('--duration', type=int, default=30, help='Duration of simulation in seconds')
    ics_parser.add_argument('--output', type=str, default='ics_traffic.log', help='Output log file path')
    ics_parser.set_defaults(func=run_ics_sim)

    # Log Parser Subcommand
    log_parser = subparsers.add_parser('log-parser', help='Run Log Analysis Toolkit')
    log_parser.add_argument('--input', type=str, required=True, help='Input log file to analyze')
    log_parser.set_defaults(func=run_log_parser)

    # Incident Response Subcommand
    ir_parser = subparsers.add_parser('incident-response', help='Run Incident Response Automation')
    ir_parser.add_argument('--ip', type=str, required=True, help='IP address to block')
    ir_parser.add_argument('--reason', type=str, default="Manual Block", help='Reason for blocking')
    ir_parser.set_defaults(func=run_incident_response)
    
    # Compliance Auditor Subcommand
    audit_parser = subparsers.add_parser('compliance-audit', help='Run System Hardening Compliance Auditor')
    audit_parser.add_argument('--profile', type=str, default='standard', help='Audit profile to compare against')
    audit_parser.set_defaults(func=run_compliance_audit)

    # VPC Generator Subcommand
    vpc_parser = subparsers.add_parser('vpc-gen', help='Run Secure VPC Terraform Generator')
    vpc_parser.add_argument('--cidr', type=str, default='10.0.0.0/16', help='VPC CIDR Block')
    vpc_parser.add_argument('--subnets', type=int, default=2, help='Number of subnets')
    vpc_parser.add_argument('--output', type=str, default='generated_vpc.tf', help='Output file')
    vpc_parser.set_defaults(func=run_vpc_generator)

    args = parser.parse_args()



    if getattr(args, 'func', None):
        args.func(args)
    else:
        parser.print_help()

if __name__ == "__main__":
    main()
