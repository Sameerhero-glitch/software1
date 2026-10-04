class Player:
    def __init__(self, name):
        self.name = name
        self.items = []
        self.location = None

    def move(self, room):
        self.location = room

    def collect_item(self):
        if self.location.item is not None:
            item = self.location.item
            self.items.append(item)
            self.location.item = None
            print("You collected:", item.name)
        else:
            print("There is no item here.")