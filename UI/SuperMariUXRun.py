#!python
# -*- coding: latin-1 -*-
"""
(c) by nobisoft 2017-
"""


# Imports
## Standard
from __future__ import print_function
## Contributed
import wx
## nobi
## Project
from model.PushSensor import PushSensor
from UI.PushSensorView import PushSensorView



class SuperMariUXRun(wx.Frame): 
    """
    """
    

# Constants
# Class Variables
# Class Methods
# Lifecycle
    def __init__(self,
                 parent,
                 numberOfSensors, 
                 title = '',
                 pos = wx.DefaultPosition,
                 size = wx.DefaultSize,  # Size(1500,600),
                 style = (wx.DEFAULT_FRAME_STYLE | wx.SUNKEN_BORDER | wx.CLIP_CHILDREN)):
        """
        """
        # inheritance
        wx.Frame.__init__(self, parent, -1, title, pos, size, style)
        # internal state
        self.sensorList = [PushSensor('PushSensor %d' % i) for i in range(numberOfSensors)]
        self.linkSensors()
        self.sensorViews = [PushSensorView(self, sensor) for sensor in self.sensorList]
        self.showSensorViews()



# Setters
# Getters
# Event Handlers
# Inheritance - Superclass
# Other API Functions
# Internal - to change without notice
    def linkSensors(self):
        """Link the PushSensors in self.sensorList by successor/predecessor relations.
        """
        for index in range(len(self.sensorList)): 
            sensor = self.sensorList[index]
            if (index > 0):
                sensor.setPredecessor(self.sensorList[index - 1])
            if (index < (len(self.sensorList) - 1)):
                sensor.setSuccessor(self.sensorList[index + 1])


    def showSensorViews(self):
        """Place the PushSensorViews in self.sensorViews in a sequence on self.
        """
        sizer = wx.BoxSizer(wx.HORIZONTAL)
        for view in self.sensorViews:
            sizer.Add(view, proportion=1, flag=(wx.ALIGN_CENTER | wx.EXPAND | wx.ALL), border=10)
        self.SetSizer(sizer)
        sizer.Fit(self)



# Class Initialization
# Executable Script
if __name__ == "__main__":
    app = wx.App(False)    
    frame = SuperMariUXRun(None, 4, title='SuperMariUXRun')
    frame.Show()
    app.MainLoop()


