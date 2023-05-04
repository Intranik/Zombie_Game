from __future__ import annotations
class Room :
    def __init__(self, name):
        self.name = name
        self.toNorth = None
        self.toSouth = None
        self.toWest = None
        self.toEast = None
        self.toNorthWest = None
        self.toNorthEast = None
        self.toSouthWest = None
        self.toSouthEast = None

    def setRoomToTheNorth(self, room: Room) :
        self.toNorth = room
    def setRoomToTheSouth(self, room: Room) :
        self.toSouth = room
    def setRoomToTheWest(self, room: Room) :
        self.toWest = room
    def setRoomToTheEast(self, room: Room) :
        self.toEast = room
    def setRoomToTheNorthWest (self, room: Room) :
        self.toNorthWest = room
    def setRoomToTheNorthEast (self, room: Room) :
        self.toNorthEast = room
    def setRoomToTheSouthWest (self, room: Room) :
        self.toSouthWest = room
    def setRoomToTheSouthEast (self, room: Room) :
        self.toSouthEast = room
 
    def getName(self) :
        return self.name
    def getRoomToTheNorth(self) :
        return self.toNorth
    def getRoomToTheSouth(self) :
        return self.toSouth
    def getRoomToTheWest(self) :
        return self.toWest
    def getRoomToTheEast(self) :
        return self.toEast
    def getRoomToTheNorthWest (self) :
        return self.toNorthWest
    def getRoomToTheNorthEast (self) :
        return self.toNorthEast
    def getRoomToTheSouthWast (self) :
        return self.toSouthWest
    def getRoomToTheSouthEast (self) :
        return self.toSouthEast