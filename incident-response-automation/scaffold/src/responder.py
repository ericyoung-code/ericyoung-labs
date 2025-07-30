def monitor_logs(file_path):
    with open(file_path, 'r') as f:
        for line in f:
            if 'ALERT' in line:
                print(f'[ACTION] Responding to alert: {line.strip()}')