import psutil
import logging
from datetime import datetime

# Configure logging
logging.basicConfig(filename='system_health.log', level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s')

# Define thresholds
CPU_THRESHOLD = 80.0  # in percentage
MEMORY_THRESHOLD = 80.0  # in percentage
DISK_THRESHOLD = 80.0  # in percentage

def check_cpu_usage():
    usage = psutil.cpu_percent(interval=1)
    if usage > CPU_THRESHOLD:
        logging.warning(f'High CPU usage detected: {usage}%')

def check_memory_usage():
    memory = psutil.virtual_memory()
    if memory.percent > MEMORY_THRESHOLD:
        logging.warning(f'High memory usage detected: {memory.percent}%')

def check_disk_usage():
    disk = psutil.disk_usage('/')
    if disk.percent > DISK_THRESHOLD:
        logging.warning(f'Low disk space detected: {disk.percent}% free')

def check_running_processes():
    process_count = len(psutil.pids())
    logging.info(f'Number of running processes: {process_count}')

def monitor_system():
    check_cpu_usage()
    check_memory_usage()
    check_disk_usage()
    check_running_processes()

if __name__ == '__main__':
    while True:
        monitor_system()
        # Wait for a minute before checking again
        time.sleep(60)
