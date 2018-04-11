from imports import *

MAX_IMAGE_SIZE = 100000

'''
Method to compress an image
'''
def compress_image(file_name, height):
    with Image.open(file_name) as img:
        width, height = img.size
        logging.info("Initial dimensions of the image:" +
                     str(width) + " " + str(height))

        if height > 200:
            new_width = ((int)((width * 1.0 / height) * 200))
            print(width / height)
            img = img.resize((new_width, 200), Image.ANTIALIAS)

        width, height = img.size
        print("Initial dimensions of the image:" +
              str(width) + " " + str(height))

        img.save(file_name, optimize=True, quality=75)

'''
Method to detect faces in an image
Returns URL for REST API for detecting faces in images
'''
def image_detection(url):
    new_url = 'http://' + url + '/image_detection'
    return new_url


'''
Method to recognise faces in an image
Returns URL for REST API for recognising faces in images
'''
def image_recognition(url):
    new_url = 'http://' + url + '/image_recognition'
    return new_url
        

'''
Method to send POST request to server
'''
def send_image(new_url):
    while True:
        # Capture Image from a RPi camera
        # subprocess.run(["raspistill", "-o", "data/image.jpg"])

        if getsize('data/image.jpg') > MAX_IMAGE_SIZE:
            compress_image('data/image.jpg', 250)

        # Code for capturing image
        captured_image = open('data/image.jpg', 'rb')

        files = {'file': captured_image}
        r = requests.post(new_url, files=files)
        logging.debug(r.text)

        sleep(5)