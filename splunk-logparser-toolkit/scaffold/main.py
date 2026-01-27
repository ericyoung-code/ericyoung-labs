import argparse
import sys
import os

# Ensure the parent directory is in the path to import src
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from src.parser import parse_logs

def main():
    parser = argparse.ArgumentParser(description="Splunk-style Log Parser")
    parser.add_argument('--input', type=str, required=True, help='Path to log file')
    
    args = parser.parse_args()
    
    parse_logs(args.input)

if __name__ == '__main__':
    main()