import requests
from time import sleep
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("url", help="Give the URL of the server")
parser.add_argument("--detection", help="Detect Faces in the image")
parser.add_argument("--recognition", help="Recognize Faces in the image")

args = parser.parse_args()
print(args.url)
url = args.url+':5000'

if args.detection:
    while True:
        url = url + '/image_detection'
        # Code for capturing image
        captured_image = open('data/salman.jpg', 'rb')

        files = {'file': captured_image}
        r = requests.post(url, files=files)
        print(r.text)

        sleep(5)

if args.recognition:
    while True:
        url = url+'/image_recognition'
        # Code for capturing image
        captured_image = open('data/salman.jpg', 'rb')

        files = {'file': captured_image}
        r = requests.post(url, files=files)
        print(r.text)

        sleep(5)