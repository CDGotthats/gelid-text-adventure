from enum import Flag

class ActorFlags(Flag):
    NONE =          0
    VISIBLE =       1 << 0
    TAKEABLE =      1 << 1
    OPENABLE =      1 << 2
    IS_OPEN =       1 << 3
    INVENTORY =     1 << 4
    LIGHT =         1 << 5

class RoomFlags(Flag):
    NONE =          0
    VISITED =       1 << 0
    LIGHT =         1 << 1
    COLD =          1 << 2