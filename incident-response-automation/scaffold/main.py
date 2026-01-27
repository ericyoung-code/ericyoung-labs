import argparse
import sys
import os

# Ensure the parent directory is in the path to import src
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from src.responder import run_response

def main():
    parser = argparse.ArgumentParser(description="Incident Response Automation Tool")
    parser.add_argument('--ip', type=str, required=True, help='IP address to block')
    parser.add_argument('--reason', type=str, default="Manual Block", help='Reason for blocking')
    
    args = parser.parse_args()
    
    run_response(args.ip, args.reason)

if __name__ == '__main__':
    main()