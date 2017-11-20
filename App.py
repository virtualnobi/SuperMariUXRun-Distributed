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
from UI.SuperMariUXRun import SuperMariUXRun


# Constants
ConstantName = 'value'



# Globals
var = 'value'


# Functions
def function(param):
    """
    """
    pass



# Executable Script
if __name__ == "__main__":
    app = wx.App(False)    
    frame = SuperMariUXRun(None, 3, title='SuperMariUXRun')
    frame.Show()
    app.MainLoop()
