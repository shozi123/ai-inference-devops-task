# monitor.py
import requests
import time

while True:
    try:
        r = requests.get("http://localhost:8000")
        print("Service OK:", r.status_code)
    except:
        print("ALERT: Service DOWN!")

    time.sleep(30)
