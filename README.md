# Alexa-Smart-Speaker brief description 

Objective of this project is to design a advanced Alexa smart speaker using commercial off the shelf advanced microphone array, camera module and a regular speaker interfaced to Raspberry Pi. This Smart Speaker is capable of performing Biometrics (Facial Recognition) based system wakeup in addition to calling out the wake-word. The processor on the Microphone array used to capture user’s voice has inbuilt Digital Signal Processing based voice algorithms which is custom tuned for better capturing and understanding of user’s speech resulting in a successful full-duplex human-machine speech interaction. In addition to Biometrics based system wakeup and microphone array-based interaction, it’s also enabled with custom skills which can perform Audio processing, Artificial Intelligence & Computer Vision based tasks when requested by user. 

**Basic Features of the this Alexa smart speaker prototype**

    Biometrics based Alexa wakeup & interaction using ReSpeaker v2

    Far-field voice capture 

    AEC capabilities for higher wake-word detection accuracy

    Noise Suppression for better user interaction 

**Special features - Alexa, friday custom skills** 

    USB RGB LED Controller

    Deep Learning & Open CV based object detection

    Audio Processing based Alarm Detector 

    Open CV based Security System

    Web-based MJPEG Streaming

**Below are the commands to run the provided scrips:** 

**Face Recog Script**

	cd /home/pi/FYP-SS/Combined_Scripts/Face_Recog_Wakeup_Alexa_C_SDK
	source ~/.profile
	workon cv
	python3 pi_face_recognition.py --cascade haarcascade_frontalface_default.xml \
	    --encodings encodings.pickle

**Alexa C++ SDK build** 	

    sudo bash /home/pi/AlexaDeviceSDK/startsample.sh

**Fire Alarm Script**  

    cd /home/pi/FYP-SS/Combined_Scripts/Alexa_JSON_Combined_LED_Security_Alarm
    python3 email_Fire_Alarm_detection_using_mic_array.py

**Security System & email**

    cd /home/pi/FYP-SS/Combined_Scripts/Alexa_JSON_Combined_LED_Security_Alarm
    source ~/.profile
    workon cv
    python if_human_body_recog_then_email.py

**Deep Learning & Open CV based object detection**

    cd /home/pi/FYP-SS/Combined_Scripts/Alexa_JSON_Combined_LED_Security_Alarm
    source ~/.profile
    workon cv
    python dl_img_frm_cam.py

**M-JPEG Streamming**

    sudo modprobe bcm2835-v4l2
    cd /home/pi/FYP-SS/Combined_Scripts/Alexa_JSON_Combined_LED_Security_Alarm
    sudo ./mjpg_streamer -i "./input_uvc.so -f 10 -r 640x320 -n -y" -o "./output_http.so -w ./www -p 80"

**Commands to run the main script which initialtes scripts based on user's command**  

    # Receive Json commands from Developer Account script 
    cd /home/pi/FYP-SS/Combined_Scripts/Alexa_JSON_Combined_LED_Security_Alarm
    source ~/.profile
    workon cv
    python3 Final_Alexa_Json_Integration_local_execution.py

    cd /home/pi/FYP-SS/Combined_Scripts/Alexa_JSON_Combined_LED_Security_Alarm
    ./ngrok http 5000
    https://developer.amazon.com/home.html
    
**Commands to callout**

	ask friday to turn on sky lights
	ask friday to turn on crimson lights
	ask friday to turn lights off

	Ask friday what she sees

	ask friday to activate alarm detector 
	ask friday to deactivate alarm detector

	ask friday to turn on security system 
	ask friday to shut down security system

	Ask friday to open eyes
	Ask friday to close eyes

**If you use the code in this repository in your work, please cite these paper using the BibTex entry below**

```
@inproceedings{sudharsan2019ai,
  title={AI Vision: Smart speaker design and implementation with object detection custom skill and advanced voice interaction capability},
  author={Sudharsan, Bharath and Kumar, Sree Prem and Dhakshinamurthy, Rakesh},
  booktitle={2019 11th International Conference on Advanced Computing (ICoAC)},
  year={2019},
  organization={IEEE}
}

@inproceedings{sudharsanaicsalexa,
  author    = {Bharath Sudharsan and
               Peter Corcoran and
               Muhammad Intizar Ali},
  title     = {Smart Speaker Design and Implementation with Biometric Authentication
               and Advanced Voice Interaction Capability},
  booktitle = {Proceedings for the 27th AIAI Irish Conference on Artificial Intelligence
               and Cognitive Science},
  year      = {2019},
  url       = {http://ceur-ws.org/Vol-2563/aics\_29.pdf}
}

```

