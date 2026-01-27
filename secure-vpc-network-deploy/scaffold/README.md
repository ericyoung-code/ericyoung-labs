# Secure VPC Network Generator

This tool provides a calculator and generator for AWS VPC Terraform configurations. It allows you to quickly scaffold a secure VPC with multiple subnets.

## Features
- **Dynamic CIDR Calculation**: Input a generic CIDR (e.g., `10.0.0.0/16`) and get valid subnet logic.
- **Terraform Output**: Generates a ready-to-deploy `main.tf` file.

## Quick Start
To use this tool, run the generator:

```bash
# Generate a VPC with 3 subnets
python lab_runner.py vpc-gen --cidr 10.10.0.0/16 --subnets 3 --output my_vpc.tf
```

## Output
- **File (`generated_vpc.tf`)**: A Terraform configuration file containing the `aws_vpc` resource and `aws_subnet` resources.