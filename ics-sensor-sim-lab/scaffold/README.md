# ICS Sensor Traffic Simulator

This tool simulates network traffic typical of an Industrial Control System (ICS) environment. It generates synthetic Modbus/TCP packets to help test monitoring and intrusion detection systems.

## Features
- Generates random internal IP addresses (192.168.1.x).
- Simulates common Modbus function codes (Read Coils, Write Registers, etc.).
- Outputs data to a CSV log file.

## Quick Start
To use this tool, run the simulator:

```bash
# Run for 30 seconds and save to traffic.log
python lab_runner.py ics-sim --duration 30 --output traffic.log
```

## Output Format
The generated CSV file contains the following columns:
- `timestamp`: Time of the event.
- `source_ip`: IP sending the request.
- `dest_ip`: Destination PLC IP (fixed at 192.168.1.100).
- `protocol`: Protocol used (MODBUS/TCP).
- `function_code`: Modbus function code used.
- `register_address`: Target register.
- `value`: Value read/written.