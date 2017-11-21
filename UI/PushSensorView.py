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
import os.path
## Contributed
import wx
import wx.lib.scrolledpanel
import wx.animate
## nobi
from nobi.ObserverPattern import Observer
## Project
from model.PushSensor import PushSensor
import UI  # to access UI.PackagePath



# # Internationalization  # requires "PackagePath = UI/__path__[0]" in _init_.py
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
        self.ImageLEDOn = wx.Image(os.path.join(UI.PackagePath, 'led_on.jpg'), wx.BITMAP_TYPE_JPEG).ConvertToBitmap()
        self.ImageLEDOff = wx.Image(os.path.join(UI.PackagePath, 'led_off.jpg'), wx.BITMAP_TYPE_JPEG).ConvertToBitmap()
        self.ImageFireworks = wx.Image(os.path.join(UI.PackagePath, 'fireworks.jpg'), wx.BITMAP_TYPE_JPEG).ConvertToBitmap()
#        self.fireworks = wx.animate.Animation(os.path.join(UI.PackagePath, 'smallFireworks.gif'))
#        self.stateVisualization = None
        # layout view
        self.outOfSightSizer = wx.BoxSizer()  
        s = wx.GridBagSizer(vgap=10, hgap=10)
        s.Add((1, 130), (2, 0))
        s.Add((130, 1), (0, 2))
        s.Add((1, 1), (5, 3))
        s.Add(wx.StaticText(self, -1, self.model.getName()), (1,1))
        self.stateView = wx.StaticBitmap(self, -1, self.ImageLEDOff)
        s.Add(self.stateView, (1, 2), (2, 1))
#         self.outOfSightSizer.Add(self.ledView)
        self.stateText = wx.StaticText(self, -1, '')
        s.Add(self.stateText, (2, 1))
#         self.fireworksView = wx.animate.AnimationCtrl(self, -1, self.fireworks)
#         self.fireworksView.SetUseWindowBackgroundColour()
#         self.fireworksView.Play()
#         self.outOfSightSizer.Add(self.fireworksView)
        self.pushButton = wx.Button(self, -1, 'Push')
        self.Bind(wx.EVT_BUTTON, self.onPush, self.pushButton)
        s.Add(self.pushButton, (3, 1), (1, 2), wx.EXPAND)
        logPane = wx.lib.scrolledpanel.ScrolledPanel(self, -1)
        self.logText = wx.StaticText(logPane, -1, '(empty log)')
        s.Add(logPane, (4, 1), (1, 2))
        self.SetSizer(s)
        # 
        self.updateAspect(self.model, PushSensor.AspectStateChanged)



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
#             if (self.stateVisualization):
#                 self.stateVisualization.Destroy()
            if (observable.getState() == PushSensor.StateIdle):
#                 self.stateVisualization = wx.StaticBitmap(self, -1, self.ImageLEDOff)
#                 self.GetSizer().Add(self.stateVisualization, (1, 2))
#                 if (self.GetSizer().FindItemAtPosition((1, 2)) == self.fireworksView):
#                     self.GetSizer().Detach(self.fireworksView)
#                     self.outOfSightSizer.Add(self.fireworksView)
#                     self.outOfSightSizer.Detach(self.ledView)
#                     self.GetSizer().Add(self.ledView, (1, 2))
                self.stateView.SetBitmap(self.ImageLEDOff)
#                 self.ledView.Show()
#                self.GetSizer().Hide(self.fireworksView)
#                 self.fireworksView.Hide()
                self.GetSizer().Layout()
            elif (observable.getState() == PushSensor.StatePushed):
#                 self.stateVisualization = wx.StaticBitmap(self, -1, self.ImageLEDOn)
#                 self.GetSizer().Add(self.stateVisualization, (1, 2))
#                 if (self.GetSizer().FindItemAtPosition((1, 2)) == self.fireworksView):
#                     self.GetSizer().Detach(self.fireworksView)
#                     self.outOfSightSizer.Add(self.fireworksView)
#                     self.outOfSightSizer.Detach(self.ledView)
#                     self.GetSizer().Add(self.ledView, (1, 2))
                self.stateView.SetBitmap(self.ImageLEDOn)
#                 self.ledView.Show()
#                 self.GetSizer().Hide(self.fireworksView)
#                 self.fireworksView.Hide()
                self.GetSizer().Layout()
            elif (observable.getState() == PushSensor.StateFinished):
#                 self.stateVisualization = wx.animate.AnimationCtrl(self, -1, self.fireworks)
#                 self.stateVisualization.SetUseWindowBackgroundColour()
#                 self.stateVisualization.Play()
#                 self.GetSizer().Add(self.stateVisualization, (1, 2))
#                 if (self.GetSizer().FindItemAtPosition((1, 2)) == self.ledView):
#                     self.GetSizer().Detach(self.ledView)
#                     self.outOfSightSizer.Add(self.ledView)
#                     self.outOfSightSizer.Detach(self.fireworksView)
#                     self.GetSizer().Add(self.fireworksView, (1, 2))
#                 self.ledView.Hide()
                self.stateView.SetBitmap(self.ImageFireworks)
#                self.GetSizer().Show(self.fireworksView)
#                 self.fireworksView.Show()
                self.GetSizer().Layout()
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


