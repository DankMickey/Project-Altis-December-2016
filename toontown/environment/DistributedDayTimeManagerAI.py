from panda3d.core import *
from direct.distributed.ClockDelta import *
from direct.interval.IntervalGlobal import *
from direct.distributed import DistributedObject
from direct.directnotify import DirectNotifyGlobal
from direct.fsm import ClassicFSM
from direct.fsm import State
from direct.task.Task import Task
from toontown.toonbase import TTLocalizer
import random
import time
from direct.showbase import PythonUtil
import DayTimeGlobals
from DistributedWeatherMGRAI import DistributedWeatherMGRAI

class DistributedDayTimeManagerAI(DistributedWeatherMGRAI):
    notify = directNotify.newCategory('DistributedDayTimeManagerAI')
    
    def __init__(self, air):
        DistributedWeatherMGRAI.__init__(self, air)
        self.air = air
        self.interval = 150
        self.currentHour = 0

    def start(self):
        DistributedWeatherMGRAI.start(self)
        
        # start the ticking process
        taskMgr.doMethodLater(self.interval, self.tick, 'time-update')

    def tick(self, task):
        if self.currentHour >= 23:
            # reset current time back to 0
            self.currentHour = 0
        
        # update the AI's current time.
        self.air.setHour(self.currentHour)
        
        # send time update to change sky state
        self.sendUpdate('update', [self.currentHour])
        
        # loop task preserving the timeout interval
        return task.again
    
    def stop(self):
        taskMgr.remove('time-update')


