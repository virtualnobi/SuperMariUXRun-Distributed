#!python
# -*- coding: latin-1 -*-
"""
(c) by nobisoft 2017-
"""
# Imports
## Standard
from __future__ import print_function
import unittest
from datetime import datetime
## Contributed
## nobi
from PushSensor import PushSensor
## Project



class TestPushSensor(unittest.TestCase):
    """
    """
    
    

# Constants
# Class Variables
# Class Methods
# Lifecycle
# Setters
# Getters
# Event Handlers
# Inheritance - Superclass
# Other API Functions
    def testCreateSequence(self):
        ps1 = PushSensor('First')
        ps3 = PushSensor('Last')
        ps2 = PushSensor('Second', predecessor=ps1, successor=ps3)
        ps1.setSuccessor(ps2)
        ps3.setPredecessor(ps2)
        self.assertEqual(ps1.getSuccessor(), ps2, 'Accessing successor failed')
        self.assertEqual(ps3.getPredecessor(), ps2, 'Accessing predecessor failed')
        self.assertEqual(ps1, ps2.getPredecessor(), 'Creation with predecessor failed')
        self.assertEqual(ps3, ps2.getSuccessor(), 'Creation with successor failed')
        self.assertEqual(ps1.getPredecessor(), None, 'Creation added bogus predecessor')
        self.assertEqual(ps3.getSuccessor(), None, 'Creation added bogus successor')
        self.assertEqual(ps1.getName(), 'First', 'Naming failed')


    def testState(self):
        ps1 = PushSensor('First')
        self.assertEqual(ps1.getState(), PushSensor.StateIdle, 'Wrong state after creation')
        with self.assertRaises(AssertionError):
            ps1.receiveMessage(None, PushSensor.MessagePush, datetime.now())
        self.assertEqual(ps1.getState(), PushSensor.StatePushed, 'Wrong state after push')
        with self.assertRaises(AssertionError):
            ps1.receiveMessage(None, PushSensor.MessagePush, datetime.now())
        self.assertEqual(ps1.getState(), PushSensor.StatePushed, 'Wrong state after 2nd push')
        with self.assertRaises(AssertionError):
            ps1.receiveMessage(None, PushSensor.MessageContinue, datetime.now())
        self.assertEqual(ps1.getState(), PushSensor.StatePushed, 'Wrong state after continue')
        with self.assertRaises(AssertionError):
            ps1.receiveMessage(None, PushSensor.MessageComplete, datetime.now())
        self.assertEqual(ps1.getState(), PushSensor.StateFinished, 'Wrong state after complete')
#         self.assertTrue(PartialDateTime(''), 'Empty string failed')
#         self.assertFalse((PartialDateTime('') < PartialDateTime('')))



# Internal - to change without notice
# Class Initialization
pass



# Executable Script
if __name__ == '__main__':
    unittest.main()
