sudo ./hubpower 001:002 power 2 off
sudo ./hubpower 001:002 power 2 on
sleep 3
sudo bash /home/pi/AlexaDeviceSDK/startsample.sh
sleep 120
sudo pkill -f startsample.sh 
sleep 3


