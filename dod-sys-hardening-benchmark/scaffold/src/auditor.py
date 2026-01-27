import json
import random
import datetime

def run_audit(profile):
    """
    Simulates a system compliance audit based on a benchmark profile.
    """
    print(f"[*] Starting Compliance Audit using profile: {profile}")
    print("[*] Scanning system configurations...")
    
    # Define some dummy checks based on DISA STIG / CIS Benchmarks
    checks = [
        {"id": "V-3001", "description": "SSH Root Login disabled", "status": "PASS"},
        {"id": "V-3002", "description": "Password Minimum Length >= 14", "status": "FAIL"},
        {"id": "V-3003", "description": "Software Updates Auto-Check Enabled", "status": "PASS"},
        {"id": "V-3004", "description": "Firewall Enabled", "status": "PASS"},
        {"id": "V-3005", "description": "Audit Logs Persist Across Reboot", "status": "FAIL"},
        {"id": "V-3006", "description": "Unused Network Protocols Disabled", "status": "PASS"},
    ]
    
    # Introduce some randomness if 'random' profile is selected, else static
    if profile == 'random':
        for check in checks:
            check["status"] = random.choice(["PASS", "FAIL"])
    
    report = {
        "timestamp": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "profile": profile,
        "total_checks": len(checks),
        "passed": sum(1 for c in checks if c["status"] == "PASS"),
        "failed": sum(1 for c in checks if c["status"] == "FAIL"),
        "details": checks
    }
    
    # Write report
    report_file = "compliance_report.json"
    with open(report_file, "w") as f:
        json.dump(report, f, indent=4)
        
    print(f"[+] Audit Complete. Report built: {report_file}")
    print(f"    Passed: {report['passed']} | Failed: {report['failed']}")
