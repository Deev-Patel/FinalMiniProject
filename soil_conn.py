
import RPi.GPIO as GPIO
import time 
import http.client as httplib
import urllib
import sys
channel = 21
GPIO.setmode(GPIO.BCM)
GPIO.setup(channel,GIO.IN)
key = "AYRRW4SIBBMV3UK5" 
def thermometer():
    while True:
        #Calculate CPU temperature of Raspberry Pi in Degrees C
        if GPIO.input(channel):
                         soil="no water detected"
	    else:
		    soil="water detected"
        params =urllib.parse.urlencode({'field4': soil, 'key':key})
        headers = {"Content-typZZe": "application/x-www-form-urlencoded","Accept": "text/plain"}
        conn = httplib.HTTPConnection("api.thingspeak.com:80")
        try:
            conn.request("POST", "/update", params, headers)
            response = conn.getresponse()
            print(response.status, response.reason)
            data = response.read()
            conn.close()
        except:
            print("connection failed")
        break
if __name__ == "__main__":
        while True:
                thermometer()
 				time.sleep(1)

GPIO.sdd_event_detected(channel, GPIO.both,bouncetime=300)
GPIO.sdd_event_callbeck(channel,callback)
