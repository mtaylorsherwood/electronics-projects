# Raspberry Pi &amp; Arduino Projects

Projects for the Raspberry Pi or Arduino's I have sitting around.

## Projects

### Temperature Logger

[temperature_logger.py](src/pi/temperature_logger.py)

[Dashboard](https://io.adafruit.com/mtaylorsherwood/dashboards/officestats?kiosk=true)

Logs the current temperature in the room and sends it to the Adafruit IO service.

Uses a Enviro-phat by Pimoroni sat on a Raspberry Pi Zero.

## Useful Repositories & Links

- Raspberry Pi Webcam by [Jeff Geerling](https://github.com/geerlingguy)
  - [https://github.com/geerlingguy/pi-webcam](https://github.com/geerlingguy/pi-webcam)

## Helpful Things

### Installing a Script as a Service

For something to run, and keep running when it inevitably crashes, we can use the built in Linux process `systemd` to manage it.

To get this working:

- Make sure it has the Python shebang at the top of the file `#!usr/bin/python3`
  - This may be different for you, try `which python` or `which python3` to get the location on your system
- Make the script executable `chmod a+x your_script_filename.py`
- Create the service file:
  - `cd /etc/systemd/system`
  - `sudo touch your_service_name.service`
  - `sudo nano your_service_name.service`
  - Then that file needs to contain something like this:

```
[Unit]
Description=My service description here

[Service]
User=pi
WorkingDirectory=/home/pi
ExecStart=/path/to/your/script.py
Restart=always

[Install]
WantedBy=multi-user.target
```

- Then `CTRL + X` to exit, hitting `Y` to save
- You can start the service using `sudo systemctl start your_service_name.service`
- Then check on the service using `sudo systemctl status your_service_name.service`
- To get it "installed" so it runs on boot `sudo systemctl enable your_service_name.service`
  - To "uninstall" `sudo systemctl disable your_service_name.service`

That should be it and it runs on boot. Using the `journalctl` should allow to check on it and the log output

`journalctl -u your_service_name -e`
