from actor import Actor

class Player(Actor):
    def __init__(self, actor_id, location_id):
        super().__init__(actor_id, location_id)