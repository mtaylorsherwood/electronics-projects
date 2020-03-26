# Utilises code from:
# Adafruit Python IO repository - https://github.com/adafruit/Adafruit_IO_Python
# Pimoroni Enviro-phat repository - https://github.com/pimoroni/enviro-phat

import time
from envirophat import weather, light
from Adafruit_IO import Client, Feed, Data, RequestError

# Keys for the Adafruit service
ADAFRUIT_IO_KEY = 'YOUR_AIO_KEY'
ADAFRUIT_IO_USERNAME = 'YOUR_AIO_USERNAME'

unit = 'hPa'  # Pressure unit, can be either hPa (Hectopascals) or Pa (pascals)
seconds = 30

# Create an instance of the REST client.
aio = Client(ADAFRUIT_IO_USERNAME, ADAFRUIT_IO_KEY)

try:
    temperature = aio.feeds('temperature')
except RequestError:
    feed = Feed(name="temperature")
    temperature = aio.create_feed(feed)

try:
    pressure = aio.feeds('pressure')
except RequestError:
    feed = Feed(name="pressure")
    pressure = aio.create_feed(feed)

try:
    lightLevel = aio.feeds('lightlevel')
except RequestError:
    feed = Feed(name="lightlevel")
    lightLevel = aio.create_feed(feed)

try:
    while True:
        aio.send_data(temperature.key, weather.temperature())
        aio.send_data(pressure.key, weather.pressure(unit=unit))
        aio.send_data(lightLevel.key, light.light())

        time.sleep(seconds)

except KeyboardInterrupt:
    pass
