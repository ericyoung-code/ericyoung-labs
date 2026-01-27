import argparse
import sys
import os

# Ensure the parent directory is in the path to import src
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from src.simulator import run_sim

def main():
    parser = argparse.ArgumentParser(description="ICS Sensor Traffic Simulator")
    parser.add_argument('--duration', type=int, default=10, help='Duration in seconds')
    parser.add_argument('--output', type=str, default='traffic.log', help='Output file')
    
    args = parser.parse_args()
    
    run_sim(args.duration, args.output)

if __name__ == '__main__':
    main()