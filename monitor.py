import time
import requests
import logging

logging.basicConfig(filename="monitor.log", level=logging.ERROR)
URL = "http://localhost:8000"

def cloudwatch_alert():
    print("AWS CloudWatch Alert: Service Down!")

while True:
    try:
        r = requests.get(URL, timeout=5)
        if r.status_code >= 500:
            logging.error("500 error detected")
            cloudwatch_alert()
    except Exception as e:
        logging.error(f"Service unreachable: {e}")
        cloudwatch_alert()

    time.sleep(30)
