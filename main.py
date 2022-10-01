from serial import Serial
from phue import Bridge

ip_hue = "192.168.0.223"

ser = Serial(port="/dev/ttyUSB0", baudrate=115200)
b = Bridge(ip_hue)
b.connect()

id_sc1 = b.get_light("sc1")

while True:
    line = str(ser.readline())
    m = match(regularExpression, line)
    if m:
        pass

    if line.startswith("b'!"):
        continue
