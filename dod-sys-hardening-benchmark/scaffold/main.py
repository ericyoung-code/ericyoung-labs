import argparse
import sys
import os

# Ensure the parent directory is in the path to import src
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from src.auditor import run_audit

def main():
    parser = argparse.ArgumentParser(description="System Hardening Compliance Auditor")
    parser.add_argument('--profile', type=str, default='standard', help='Audit profile (e.g., standard, strict)')
    
    args = parser.parse_args()
    
    run_audit(args.profile)

if __name__ == '__main__':
    main()
