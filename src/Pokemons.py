from src.DiGraph import DiGraph
class Pokemons:
    def __init__(self, data: dict) -> None:
        self.value = data['value']
        self.type = int(data['type'])
        location = str(data['pos']).split(',')
        self.pos = [float(location[0]),float(location[1]),float(location[2])]
        self.src = None
        self.dest = None




