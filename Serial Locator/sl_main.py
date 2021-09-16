# Serial Locator
# Author: Daniel Williams
# Date Created: 9/15/2021 7:36 PM

from serial import Serial

# Opening Serial Port Connection
ser = Serial()
ser.baudrate = 9600
ser.port = 'COM8'

if ser.isOpen():
    print(ser.port, " is already open.")
else:
    ser.open()
    print(ser.port, " has been opened")

string = ""
previous_string = ""

#Prep File Headers
try:
    f = open('Serial Locator\\GPS_Data\\data.csv', 'w')
    f.write("Latitude,Longitude,Time,Date,Year,Speed,Satellites_in_view,Connected_Satellites,Satellites_Used,color\n")
    f.close()
except:
    print("File Exists")

while True:
    # read in the line from the Serial Connection
    line = ser.read()
    print("-", line)
    if line == b'' or line == b'\r':
        continue
    elif line == b'\n':
        #Write data to file to be read by plotter
        if string != previous_string:
            with open('Serial Locator\\GPS_Data\\data.csv', 'a') as f:
                f.write(f"{string}\n")
                f.close()
                previous_string = string
        string = ""
    else:
        # Decode from bit to string
        line = str(line.decode("utf-8"))
        # Build each line for the CSV
        string += line    
