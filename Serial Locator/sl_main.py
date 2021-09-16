# Serial Locator
# Author: Daniel Williams
# Date Created: 9/15/2021 7:36 PM

from serial import Serial

# Opening Serial Port Connection
ser = Serial('COM8', 9600)
ser.open()

DISCONNECT = 0
while not DISCONNECT:
    # read in the line from the Serial Connection
    line = ser.read()
    
    # Parse the line for the data
    lat, lng, time, date, speed, sat_in_view, sat_conn, sat_used = line.split(",")
    
    #Write data to file to be read by plotter
    with open('Serial Locator\GPS_Data\data.csv', 'a') as f:
        f.write(f"{date} {time},{lat},{lng}\n")

f.close()
