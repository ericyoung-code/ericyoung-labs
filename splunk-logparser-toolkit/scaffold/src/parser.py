def parse_logs(file_path):
    with open(file_path, 'r') as f:
        for line in f:
            print(f'Parsed line: {line.strip()}')