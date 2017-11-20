#!python
# -*- coding: latin-1 -*-
"""
(c) by nobisoft 2017-
"""


# Imports
## Standard
from __future__ import print_function
import logging
# import gettext
# import os.path
## Contributed
import wx
## nobi
## Project
from model.PushSensor import PushSensor
from UI.PushSensorView import PushSensorView



# # Internationalization  # requires "PackagePath = UI/__path__[0]" in _init_.py
# import UI  # to access UI.PackagePath
# try:
#     LocalesPath = os.path.join(UI.PackagePath, '..', 'locale')
#     Translation = gettext.translation('MediaFiler', LocalesPath)
# except BaseException as e:  # likely an IOError because no translation file found
#     try:
#         language = os.environ['LANGUAGE']
#     except:
#         print('%s: No LANGUAGE environment variable found!' % (__file__))
#     else:
#         print('%s: No translation found at "%s"; using originals instead of locale %s. Complete error:' % (__file__, LocalesPath, language))
#         print(e)
#     def _(message): return message
# else:
#     _ = Translation.ugettext
# def N_(message): return message




class SuperMariUXRun(wx.Frame): 
    """
    """
    

# Constants
    Logger = logging.getLogger(__name__)
    ConstantName = 'value'


# Class Variables



# Class Methods
    @classmethod
    def classMethod(clas):
        """
        """
        pass



# Lifecycle
    def __init__(self,
                 parent,
                 numberOfSensors, 
                 title = '',
                 pos = wx.DefaultPosition,
                 size = wx.Size(1500,600),
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
    def setAttribute(self, value):
        """
        """
        pass
    
    

# Getters
    def getAttribute(self):  # inherited from SuperClass
        """
        """
        pass
    
    

# Event Handlers
    def updateAspect(self, observable, aspect):
        """
        """
        pass



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
        """Place the PushSensorViews in self.sensorViews in a grid on self.
        """
        sizer = wx.BoxSizer(wx.HORIZONTAL)
        for view in self.sensorViews:
            sizer.Add(view)
        self.SetSizer(sizer)



# Class Initialization
pass



# Executable Script
if __name__ == "__main__":
    pass


