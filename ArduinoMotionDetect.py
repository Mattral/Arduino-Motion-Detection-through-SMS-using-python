#!/usr/bin/env python
import serial
import requests
import zang
from datetime import date, datetime, timedelta
from zang import ZangException, Configuration, ConnectorFactory
sid = 'Add Yours Here'
authToken = 'Add Yours Here'
url = 'http://api.zang.io/v2'
configuration = Configuration(sid, authToken, url=url)
smsMessagesConnector = ConnectorFactory(configuration).smsMessagesConnector
# Set the serial port to the same serial port you uploaded the arduino sketch to
# In the Arduino IDE, click "Tools > Serial Port"
# SERIAL_PORT = "/dev/tty.usbserial-A70064Mh"
SERIAL_PORT = "COM3"
SERIAL_BAUD = 115200
# Don"t send more than one message every 30 minutes
SENSOR_INTERVAL = timedelta(minutes=30)
# Start the server
if __name__ == "__main__":
 print("Starting SMS motion detector server at", datetime.now())
 last_sent_time = None
 # Open a serial connection to the Arduino
 with serial.Serial(SERIAL_PORT, SERIAL_BAUD) as arduino:
 while True:
 print("Polling Arduino...")
 # Listen for the Arduino to send a byte
 byte_received = arduino.read()
 print("Received byte:", byte_received)
 # Motion was detected
 if byte_received == b'1':
 print("Motion detected at", datetime.now())
 # If we haven"t sent an SMS in the last 31 minutes, send one now
 if not last_sent_time or (datetime.now() - last_sent_time) > SENSOR_INTERVAL:
 last_sent_time = datetime.now()
 print("Sending SMS...")
 
# Send request to TelAPI to send SMS
 try:
 smsMessage = smsMessagesConnector.sendSmsMessage(
 to='+970566660009',
 body='Hello from Zang!',
 from_='+1(704) 445-2979')
 print(smsMessage)
 except ZangException as ze:
 print(ze)