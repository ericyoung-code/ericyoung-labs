# Incident Response Automation Tool

This tool simulates automated defensive actions, such as blocking an IP address on a firewall, in response to detected threats.

## Features
- **Automated Response**: Appends "BLOCK" rules to a simulated firewall configuration file (`firewall_rules.txt`).
- **Audit Logging**: Logs the time, action, and reason for every response.

## Usage

You can run this tool using the unified `lab_runner.py` in the root directory:

```bash
# Block an IP address
python lab_runner.py incident-response --ip 10.10.10.xxx --reason "Malicious Activity Detected"
```

## Output
- **Console**: Confirms the action taken.
- **File (`firewall_rules.txt`)**: Appends a line like:
  `[2024-10-27 12:00:00] ACTION: BLOCK 10.10.10.xxx | REASON: Malicious Activity Detected`