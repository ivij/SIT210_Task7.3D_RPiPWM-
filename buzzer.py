import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
Trig = 23
ECHO = 18
buzzer = 3
LED = 2

print(" Ultrasonic Sensor in Work")

GPIO.setup(Trig,GPIO.OUT)

GPIO.setup(ECHO,GPIO.IN)

GPIO.setup(LED,GPIO.OUT)

GPIO.setup(buzzer,GPIO.OUT)

level_1 = GPIO.PWM(2,20)

level_2 = GPIO.PWM(3,20)

try:
	while True:

    		GPIO.output(Trig, False)

   	 	time.sleep(1)

    		GPIO.output(Trig, True)

    		time.sleep(0.01)

    		GPIO.output(Trig, False)


    		while GPIO.input(ECHO )== 0:

        		initial_time = time.time()

    		while GPIO.input(ECHO) == 1:

        		final_time = time.time()

    		net_duration = final_time - initial_time

    		total_distance = net_duration*11150

    		total_distance = round(total_distance,2)

    		level_1.start(0)

    		level_2.start(0)

    		if 25 < total_distance < 50:

        		level_1.ChangeDutyCycle(2.0)

			level_2.ChangeDutyCycle(2.0)


    		if total_distance < 25:

        		level_1.ChangeDutyCycle(100.0)

        		level_2.ChangeDutyCycle(80.0)


    		if total_distance > 50:

			level_1.stop()

			level_2.stop()

except KeyboardInterrupt:
	GPIO.cleanup()


