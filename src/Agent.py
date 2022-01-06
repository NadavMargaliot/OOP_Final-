class Agent:
    def __init__(self, data: dict) -> None:
        self.id = int(data['id'])
        self.value = float(data['value'])
        self.src = int(data['src'])
        self.dest = int(data['dest'])
        self.speed = float(data['speed'])
        location = str(data['pos']).split(',')
        self.pos = [float(location[0]),float(location[1]),float(location[2])]
        self.path = []




