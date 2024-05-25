import requests
import threading
import random

messages = []
with open("messages.txt", 'r') as f:
    Content = f.read()
    messages = Content.split('\n')
    f.close()

teleApis = []
with open("ScammerApisToSpam.txt") as f:
    ApiFileContent = f.read()
    teleApis = ApiFileContent.split("\n")
    f.close()


def SendMessage():
    while 1:
        for i in range(len(teleApis)):
            response = requests.get(f"{teleApis[i]}{random.choice(messages)}")
            if response.status_code == 200:
                print(f"API {i+1}: Message sent! : {response.json()['result']['text']}")
            else:
                print(f"API {i+1}: ERROR: {response.json()['description']}")


threads = []
amount_of_threads = 50

for i in range(amount_of_threads):
    t = threading.Thread(target=SendMessage)
    t.daemon = True
    threads.append(t)

for i in range(amount_of_threads):
    threads[i].start()

for i in range(amount_of_threads):
    threads[i].join()
