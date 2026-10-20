class Inventory:
    def __init__(self):
        self.inventory = []
    
    def add_item(self, item):       self.inventory.append(item)
    def has_item(self, item_id):    return item_id in [item.name for item in self.inventory]
    def __len__(self):              return len(self.inventory)

    def _find_item(self, item_id):
        if self.has_item(item_id):
            return [item.name for item in self.inventory].index(item_id)
        else:
            return -1
    def get_item(self, item_id):
        item_index = self._find_item(item_id)
        if item_index != -1:
            return self.inventory[item_index]
    def pop_item(self, item_id):
        item_index = self._find_item(item_id)
        if item_index != -1:
            return self.inventory.pop(item_index)
    def remove_item(self, item_id):
        self.pop_item(item_id)