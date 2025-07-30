with open('alerts.log', 'r') as f:
    for line in f:
        if 'ALERT' in line:
            print('[ACTION] Auto-response triggered')