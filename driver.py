from imports import *
from utils import *

parser = argparse.ArgumentParser()
parser.add_argument("url", help="Give the URL of the server")
parser.add_argument("--detection", help="Detect Faces in the image")
parser.add_argument("--recognition", help="Recognize Faces in the image")

args = parser.parse_args()
logging.info("IP Address: " + str(args.url))
url = args.url + ':5000'

if args.detection:
    new_url = image_detection(url)
elif args.recognition:
    new_url = image_recognition(url)

send_image(new_url)