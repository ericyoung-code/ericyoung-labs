# N-ETHER: Network Enumeration Tool

N-ETHER is a concurrent network scanner designed for speed and flexibility. It acts as a robust wrapper around Nmap, allowing for parallel scanning of multiple targets.

## Features
- **Concurrent Scanning**: Scans multiple targets simultaneously using threads.
- **Modes**:
    - **Quick Scan (`-q`)**: Scans top 100 ports.
    - **Full Scan**: Scans all ports (default).
- **Target Flexibility**: Accepts a single IP or a file containing a list of targets.
- **Reporting**: Consolidates results into a single summary file.

## Usage

Run it via the unified lab runner:

```bash
# Scan a single target (Quick Mode)
python lab_runner.py n-ether --target 192.168.1.1 --quick

# Scan a list of targets from a file
python lab_runner.py n-ether --target targets.txt --output my_scan_report.txt
```

## Prerequisites
- **Nmap**: This tool requires `nmap` to be installed and available in your system's PATH.
