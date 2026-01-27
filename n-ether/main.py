import argparse
import sys
import os

# Ensure the parent directory is in the path to import src
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from src.scanner import run_network_scan

def main():
    parser = argparse.ArgumentParser(description="N-ETHER: Network Enumeration Tool (Python)")
    parser.add_argument('-t', '--target', required=True, help='Target IP or File Path')
    parser.add_argument('-q', '--quick', action='store_true', help='Quick scan (top 100 ports)')
    parser.add_argument('-o', '--output', default='scan_summary.txt', help='Output summary file')
    
    args = parser.parse_args()
    
    run_network_scan(args.target, args.quick, args.output)

if __name__ == '__main__':
    main()
