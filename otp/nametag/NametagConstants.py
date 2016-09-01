CFNoQuitButton=256
CFPageButton=16
CFQuicktalker=4
CFQuitButton=32
CFReversed=64
CFSndOpenchat=128
CFSpeech=1
CFThought=2
CFTimeout=8

CCNormal = 0
CCNonPlayer = 1
CCSuit = 2
CCToonBuilding = 3
CCSuitBuilding = 4
CCHouseBuilding = 5
CCSpeedChat = 6

NAMETAG_COLORS = {
    CCNormal: (
        # Normal  FG                    BG
        ((0.3, 0.3, 0.7, 1.0), (0.8, 0.8, 0.8, 0.5),  # Name
         (0.0, 0.0, 0.0, 1.0), (1.0, 1.0, 1.0, 1.0)), # Chat
        # Click   FG                    BG
        ((0.3, 0.3, 0.7, 1.0), (0.2, 0.2, 0.2, 0.6),  # Name
         (1.0, 0.5, 0.5, 1.0), (1.0, 1.0, 1.0, 1.0)), # Chat
        # Hover   FG                    BG
        ((0.5, 0.5, 1.0, 1.0), (1.0, 1.0, 1.0, 1.0),  # Name
         (0.0, 0.6, 0.6, 1.0), (1.0, 1.0, 1.0, 1.0)), # Chat
        # Disable FG                    BG
        ((0.3, 0.3, 0.7, 1.0), (0.8, 0.8, 0.8, 0.5),  # Name
         (0.0, 0.0, 0.0, 1.0), (1.0, 1.0, 1.0, 1.0)), # Chat
    ),
    CCNonPlayer: (
        # Normal  FG                    BG
        ((0.8, 0.4, 0.0, 1.0), (0.8, 0.8, 0.8, 0.5),  # Name
         (0.0, 0.0, 0.0, 1.0), (1.0, 1.0, 1.0, 1.0)), # Chat
        # Click   FG                    BG
        ((0.8, 0.4, 0.0, 1.0), (0.8, 0.8, 0.8, 0.5),  # Name
         (0.0, 0.0, 0.0, 1.0), (1.0, 1.0, 1.0, 1.0)), # Chat
        # Hover   FG                    BG
        ((0.8, 0.4, 0.0, 1.0), (0.8, 0.8, 0.8, 0.5),  # Name
         (0.0, 0.0, 0.0, 1.0), (1.0, 1.0, 1.0, 1.0)), # Chat
        # Disable FG                    BG
        ((0.8, 0.4, 0.0, 1.0), (0.8, 0.8, 0.8, 0.5),  # Name
         (0.0, 0.0, 0.0, 1.0), (1.0, 1.0, 1.0, 1.0)), # Chat
    ),
    CCSuit: (
        # Normal  FG                    BG
        ((0.0, 0.0, 0.0, 1.0), (0.8, 0.8, 0.8, 0.5),  # Name
         (0.0, 0.0, 0.0, 1.0), (1.0, 1.0, 1.0, 1.0)), # Chat
        # Click   FG                    BG
        ((0.2, 0.2, 0.2, 1.0), (0.2, 0.2, 0.2, 0.6),  # Name
         (1.0, 0.5, 0.5, 1.0), (1.0, 1.0, 1.0, 1.0)), # Chat
        # Hover   FG                    BG
        ((0.0, 0.0, 0.0, 1.0), (1.0, 1.0, 1.0, 0.7),  # Name
         (0.0, 0.6, 0.6, 1.0), (1.0, 1.0, 1.0, 1.0)), # Chat
        # Disable FG                    BG
        ((0.2, 0.2, 0.2, 1.0), (0.8, 0.8, 0.8, 0.5),  # Name
         (0.0, 0.0, 0.0, 1.0), (1.0, 1.0, 1.0, 1.0)), # Chat
    ),
    CCSuitBuilding: (
        # Normal  FG                    BG
        ((0.5, 0.5, 0.5, 1.0), (0.8, 0.8, 0.8, 0.5),  # Name
         (0.0, 0.0, 0.0, 1.0), (1.0, 1.0, 1.0, 1.0)), # Chat
        # Click   FG                    BG
        ((0.5, 0.5, 0.5, 1.0), (0.2, 0.2, 0.2, 0.6),  # Name
         (1.0, 0.5, 0.5, 1.0), (1.0, 1.0, 1.0, 1.0)), # Chat
        # Hover   FG                    BG
        ((0.7, 0.7, 0.7, 1.0), (1.0, 1.0, 1.0, 0.7),  # Name
         (0.0, 0.6, 0.6, 1.0), (1.0, 1.0, 1.0, 1.0)), # Chat
        # Disable FG                    BG
        ((0.5, 0.5, 0.5, 1.0), (0.8, 0.8, 0.8, 0.5),  # Name
         (0.0, 0.0, 0.0, 1.0), (1.0, 1.0, 1.0, 1.0)), # Chat
    ),
    CCToonBuilding: (
        # Normal  FG                    BG
        ((0.2, 0.6, 0.9, 1.0), (0.8, 0.8, 0.8, 0.5),  # Name
         (0.0, 0.0, 0.0, 1.0), (1.0, 1.0, 1.0, 1.0)), # Chat
        # Click   FG                    BG
        ((0.2, 0.6, 0.9, 1.0), (0.8, 0.8, 0.8, 0.5),  # Name
         (0.0, 0.0, 0.0, 1.0), (1.0, 1.0, 1.0, 1.0)), # Chat
        # Hover   FG                    BG
        ((0.2, 0.6, 0.9, 1.0), (0.8, 0.8, 0.8, 0.5),  # Name
         (0.0, 0.0, 0.0, 1.0), (1.0, 1.0, 1.0, 1.0)), # Chat
        # Disable FG                    BG
        ((0.2, 0.6, 0.9, 1.0), (0.8, 0.8, 0.8, 0.5),  # Name
         (0.0, 0.0, 0.0, 1.0), (1.0, 1.0, 1.0, 1.0)), # Chat
    ),
    CCHouseBuilding: (
        # Normal  FG                    BG
        ((0.2, 0.6, 0.9, 1.0), (0.8, 0.8, 0.8, 0.5),  # Name
         (0.0, 0.0, 0.0, 1.0), (1.0, 1.0, 1.0, 1.0)), # Chat
        # Click   FG                    BG
        ((0.2, 0.2, 0.5, 1.0), (0.2, 0.2, 0.2, 0.6),  # Name
         (1.0, 0.5, 0.5, 1.0), (1.0, 1.0, 1.0, 1.0)), # Chat
        # Hover   FG                    BG
        ((0.5, 0.5, 1.0, 1.0), (1.0, 1.0, 1.0, 1.0),  # Name
         (0.0, 0.6, 0.6, 1.0), (1.0, 1.0, 1.0, 1.0)), # Chat
        # Disable FG                    BG
        ((0.0, 0.6, 0.2, 1.0), (0.8, 0.8, 0.8, 0.5),  # Name
         (0.0, 0.0, 0.0, 1.0), (1.0, 1.0, 1.0, 1.0)), # Chat
    ),
    CCSpeedChat: (
        # Normal  FG                    BG
        ((0.0, 0.6, 0.2, 1.0), (0.8, 0.8, 0.8, 0.5),  # Name
         (0.0, 0.0, 0.0, 1.0), (1.0, 1.0, 1.0, 1.0)), # Chat
        # Click   FG                    BG
        ((0.0, 0.5, 0.0, 1.0), (0.5, 0.5, 0.5, 0.6),  # Name
         (1.0, 0.5, 0.5, 1.0), (1.0, 1.0, 1.0, 1.0)), # Chat
        # Hover   FG                    BG
        ((0.0, 0.7, 0.2, 1.0), (1.0, 1.0, 1.0, 0.7),  # Name
         (0.0, 0.6, 0.6, 1.0), (1.0, 1.0, 1.0, 1.0)), # Chat
        # Disable FG                    BG
        ((0.0, 0.6, 0.2, 1.0), (0.8, 0.8, 0.8, 0.5),  # Name
         (0.0, 0.0, 0.0, 1.0), (1.0, 1.0, 1.0, 1.0)), # Chat
    )
}

ARROW_COLORS = {
    CCSuit: (0.5, 0.5, 0.5, 1.0),
}

DEFAULT_WORDWRAPS = {
    CCNormal: 7.5,
    CCNonPlayer: 7.5,
    CCSuit: 7.5,
    CCToonBuilding: 8.5,
    CCSuitBuilding: 8.5,
    CCHouseBuilding: 10.0,
    CCSpeedChat: 7.5
}

WTNormal = 0
WTQuickTalker = 1
WTSystem = 2
WTBattleSOS = 3
WTEmote = 4
WTToontownBoardingGroup = 5

WHISPER_COLORS = {
    WTNormal: (
        # Normal  FG                    BG
        ((0.0, 0.0, 0.0, 1.0), (0.2, 0.6, 0.8, 0.6)),
        # Click   FG                    BG
        ((1.0, 0.5, 0.5, 1.0), (1.0, 1.0, 1.0, 0.8)),
        # Hover   FG                    BG
        ((0.0, 0.0, 0.0, 1.0), (0.2, 0.7, 0.9, 0.6)),
        # Disable FG                    BG
        ((0.0, 0.0, 0.0, 1.0), (0.2, 0.7, 0.8, 0.6))
    ),
    WTQuickTalker: (
        # Normal  FG                    BG
        ((0.0, 0.0, 0.0, 1.0), (0.2, 0.6, 0.8, 0.6)),
        # Click   FG                    BG
        ((1.0, 0.5, 0.5, 1.0), (1.0, 1.0, 1.0, 0.8)),
        # Hover   FG                    BG
        ((0.0, 0.0, 0.0, 1.0), (0.2, 0.7, 0.9, 0.6)),
        # Disable FG                    BG
        ((0.0, 0.0, 0.0, 1.0), (0.2, 0.7, 0.8, 0.6))
    ),
    WTSystem: (
        # Normal  FG                    BG
        ((0.0, 0.0, 0.0, 1.0), (0.8, 0.3, 0.6, 0.6)),
        # Click   FG                    BG
        ((1.0, 0.5, 0.5, 1.0), (1.0, 1.0, 1.0, 0.8)),
        # Hover   FG                    BG
        ((0.0, 0.0, 0.0, 1.0), (0.8, 0.4, 1.0, 0.6)),
        # Disable FG                    BG
        ((0.0, 0.0, 0.0, 1.0), (0.8, 0.3, 0.6, 0.6))
    ),
    WTBattleSOS: (
        # Normal  FG                    BG
        ((0.0, 0.0, 0.0, 1.0), (0.8, 0.3, 0.6, 0.6)),
        # Click   FG                    BG
        ((1.0, 0.5, 0.5, 1.0), (1.0, 1.0, 1.0, 0.8)),
        # Hover   FG                    BG
        ((0.0, 0.0, 0.0, 1.0), (0.8, 0.4, 0.0, 0.8)),
        # Disable FG                    BG
        ((0.0, 0.0, 0.0, 1.0), (0.8, 0.3, 0.6, 0.6))
    ),
    WTEmote: (
        # Normal  FG                    BG
        ((0.0, 0.0, 0.0, 1.0), (0.9, 0.5, 0.1, 0.6)),
        # Click   FG                    BG
        ((1.0, 0.5, 0.5, 1.0), (1.0, 1.0, 1.0, 0.8)),
        # Hover   FG                    BG
        ((0.0, 0.0, 0.0, 1.0), (0.9, 0.6, 0.2, 0.6)),
        # Disable FG                    BG
        ((0.0, 0.0, 0.0, 1.0), (0.9, 0.6, 0.1, 0.6))
    ),
    WTToontownBoardingGroup: (
        # Normal  FG                    BG
        ((0.0, 0.0, 0.0, 1.0), (0.9, 0.5, 0.1, 0.6)),
        # Click   FG                    BG
        ((1.0, 0.5, 0.5, 1.0), (1.0, 1.0, 1.0, 0.8)),
        # Hover   FG                    BG
        ((0.0, 0.0, 0.0, 1.0), (0.9, 0.6, 0.2, 0.6)),
        # Disable FG                    BG
        ((0.0, 0.0, 0.0, 1.0), (0.9, 0.6, 0.1, 0.6))
    )
}

def getFriendColor(handle):
    return CCNormal if base.localAvatar.isTrueFriends(handle.doId) else CCSpeedChat
