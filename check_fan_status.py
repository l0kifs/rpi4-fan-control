from time import sleep
import RPi.GPIO as GPIO

# Configuration
FAN_PIN = 4  # GPIO pin where the fan is connected

# Set up GPIO
GPIO.setmode(GPIO.BCM)  # Use Broadcom GPIO pin numbering
GPIO.setup(FAN_PIN, GPIO.OUT)

# Check the status
fan_status = GPIO.input(FAN_PIN)

if fan_status == GPIO.HIGH:
    print("Fan is ON")
    GPIO.output(FAN_PIN, GPIO.LOW)  # Turn the fan off
else:
    print("Fan is OFF")

# Clean up GPIO
sleep(5)
GPIO.cleanup()
