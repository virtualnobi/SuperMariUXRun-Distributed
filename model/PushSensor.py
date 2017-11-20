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
from threading import Timer
import random
## Contributed
## nobi
from nobi.ObserverPattern import Observable
## Project



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




class PushSensor(Observable): 
    """A simulation version of a SuperMariUXRun Push sensor.
    """
    

# Constants
    Logger = logging.getLogger(__name__)
    
    # States of the push sensor 
    StateIdle = 'idle'  # waits for a push
    StatePushed = 'pushed'  # has been pushed, waits for continue/complete message from successor
    StateFinished = 'finished'  # has received confirmation that run is complete, blinks for applause

    # Message Types
    MessagePush = 'push'  # external physical push
    MessageContinue = 'continue'  # sent to predecessor to keep it "pushed"  
    MessageComplete = 'complete'  # sent to predecessor to indicate pushing of final sensor
    MessageConfirm = 'confirm'  # sent to successor to indicate it's still "pushed", triggers final blinking

    # Timings
    StayPushedDuration = 1  # how long sensor will stay in 'pushed' state before going 'idle', in seconds
    StayFinishedDuration = 2  # how long sensor will stay in 'finished' state before going 'idle', in seconds

    # Aspects of ObserverPattern
    AspectStateChanged = 'state'



# Class Variables
# Class Methods
    @classmethod
    def classMethod(clas):
        """
        """
        pass



# Lifecycle
    def __init__(self, name, predecessor=None, successor=None):
        """
        """
        # inheritance
        super(PushSensor, self).__init__([PushSensor.AspectStateChanged])
        # internal state
        self.name = name
        self.predecessor = predecessor
        self.successor = successor
        self.state = PushSensor.StateIdle
        self.timer = None



# Setters
    def setPredecessor(self, aPushSensor):
        """
        """
        self.predecessor = aPushSensor
        
    
    def setSuccessor(self, aPushSensor):
        """
        """
        self.successor = aPushSensor


    def setState(self, newState):
        """Set self's state as specified. 
        """
        if (newState in [PushSensor.StateIdle, PushSensor.StatePushed, PushSensor.StateFinished]):
            self.state = newState
            self.changedAspect(PushSensor.AspectStateChanged)
            if (self.state == PushSensor.StatePushed):
                self.setTimer(Timer(PushSensor.StayPushedDuration, 
                                    lambda : self.setState(PushSensor.StateIdle)))
            if (self.state == PushSensor.StateFinished):
                self.setTimer(Timer(PushSensor.StayFinishedDuration, 
                                    lambda : self.setState(PushSensor.StateIdle)))
        else: 
            assert False, ('PushSensor.setState(): Illegal state "%s" cannot be set' % newState)


    def cancelTimer(self):
        """Cancel any existing timer. 
        """
        if (self.timer):
            self.timer.cancel()
            self.timer = None


    def setTimer(self, newTimer):
        """Cancel any existing timer, and start the specified one. 
        """
        self.cancelTimer()
        self.timer = newTimer
        self.timer.start()


# Getters
    def getName(self):
        return(self.name)


    def getPredecessor(self):
        return(self.predecessor)
    
    
    def getSuccessor(self):
        return(self.successor)


    def getState(self):
        return(self.state)


# Event Handlers
    def updateAspect(self, observable, aspect):
        """
        """
        pass



# Inheritance - Superclass
# Other API Functions
    def sendMessage(self, receiver, messageType):
        """Send a message after a random delay
        """
        if (receiver):
            delay = (random.randint(1, 100) / 1000)
            print('PushSensor %s: Sending %s to %s with delay %s' %(self.name, messageType, receiver.getName(), delay))
            now = datetime.now()
            def send():
                receiver.receiveMessage(self, messageType, now)
            Timer(delay, send).start()
        else:
            print('PushSensor %s: Not sending "%s" because no receiver given' % (self.getName(), messageType))


    def receiveMessage(self, sender, messageType, timestamp):  # @UnusedVariable
        """
        """
        if (not messageType in [PushSensor.MessagePush, PushSensor.MessageContinue, PushSensor.MessageComplete, PushSensor.MessageConfirm]):
                assert False, ('PushSensor %n: Received illegal message type %s' % (self.name, messageType))             
        print('PushSensor %s: Received %s from %s' % (self.name, 
                                                      messageType, 
                                                      sender.getName() if (sender) else 'None'))
        if (self.state == PushSensor.StateIdle):
            if (messageType == PushSensor.MessagePush):
                self.setState(PushSensor.StatePushed)
                if (not self.successor):
                    self.sendMessage(self.predecessor, PushSensor.MessageComplete)
                else:
                    self.sendMessage(self.predecessor, PushSensor.MessageContinue)
            else:
                print('PushSensor %s: Ignoring %s in state %s' % (self.name, messageType, self.state))
        elif (self.state == PushSensor.StatePushed):
            if ((messageType == PushSensor.MessagePush)
                or (messageType == PushSensor.MessageContinue)):
                if (not self.successor): 
                    self.sendMessage(self.predecessor, PushSensor.MessageComplete)
                else:
                    self.sendMessage(self.predecessor, PushSensor.MessageContinue)
            elif (messageType == PushSensor.MessageComplete):
                if (self.predecessor):
                    self.sendMessage(self.predecessor, PushSensor.MessageComplete)
                else:  # no predecessor, this is the first sensor
                    self.setState(PushSensor.StateFinished)
                    self.sendMessage(self.successor, PushSensor.MessageConfirm)
            elif (messageType == PushSensor.MessageConfirm):
                self.setState(PushSensor.StateFinished)
                self.sendMessage(self.successor, PushSensor.MessageConfirm)
        elif (self.state == PushSensor.StateFinished):
            print('PushSensor %s: Ignoring %s in state %s' % (self.name, messageType, self.state))
        else: 
            assert False, ('PushSensor %s: In illegal state %s' % (self.name, self.state))
        if (not (self.successor or self.predecessor)):
            assert False, ('PushSensor %s: Neither successor nor predecessor, where did the %s come from?' % (self.name, messageType))



# Internal - to change without notice
# Class Initialization
pass



# Executable Script
if __name__ == "__main__":
    pass


