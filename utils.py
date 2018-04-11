from imports import *

def image_detection(url):
    new_url = 'http://' + url + '/image_detection'
    return new_url

def image_recognition(url):
    new_url = 'http://' + url + '/image_recognition'
    return new_url
        
def send_image(new_url):
    while True:
        # Capture Image from a RPi camera
        subprocess.run(["raspistill", "-o", "data/image.jpg"])

        # Code for capturing image
        captured_image = open('data/salman.jpg', 'rb')

        files = {'file': captured_image}
        r = requests.post(new_url, files=files)
        logging.debug(r.text)

        sleep(5)