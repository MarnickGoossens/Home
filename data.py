from serial import Serial

ser = Serial(port="/dev/ttyUSB0", baudrate=115200)

while True:
    line = str(ser.readline())
    print(line)

    if line.startswith("b'!"):
        print("-----------------------")
