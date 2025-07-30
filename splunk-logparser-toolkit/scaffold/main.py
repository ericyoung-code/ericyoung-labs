# Entry point for log parser
from src.parser import parse_logs

if __name__ == '__main__':
    parse_logs('logs/sample.log')