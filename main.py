import requests
import time
import random

URL = "監視したいURL"

TARGET_TEXT = "現在販売中のチケット情報はありません。"

while True:

    try:

        r = requests.get(URL)

        html = r.text

        if TARGET_TEXT not in html:

            print("チケット販売の可能性")

        else:

            print("まだ販売なし")

    except Exception as e:

        print(e)

    wait = random.randint(30,60)

    time.sleep(wait)
