from serial import Serial
from re import match
from datetime import datetime, timedelta
from time import sleep
from phue import Bridge


verbruik_aan = 700
minimum_tijd_aan = 2


ser = Serial(port="/dev/ttyUSB0", baudrate=115200)
regularExpression = "b'(1-0:\d.7.0)\((\d{2}.\d{3}).*'"

ip_hue = "192.168.0.223"
b = Bridge(ip_hue)
b.connect()

tijd_on = datetime.now()
codes = ["1-0:1.7.0", "1-0:2.7.0"]
dictionary = {}


def plug(dictionary):
    verbruik = int(dictionary["1-0:1.7.0"] - dictionary["1-0:2.7.0"])
    sc1_status = b.get_light("sc1")["state"]["on"]

    if not sc1_status and verbruik >= verbruik_aan:
        b.set_light("sc1", "on", True)
        tijd_on = datetime.now()
    elif (
        sc1_status
        and tijd_on + timedelta(minutes=minimum_tijd_aan) < datetime.now()
        and verbruik < verbruik_aan
    ):
        b.set_light("sc1", "on", False)


while True:
    line = str(ser.readline())
    m = match(regularExpression, line)
    if m:
        code = m.group(1)
        waarde = m.group(2)
        if code in codes:
            dictionary[code] = float(waarde) * 1000

    if line.startswith("b'!"):
        plug(dictionary)
        sleep(5)
        continue
