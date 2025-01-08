import RPi.GPIO as GPIO
import time

# Configuration
FAN_PIN = 4  # GPIO pin where the fan is connected
TEMP_THRESHOLD_ON = 60  # Temperature (°C) to turn the fan on
TEMP_THRESHOLD_OFF = 50  # Temperature (°C) to turn the fan off
CHECK_INTERVAL = 5  # Time (seconds) between temperature checks

# Set up GPIO
GPIO.setmode(GPIO.BCM)  # Use Broadcom GPIO pin numbering
GPIO.setup(FAN_PIN, GPIO.OUT)
GPIO.output(FAN_PIN, GPIO.LOW)  # Fan starts off


def get_cpu_temperature():
    """Reads the CPU temperature from the system."""
    with open("/sys/class/thermal/thermal_zone0/temp", "r") as file:
        temp = int(file.read()) / 1000.0  # Convert from millidegree Celsius to Celsius
    return temp


def control_fan():
    """Control the fan based on the CPU temperature."""
    try:
        fan_on = False  # Track fan status
        while True:
            cpu_temp = get_cpu_temperature()
            print(f"CPU Temperature: {cpu_temp:.1f}°C")

            if not fan_on and cpu_temp > TEMP_THRESHOLD_ON:
                GPIO.output(FAN_PIN, GPIO.HIGH)
                fan_on = True
                print("Fan turned ON")

            elif fan_on and cpu_temp < TEMP_THRESHOLD_OFF:
                GPIO.output(FAN_PIN, GPIO.LOW)
                fan_on = False
                print("Fan turned OFF")

            time.sleep(CHECK_INTERVAL)

    except KeyboardInterrupt:
        print("Exiting fan control script...")

    finally:
        GPIO.output(FAN_PIN, GPIO.LOW)  # Ensure fan is off
        GPIO.cleanup()  # Clean up GPIO settings


if __name__ == "__main__":
    control_fan()
