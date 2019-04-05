# Alexa-Smart-Speaker brief description 

    A modern Smart-speaker with an advanced microphone array, camera module interfaced with Pi capable of performing AI-based tasks  

    This Smart Speaker is capable of performing Facial Recognition used for Biometrics based Speaker System wakeup in addition to   calling out the Alexa wake-word.  
    It also performs other Computer Vision based applications such as implementation of a camera-based security system. The Microphone array used to capture user’s voice has inbuilt Digital Signal Processing based voice algorithms which enables better capturing and understanding of user’s speech resulting in a successful full-duplex human-machine speech interaction  


Biometrics based Alexa wakeup & interaction using ReSpeaker v2

    Far-field voice capture 

    AEC capabilities for higher wake-word detection accuracy

    Noise Suppression for better user interaction 

Special features of Smart-Speaker - Alexa, friday Custom Skill 

    USB RGB LED Controller

    Deep Learning & Open CV based object detection

    Audio Processing based Alarm Detector 

    Open CV based Security System

    Web-based MJPEG Streaming

ODAS and ReSpeaker v2

    Visualisation of noise and reverberation 

    Filtering by varying thresholds 

    Tracking & visualising multiple voice sources

#How to run the scripts sererately: 

#Face Recog Script
    cd /home/pi/FYP-SS/Combined_Scripts/Face_Recog_Wakeup_Alexa_C_SDK
    source ~/.profile
    workon cv
    python3 pi_face_recognition.py --cascade haarcascade_frontalface_default.xml \
	    --encodings encodings.pickle

#Alexa C++ SDK build 	
    sudo bash /home/pi/AlexaDeviceSDK/startsample.sh

# Fire Alarm Script	- working in this local env 
    cd /home/pi/FYP-SS/Combined_Scripts/Alexa_JSON_Combined_LED_Security_Alarm
    python3 email_Fire_Alarm_detection_using_mic_array.py

# Security System & email
    cd /home/pi/FYP-SS/Combined_Scripts/Alexa_JSON_Combined_LED_Security_Alarm
    source ~/.profile
    workon cv
    python if_human_body_recog_then_email.py

#Deep Learning & Open CV based object detection
    cd /home/pi/FYP-SS/Combined_Scripts/Alexa_JSON_Combined_LED_Security_Alarm
    source ~/.profile
    workon cv
    python dl_img_frm_cam.py

# M-JPEG Streamming
    sudo modprobe bcm2835-v4l2
    cd /home/pi/FYP-SS/Combined_Scripts/Alexa_JSON_Combined_LED_Security_Alarm
    sudo ./mjpg_streamer -i "./input_uvc.so -f 10 -r 640x320 -n -y" -o "./output_http.so -w ./www -p 80"

# Commands to run the main script which initialtes scripts based on user's command  
# Receive Json commands from Developer Account script 
    cd /home/pi/FYP-SS/Combined_Scripts/Alexa_JSON_Combined_LED_Security_Alarm
    source ~/.profile
    workon cv
    python3 Final_Alexa_Json_Integration_local_execution.py

    cd /home/pi/FYP-SS/Combined_Scripts/Alexa_JSON_Combined_LED_Security_Alarm
    ./ngrok http 5000
    https://developer.amazon.com/home.html
