# Entry point for incident response automation
from src.responder import monitor_logs

if __name__ == '__main__':
    monitor_logs('logs/alerts.log')