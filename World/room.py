from Engine.game_directions import Directions
from inventory import Inventory

class Link:
    def __init__(self, direction, destination):
        self.direction:Directions = direction
        self.destination = destination

class Node:
    def __init__(self):
        self.links:list[Link] = []
    def add_link(self, link): self.links.append(link)
    def has_link(self, direction): return direction in [link.direction for link in self.links]
    def find_link(self, direction):
        if self.has_link(direction):
            return [link.direction for link in self.links].index(direction)
        else:
            return -1

class Room(Inventory, Node):
    def __init__(self, room_id):
        super().__init__()
        self.room_id = room_id