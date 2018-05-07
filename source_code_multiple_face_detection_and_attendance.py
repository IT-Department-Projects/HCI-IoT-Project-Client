import cv2
import os
import numpy as np
import sys
import pickle
import csv

###Image Cropping Library
from PIL import Image,ImageFile
ImageFile.MAXBLOCK = 2**20
import face_recognition
import time;
from os import listdir


subjects = ["", "15IT135", "15IT136","15IT250"]

def detect_face(img):
	gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
	face_cascade = cv2.CascadeClassifier('opencv-files/lbpcascade_frontalface.xml')
	faces = face_cascade.detectMultiScale(gray, scaleFactor=1.2, minNeighbors=5);
	if (len(faces) == 0):
		return None, None
	(x, y, w, h) = faces[0]
	return gray[y:y+w, x:x+h], faces[0]


def prepare_training_data(data_folder_path):
	dirs = os.listdir(data_folder_path)
	faces = []
	labels = []
	for dir_name in dirs:
		if not dir_name.startswith("s"):
			continue;
		label = int(dir_name.replace("s", ""))
		subject_dir_path = data_folder_path + "/" + dir_name
		subject_images_names = os.listdir(subject_dir_path)
		for image_name in subject_images_names:
			if image_name.startswith("."):
				continue;
			image_path = subject_dir_path + "/" + image_name
			image = cv2.imread(image_path)
			cv2.imshow("Training on image...", cv2.resize(image, (400, 500)))
			cv2.waitKey(100)
			face, rect = detect_face(image)
			if face is not None:
				faces.append(face)
				labels.append(label)
			
	cv2.destroyAllWindows()
	cv2.waitKey(1)
	cv2.destroyAllWindows()
	
	return faces, labels

"""
faces, labels = prepare_training_data("training-data")
with open("faces.pickle",'wb') as file:
	pickle.dump(faces,file)
with open("labels.pickle",'wb') as file:
	pickle.dump(labels,file)
"""
pickle_out_faces=open('faces.pickle','rb')
pickle_out_labels=open('labels.pickle','rb')
faces=pickle.load(pickle_out_faces)
labels=pickle.load(pickle_out_labels)
face_recognizer = cv2.face.LBPHFaceRecognizer_create()
face_recognizer.train(faces, np.array(labels))


def image_cropping(test_image):
	image = face_recognition.load_image_file(test_image)

	# Find all the faces in the image using a pre-trained convolutional neural network.
	# This method is more accurate than the default HOG model, but it's slower
	# unless you have an nvidia GPU and dlib compiled with CUDA extensions. But if you do,
	# this will use GPU acceleration and perform well.
	# See also: find_faces_in_picture.py
	face_locations = face_recognition.face_locations(image, number_of_times_to_upsample=0, model="cnn")

	print("I found {} face(s) in this photograph.".format(len(face_locations)))

	for face_location in face_locations:

	    # Print the location of each face in this image
	    top, right, bottom, left = face_location
	    print("A face is located at pixel location Top: {}, Left: {}, Bottom: {}, Right: {}".format(top, left, bottom, right))
	    top=top-100
	    bottom=bottom+100
	    left=left-100
	    right=right+100
	    # You can access the actual face itself like this:
	    face_image = image[top:bottom, left:right]
	    pil_image = Image.fromarray(face_image)
	    ts = time.time()
	    pil_image.save("test-data/"+str(ts)+".jpg", "JPEG", quality=100, optimize=True, progressive=True)
	    img = Image.open("test-data/"+str(ts)+".jpg")
	    #img2 = img.rotate(270)
	    #img2.save("test-data/"+str(ts)+".jpg")



def predict(test_img):
	img = test_img.copy()
	face, rect = detect_face(img)
	label, confidence = face_recognizer.predict(face)
	label_text = subjects[label]
	
	return label_text

def sample_detection():
	#for file in listdir("/Users/aimanabdullahanees/Desktop/HCI_Project/test-data"):
	#	if not file.startswith('.'):
		a=cv2.imread("test-data/1525412260.254556.jpg")
		name=predict(a)
		print(name)


def takeAttendance():
	#load test images
	test_img1 = cv2.imread("test-data/"+sys.argv[1])

	#perform a prediction
	predicted_student = predict(test_img1)
	print(predicted_student)
	csv_reader = csv.reader(open('StudentDetails.csv', 'r'))
	content_as_list = list(csv_reader)
	#print(content_as_list)
	#print(type(csv_reader))
	#load_student_attendance = pd.read_csv('StudentDetails.csv')
	
	
	temp_id = predicted_student[4:]
	int_id = int(temp_id)
	if int_id <= 153:
		int_id = int(temp_id) - 101
	else:
		int_id = int(temp_id)-201+53
	#print(content_as_list[int_id])
	check = int(content_as_list[int_id][2])
	
	if check == 0:
		content_as_list[int_id][2] = str(1)
	
	#print(content_as_list)

	csv_writer = csv.writer(open('StudentDetails.csv', 'w', newline=''))
	csv_writer.writerows(content_as_list)
	

takeAttendance()
test_image=sys.argv[1]
image_cropping(test_image)
sample_detection()
