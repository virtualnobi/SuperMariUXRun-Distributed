#!python
# -*- coding: latin-1 -*-
"""
(c) by nobisoft 2017-
"""


# Imports
## Standard
from __future__ import print_function
import logging
## Contributed
import wx
## nobi
## Project



class wxTextCtrlHandler(logging.Handler): 
    """A logging.Handler which writes to a wx.TextCtrl
    """
    

# Constants
    ConstantName = 'value'


# Class Variables



# Class Methods
#     @classmethod
#     def classMethod(clas):
#         """
#         """
#         pass



# Lifecycle
    def __init__(self, ctrl, maxLines=1000, **kwargs):
        """
        """
        # inheritance
        super(wxTextCtrlHandler, self).__init__(**kwargs)
        # internal state
        self.ctrl = ctrl
        self.maxLines = maxLines
        self.logString = '(empty log)'
        # 
        print(self.logString)
        self.ctrl.SetValue(self.logString)



# Setters
# Getters
# Event Handlers
# Inheritance - Superclass
# Other API Functions
    def emit(self, logRecord):
        """
        class Form1(wx.Panel):
    def __init__(self, parent):
        wx.Panel.__init__(self, parent)

        self.logger = wx.TextCtrl(self,5, "",wx.Point(20,20), wx.Size(200,200), \
                wx.TE_MULTILINE |  wx.TE_READONLY)# |  wx.TE_RICH2)

        t = Timer(0.1, self.AddText)
        t.start()

    def AddText(self):
        # Resart the timer
        t = Timer(0.25, self.AddText)
        t.start() 

        # Work out if we're at the end of the file
        currentCaretPosition = self.logger.GetInsertionPoint()
        currentLengthOfText = self.logger.GetLastPosition()
        if currentCaretPosition != currentLengthOfText:
            self.holdingBack = True
        else:
            self.holdingBack = False

        timeStamp = str(time.time())

        # If we're not at the end of the file, we're holding back
        if self.holdingBack:
            print "%s FROZEN"%(timeStamp)
            self.logger.Freeze()
            (currentSelectionStart, currentSelectionEnd) = self.logger.GetSelection()
            self.logger.AppendText(timeStamp+"\n")
            self.logger.SetInsertionPoint(currentCaretPosition)
            self.logger.SetSelection(currentSelectionStart, currentSelectionEnd)
            self.logger.Thaw()
        else:
            print "%s THAWED"%(timeStamp)
            self.logger.AppendText(timeStamp+"\n")
---
            def OnText(self, event):
        #text_ctrl.ShowPosition(text_ctrl.GetLastPosition())
        text_ctrl.ScrollPages(1)
---
        After calling AppendText, call ScrollLines(-1)

        """
        addedLogString = self.format(logRecord)
        print(addedLogString)
        self.ctrl.SetInsertionPointEnd()
        self.ctrl.AppendText(addedLogString + '\n')
        self.ctrl.SetInsertionPointEnd()
#        self.logString = (self.logString + '\n' + addedLogString)  # TODO: respect maxLines
#        self.ctrl.SetValue(self.logString)



# Internal - to change without notice
    pass


# Class Initialization
pass



# Executable Script
if __name__ == "__main__":
    pass


