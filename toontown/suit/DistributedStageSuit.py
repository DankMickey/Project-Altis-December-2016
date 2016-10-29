from toontown.suit import DistributedFactorySuit
from toontown.suit.Suit import *
from direct.directnotify import DirectNotifyGlobal
from direct.actor import Actor
from otp.avatar import Avatar
import SuitDNA
from toontown.toonbase import ToontownGlobals
from pandac.PandaModules import *
from toontown.battle import SuitBattleGlobals
from direct.task import Task
from toontown.battle import BattleProps
from toontown.toonbase import TTLocalizer
import string

class DistributedStageSuit(DistributedFactorySuit.DistributedFactorySuit):
    notify = DirectNotifyGlobal.directNotify.newCategory('DistributedStageSuit')

    def setCogSpec(self, spec):
        self.spec = spec
        self.setPos(spec['pos'])
        self.setH(spec['h'])
        self.originalPos = spec['pos']
        self.escapePos = spec['pos']
        self.pathEntId = spec['path']
        self.behavior = spec['behavior']
        self.skeleton = spec['skeleton']
        self.boss = spec['boss']
        self.revives = spec.get('revives')
        if self.reserve:
            self.reparentTo(hidden)
        else:
            self.doReparent()
			
    def renameBoss(self):
        if self.getSkeleRevives() > 0:
            nameInfo = TTLocalizer.SuitBaseNameWithLevel % {'name': TTLocalizer.DistrictAttorney,
             'dept': self.getStyleDept(),
             'level': '%s%s' % (self.getActualLevel(), TTLocalizer.SkeleRevivePostFix)}
            self.setName(TTLocalizer.DistrictAttorney)
            self.setDisplayName(nameInfo)
        else:
            nameInfo = TTLocalizer.SuitBaseNameWithLevel % {'name': TTLocalizer.DistrictAttorney,
             'dept': self.getStyleDept(),
             'level': self.getActualLevel()}
            self.setName(TTLocalizer.DistrictAttorney)
            self.setDisplayName(nameInfo)
