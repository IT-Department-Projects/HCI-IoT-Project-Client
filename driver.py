from imports import *
from utils import *

'''
Add arguments to check whether face in image
has to be recognised or detected
'''
parser = argparse.ArgumentParser()
parser.add_argument("url", help="Give the URL of the server")
parser.add_argument("--detection", help="Detect Faces in the image")
parser.add_argument("--recognition", help="Recognize Faces in the image")

'''
Logger instance to add all logger related information
'''
logger = logging.getLogger('attendance')
hdlr = logging.FileHandler('/var/tmp/attendance.log')
formatter = logging.Formatter('%(asctime)s %(levelname)s %(message)s')
hdlr.setFormatter(formatter)
logger.addHandler(hdlr)
logger.setLevel(logging.INFO)

'''
Parsing arguments to define IP Address
'''
args = parser.parse_args()
logging.info("IP Address: " + str(args.url))
url = args.url + ':5000'

'''
Check whether argument is for image detection or 
for image recognition
'''
if args.detection:
    new_url = image_detection(url)
elif args.recognition:
    new_url = image_recognition(url)

'''
Send the image to a particular URL
'''
send_image(new_url)