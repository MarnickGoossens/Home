from serial import Serial
from re import match
from phue import Bridge

ser = Serial(port="/dev/ttyUSB0", baudrate=115200)
regularExpression = "b'(1-0:\d.7.0)\((\d{2}.\d{3}).*'"

# ip_hue = "192.168.0.223"
# b = Bridge(ip_hue)
# b.connect()

codes = ["1-0:1.7.0", "1-0:2.7.0"]
dictionary = {}


def plug(dictionary):
    verbruik = int((dictionary["1-0:1.7.0"] - dictionary["1-0:2.7.0"]) * 1000)
    print(verbruik, "W")


while True:
    line = str(ser.readline())
    m = match(regularExpression, line)
    if m:
        code = m.group(1)
        waarde = m.group(2)
        if code in codes:
            dictionary[code] = float(waarde)

    if line.startswith("b'!"):
        plug(dictionary)
        continue
