import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
Trig = 18
ECHO = 24
buzzer = 3
LED = 2
print("Distance")
GPIO.setup(Trig,GPIO.OUT)
GPIO.setup(ECHO,GPIO.IN)
GPIO.setup(LED,GPIO.OUT)
GPIO.setup(buzzer,GPIO.OUT)

try:
	while True:
		GPIO.output(Trig, False)
		time.sleep(1)
		GPIO.output(Trig, True)
		time.sleep(0.01)
		GPIO.output(Trig, False)

		while GPIO.input(ECHO) ==0:
			pulse_start = time.time()

	        while GPIO.input(ECHO) ==1:
	                pulse_end = time.time()

		pulse_duration = pulse_end - pulse_start

		distance = pulse_duration*11150
		distance = round(distance,2)

		if distance < 20:
			GPIO.output(buzzer, GPIO.HIGH)
			GPIO.output(LED, GPIO.LOW)
			print("BUZZER ON/LED OFF")
		else:
			print("BUZZER OFF/LED ON")
	                GPIO.output(buzzer, GPIO.LOW)
	                GPIO.output(LED, GPIO.HIGH)

except KeyboardInterrupt:
        GPIO.cleanup()

