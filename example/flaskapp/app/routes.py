import time
import sys
sys.path.append('/var/lib/cloud9/server/HS-MEC_final-project_Server/example/am2302_sensor/Adafruit_Python_DHT')
from flask import Flask, render_template
import Adafruit_DHT
import serial
import Adafruit_BBIO.GPIO as GPIO
import Adafruit_BBIO.ADC as ADC

app = Flask(__name__)
ADC.setup()
HTsensor = Adafruit_DHT.AM2302
HTPin = 'P8_7'
DPin = 'P8_10'
hitterPin = 'P8_8'
GPIO.setup(hitterPin, GPIO.OUT)
airconPin1= 'P8_16'
airconPin2= 'P8_18'
GPIO.setup(airconPin1, GPIO.OUT)
GPIO.setup(airconPin2, GPIO.OUT)
humidifierPin1 = 'P9_23'
humidifierPin2 = 'P9_25'
GPIO.setup(humidifierPin1, GPIO.OUT)
GPIO.setup(humidifierPin2, GPIO.OUT)
coolerPin = 'P8_12'
GPIO.setup(coolerPin, GPIO.OUT)
humidity = 0
temperature = 0
dustVal = 0
#ser = serial.Serial('/dev/ttyACM0', 9600)

def read():
    global humidity, temperature, dustVal
    humidity, temperature = Adafruit_DHT.read_retry(HTsensor, HTPin)
    #dustRatio = ser.readline()
    #dustVal = float(dustRatio[:4])
    #if dustVal is not None:
    #    print "%0.1f" % dustVal
    #else:
    #    print("Failed to get Dust Sensor value.")
    if humidity is not None and temperature is not None:
        print('Temp={0:0.1f}*C  Humidity={1:0.1f}%'.format(temperature, humidity))
    else:
        print('Failed to get reading. Try again!')

@app.route('/')
def home():
    return render_template('index.html')
    
@app.route('/temp/', methods=['POST', 'GET'])
def readTemp():
    #192.168.7.2:1234/temp
    read()
    if temperature is not None:
        return '%0.1f' % (temperature)
    else:
        return 'Failed.'

@app.route('/humid/', methods=['POST', 'GET'])
def readHumid():
    #192.168.7.2:1234/humid
    if humidity is not None:
        return '%0.1f' % (humidity)
    else:
        return 'Failed.'

@app.route('/dust/', methods=['POST', 'GET'])
def readDust():
    #192.168.7.2:1234/dust
    if dustVal is not None:
        return '%0.1f' % (dustVal)
    else:
        return 'Failed.'
    

@app.route('/hitter/<int:status>', methods=['POST', 'GET'])
def hitterOnOff(status):
    #192.168.7.2:1234/hitter/0 -> hitter Off
    #192.168.7.2:1234/hitter/1 -> hitter On
    if status == 1:
        GPIO.output('P8_8', GPIO.HIGH)
    elif status == 0:
        GPIO.output('P8_8', GPIO.LOW)
    return '%d' % (status)
    
@app.route('/aircon/<int:status>', methods=['POST', 'GET'])
def airconOnOff(status):
    #192.168.7.2:1234/aircon/0 -> aircon Off
    #192.168.7.2:1234/aircon/1 -> aircon On
    if status == 1:
        GPIO.output('P8_16', GPIO.HIGH)
        GPIO.output('P8_18', GPIO.HIGH)
    elif status == 0:
        GPIO.output('P8_16', GPIO.LOW)
        GPIO.output('P8_18', GPIO.LOW)
    return '%d' % (status)
    

@app.route('/humidifier/<int:status>', methods=['POST', 'GET'])
def humidifierOnOff(status):
    #192.168.7.2:1234/humidifier/0 -> humidifier Off
    #192.168.7.2:1234/humidifier/1 -> humidifier On
    if status == 1:
        GPIO.output('P9_23', GPIO.HIGH)
        GPIO.output('P9_25', GPIO.HIGH)
    elif status == 0:
        GPIO.output('P9_23', GPIO.LOW)
        GPIO.output('P9_25', GPIO.LOW)
    return '%d' % (status)
   
@app.route('/cooler/<int:status>', methods=['POST', 'GET'])
def coolerOnOff(status):
    #192.168.7.2:1234/cooler/0 -> cooler Off
    #192.168.7.2:1234/cooler/1 -> cooler On
    if status == 1:
        GPIO.output('P8_12', GPIO.HIGH)
    elif status == 0:
        GPIO.output('P8_12', GPIO.LOW)
    return '%d' % (status)
   
if __name__ == '__main__':
    app.debug=True
    app.run(host='0.0.0.0')