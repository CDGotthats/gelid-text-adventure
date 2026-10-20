from abc import ABC
from inventory import Inventory

class Actor(ABC, Inventory):
    def __init__(self, actor_id, location_id):
        super().__init__()
        self.actor_id = actor_id
        self.location_id = location_id