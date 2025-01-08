# rpi4-fan-control

Simple python script to control fan on rpi4

## Steps to Use

1. Connect the Fan to GPIO  
Connect the positive wire of the fan to the GPIO pin (e.g., GPIO18).  
Connect the ground wire of the fan to a GND pin on the Raspberry Pi.

2. Install Dependencies  
Install the required library for GPIO

    ```bash
    sudo apt update
    sudo apt install python3-rpi.gpio
    ```

3. Run the Script

    ```bash
    python3 fan_control.py
    ```

4. Adjust Thresholds  
Update TEMP_THRESHOLD_ON and TEMP_THRESHOLD_OFF as per your cooling requirements.

5. Autostart on Boot  
To run the script automatically at startup, add it to `/etc/rc.local` or create a systemd service.
