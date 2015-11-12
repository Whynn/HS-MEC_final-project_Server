import time
import sys
sys.path.append('/var/lib/cloud9/server/HS-MEC_final-project_Server/example/am2302_sensor/Adafruit_Python_DHT')
from flask import Flask, render_template
import Adafruit_DHT
import serial

app = Flask(__name__)
HTsensor = Adafruit_DHT.AM2302
HTpin = 'P8_11'
ser = serial.Serial('/dev/ttyACM0', 9600)

while True:
    humidity, temperature = Adafruit_DHT.read_retry(HTsensor, HTpin)
    dustVal = ser.readline()
    if dustVal is not None:
        print(dustVal+"%")
    else:
        print("Failed to get Dust Sensor value.")
    if humidity is not None and temperature is not None:
        print('Temp={0:0.1f}*C  Humidity={1:0.1f}%'.format(temperature, humidity))
    else:
        print('Failed to get reading. Try again!')
    time.sleep(1)

@app.route('/')
def home():
    return render_template('index.html')
    
@app.route('/temp', method=['POST', 'GET'])
def readTemp():
    #192.168.7.2:1234/temp
    if temperature is not None:
        return '%d' % (temperature)
    else:
        return 'Failed.'

@app.route('/humid', method=['POST', 'GET'])
def readHumid():
    #192.168.7.2:1234/humid
    if humidity is not None:
        return '%d' % (humidity)
    else:
        return 'Failed.'

@app.route('/dust', method=['POST', 'GET'])
def readDust():
    #192.168.7.2:1234/dust
    return '%d' % (aread)
    
    

@app.route('/hitter/<int:status>', method=['POST', 'GET'])
def hitterOnOff(status):
    #192.168.7.2:1234/hitter/0 -> hitter Off
    #192.168.7.2:1234/hitter/255 -> hitter On
    return '%d' % (status)
    
@app.route('/aircon/<int:status>', method=['POST', 'GET'])
def airconOnOff(status):
    #192.168.7.2:1234/aircon/0 -> aircon Off
    #192.168.7.2:1234/aircon/255 -> aircon On
    return '%d' % (status)
    

@app.route('/humidifier/<int:status>', method=['POST', 'GET'])
def humidifierOnOff(status):
    #192.168.7.2:1234/humidifier/0 -> humidifier Off
    #192.168.7.2:1234/humidifier/255 -> humidifier On
    return '%d' % (status)
   
@app.route('/cooler/<int:status>', method=['POST', 'GET'])
def coolerOnOff(status):
    #192.168.7.2:1234/cooler/0 -> cooler Off
    #192.168.7.2:1234/cooler/255 -> cooler On
    return '%d' % (status)
   
if __name__ == '__main__':
    app.debug=True
    app.run(host)