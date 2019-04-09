source ~/.profile
workon cv
python3 pi_face_recognition.py --cascade haarcascade_frontalface_default.xml \
	--encodings encodings.pickle
