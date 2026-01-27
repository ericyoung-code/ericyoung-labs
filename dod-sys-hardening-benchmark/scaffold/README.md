# System Hardening Compliance Auditor

This tool simulates a security compliance audit, checking system configurations against a defined benchmark (e.g., DISA STIG or CIS).

## Features
- **Simulated Checks**: Verifies simulated system states like "SSH Root Login" or "Password Complexity".
- **Reporting**: Generates a detailed JSON report with pass/fail status for each check.

## Usage

You can run this tool using the unified `lab_runner.py` in the root directory:

```bash
# Run audit with 'standard' profile
python lab_runner.py compliance-audit --profile standard
```

## Output
- **Console**: Summary of Passed/Failed checks.
- **File (`compliance_report.json`)**: Detailed breakdown of every check performed.