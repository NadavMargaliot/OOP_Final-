class Pokemons:
    def __init__(self, data: dict) -> None:
        self.value = data['value']
        self.type = int(data['type'])
        xyz = str(data['pos']).split(',')
        self.pos = []
        for n in xyz:
            print(n)
            self.pos.append(float(n))
        self.src = None
        self.dest = None
