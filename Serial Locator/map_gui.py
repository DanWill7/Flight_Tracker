# File to run GUI menu before live plotting and provide a front end to the user
# Author: Daniel Williams
# Date Created: 9/15/2021 9:26PM

import os

import matplotlib.pyplot as plt
import PySimpleGUI as sg

import plot_loc as pl


def run_gui():
    """Creates a simple gui prior to plotting to allow user to select file to plot."""

    # layout for the pysimplegui buttons and file explorer
    layout = [
        [
            sg.In("test.txt"),
            sg.FileBrowse(file_types=(("Text Files", "*.txt"),)),
        ],
        [sg.Button("Plot"), sg.Cancel()],
    ]

    # creates gui window
    window = sg.Window("GPS Location", layout)

    # infinite while loop to last for the duration of the open gui
    while True:
        # storing the user input in the gui as event and values variables
        event, values = window.read()

        # breaks out of while loop if cancel is selected
        if event in (sg.WIN_CLOSED, "Cancel"):
            break

        # runs the liveplot UDF when plot button is selected based on the file selected in the file browser
        elif event == "Plot":
            # strip off path front end to trim and just get filename
            filename = os.path.basename(values[0])
            # print filename used to terminal
            print("File selected: " + filename)
            # run live plot UDF
            pl.live_plot(filename)

    # closes gui window
    window.close()
