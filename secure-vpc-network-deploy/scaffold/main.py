import argparse
import sys
import os

# Ensure the parent directory is in the path to import src
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from src.generator import generate_vpc_tf

def main():
    parser = argparse.ArgumentParser(description="Secure VPC Terraform Generator")
    parser.add_argument('--cidr', type=str, default='10.0.0.0/16', help='VPC CIDR Block')
    parser.add_argument('--subnets', type=int, default=2, help='Number of subnets to generate')
    parser.add_argument('--output', type=str, default='generated_vpc.tf', help='Output .tf file path')
    
    args = parser.parse_args()
    
    generate_vpc_tf(args.cidr, args.subnets, args.output)

if __name__ == '__main__':
    main()
