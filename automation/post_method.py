#!/usr/bin/python3


import requests
import time
from datetime import datetime
from random import randint

def init_requests():

    sess = requests.session()

    payload = {
        "date_reading":"2021-12-18T04:38:07.333Z",
        "temperature": 65,
        "humidity": 61,
        "dioxide": 503,
        "radiation": 1.1
    }
    # print(payload)

    # payload ={
    #     "ID": 0, "CreatedAt": "2021-11-28T23:38:07.333-05:00", "UpdatedAt": "2021-11-28T23:38:07.333-05:00", "DeletedAt": None,
    #     "date_reading": "0001-01-01T00:00:00Z", "temperature": 25, "humidity": 76, "dioxide": 600, "radiation": 1.1
    # }

    response = sess.post(
        url="http://127.0.0.1:8000/realtime/post-reading", json=payload)

    # time.sleep(5)
    # print(response)


def main():

    # for x in range(100):
    init_requests()



if __name__ == "__main__":
    main()
