# source ~/.profile
# workon cv
# python3 pi_face_recognition.py --cascade haarcascade_frontalface_default.xml \
#	--encodings encodings.pickle
from imutils.video import VideoStream
from imutils.video import FPS
import face_recognition
import argparse
import imutils
import pickle
import os
import time
import cv2
from time import sleep
# construct the argument parser and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-c", "--cascade", required=True,
	help = "path to where the face cascade resides")
ap.add_argument("-e", "--encodings", required=True,
	help="path to serialized db of facial encodings")
args = vars(ap.parse_args())

os.system('sudo modprobe bcm2835-v4l2')

# load the known faces and embeddings along with OpenCV's Haar
# cascade for face detection
print("[INFO] loading encodings + face detector...")
data = pickle.loads(open(args["encodings"], "rb").read())
detector = cv2.CascadeClassifier(args["cascade"])

# initialize the video stream and allow the camera sensor to warm up
print("[INFO] starting video stream...")
vs = VideoStream(src=0).start()
#vs = VideoStream(usePiCamera=True).start()
time.sleep(2.0)

# start the FPS counter
fps = FPS().start()
#os.system('sudo python Or.py')
# loop over frames from the video file stream
flag = 1
count = 0
while True:
        
	#os.system('sudo python Or.py')
	# grab the frame from the threaded video stream and resize it
	# to 500px (to speedup processing)
	#pixel_ring.set_brightness(2)
	#pixel_ring.set_color(rgb=None, r=255, g=165, b=0)
	frame = vs.read()
	frame = imutils.resize(frame, width=500)
	os.system('sudo python All12_LEDs_Orange.py')
	if flag == 1:
            os.system('sudo python All12_LEDs_Orange.py')
            #print(count)
	# convert the input frame from (1) BGR to grayscale (for face
	# detection) and (2) from BGR to RGB (for face recognition)
	gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
	rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

	# detect faces in the grayscale frame
	rects = detector.detectMultiScale(gray, scaleFactor=1.1, 
		minNeighbors=5, minSize=(30, 30),
		flags=cv2.CASCADE_SCALE_IMAGE)

	# OpenCV returns bounding box coordinates in (x, y, w, h) order
	# but we need them in (top, right, bottom, left) order, so we
	# need to do a bit of reordering
	
	boxes = [(y, x + w, y + h, x) for (x, y, w, h) in rects]

	# compute the facial embeddings for each face bounding box
	encodings = face_recognition.face_encodings(rgb, boxes)
	names = []
	count = count + 1
	#os.system('sudo python All12_LEDs_Orange.py')
	print(count)
	if count == 50:
            flag = 1
            count = 0
	# loop over the facial embeddings
	for encoding in encodings:
		# attempt to match each face in the input image to our known
		# encodings
		matches = face_recognition.compare_faces(data["encodings"],
			encoding)
		name = "Unknown"
		#os.system('sudo python Re.py')
		# check to see if we have found a match
		if True in matches:
			# find the indexes of all matched faces then initialize a
			# dictionary to count the total number of times each face
			# was matched
			matchedIdxs = [i for (i, b) in enumerate(matches) if b]
			counts = {}
			os.system('pkill -f All12_LEDs_Orange.py')
			#print (names)
			#os.system('sudo python All12_LEDs_Green.py')
			#sleep(1)
			#os.system('pkill -f All12_LEDs_Green.py')
			os.system('sudo python All12_LEDs_Green.py')
			sleep(1)
			os.system('pkill -f All12_LEDs_Green.py')
			#os.system('./G_TTS.sh Hi "", Welcome back')
			flag = 2
			#os.system('sudo python off.py')

			# loop over the matched indexes and maintain a count for
			# each recognized face face
			for i in matchedIdxs:
				name = data["names"][i]
				counts[name] = counts.get(name, 0) + 1

			# determine the recognized face with the largest number
			# of votes (note: in the event of an unlikely tie Python
			# will select first entry in the dictionary)
			name = max(counts, key=counts.get)
		
		# update the list of names
		names.append(name)
		print (name)
		if(name != "Unknown"):
                    command = "./G_TTS.sh Hi " +name+ " Welcome back"
                    print (command)
                    os.system(command)
                    #os.system("deactivate")
                    #os.system("python3 /home/pi/alexa.py")
                    #os.system("sh wake_alexa.sh")
                    os.system("sh Sleep_Script.sh")                    
		#os.system('./G_TTS.sh Hi "name", Welcome back')

	# loop over the recognized faces
	for ((top, right, bottom, left), name) in zip(boxes, names):
		# draw the predicted face name on the image
		cv2.rectangle(frame, (left, top), (right, bottom),
			(0, 255, 0), 2)
		y = top - 15 if top - 15 > 15 else top + 15
		cv2.putText(frame, name, (left, y), cv2.FONT_HERSHEY_SIMPLEX,
			0.75, (0, 255, 0), 2)

	# display the image to our screen
	cv2.imshow("Frame", frame)
	key = cv2.waitKey(1) & 0xFF

	# if the `q` key was pressed, break from the loop
	if key == ord("q"):
		break

	# update the FPS counter
	fps.update()

# stop the timer and display FPS information
fps.stop()
print("[INFO] elasped time: {:.2f}".format(fps.elapsed()))
print("[INFO] approx. FPS: {:.2f}".format(fps.fps()))

# do a bit of cleanup
cv2.destroyAllWindows()
os.system('sudo python All12_LEDs_Off.py')
vs.stop()