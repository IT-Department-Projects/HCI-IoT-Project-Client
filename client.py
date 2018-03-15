import requests
from time import sleep

url = 'http://10.100.120.48/image_recognition'

while True:
    # Code for capturing image

    captured_image = open('data/salman.jpg', 'rb')

    files = {'image': captured_image}
    r = requests.post(url, files=files)
    print(r.text)

    sleep(5)
