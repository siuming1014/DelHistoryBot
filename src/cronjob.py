import requests
import time


while True:
    for i in range(60):
        print(i)
        time.sleep(1)
    try:
        r = requests.get('http://localhost:5000/process_queue')
        print(r.status_code)
        print(r.content)
    except Exception as e:
        print(e)
