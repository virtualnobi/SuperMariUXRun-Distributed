#!python
# -*- coding: latin-1 -*-
"""
(c) by nobisoft 2017-
"""


# Imports
## Standard
from __future__ import print_function
import logging
from datetime import datetime
# import gettext
# import os.path
## Contributed
import wx
import wx.lib.scrolledpanel
## nobi
from nobi.ObserverPattern import Observer
## Project
from model.PushSensor import PushSensor



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




class PushSensorView(wx.Panel, Observer): 
    """Show the state of a PushSensor, and allow it to be pushed.
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
    def __init__(self, parent, aPushSensor):
        """
        """
        # inheritance
        super(PushSensorView, self).__init__(parent, -1)
        Observer.__init__(self)
        # internal state
        self.model = aPushSensor
        self.model.addObserverForAspect(self, PushSensor.AspectStateChanged)
        s = wx.GridBagSizer(4, 2)
        s.Add(wx.StaticText(self, -1, self.model.getName()), (0,0))
        self.stateText = wx.StaticText(self, -1, self.model.getState())
        s.Add(self.stateText, (1, 0))
        self.pushButton = wx.Button(self, -1, 'Push')
        self.Bind(wx.EVT_BUTTON, self.onPush, self.pushButton)
        s.Add(self.pushButton, (2, 0), (1, 2))
        logPane = wx.lib.scrolledpanel.ScrolledPanel(self, -1)
        self.logText = wx.StaticText(logPane, -1, '(empty log)')
        s.Add(logPane, (3, 0), (1, 2))
        self.SetSizer(s)



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
        if (aspect == PushSensor.AspectStateChanged):
            self.stateText.SetLabel(observable.getState())
            if (observable.getState() == PushSensor.StateIdle):
                pass
            elif (observable.getState() == PushSensor.StatePushed):
                pass
            elif (observable.getState() == PushSensor.StateFinished):
                pass
            else:
                assert False, ('Illegal state in PushSensor %s' % observable.getName())


    def onPush(self, event):  # @UnusedVariable
        """
        """
        self.model.receiveMessage(None, PushSensor.MessagePush, datetime.now())


# Inheritance - Superclass
# Other API Functions
# Internal - to change without notice
    pass


# Class Initialization
pass



# Executable Script
if __name__ == "__main__":
    pass


