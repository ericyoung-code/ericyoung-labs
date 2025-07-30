with open('sample.log', 'r') as f:
    for line in f:
        print('Parsed:', line.strip())