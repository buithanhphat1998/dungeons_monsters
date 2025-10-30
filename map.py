

class Map:
    """
    Attributes: 
    <<class var>> _instance: Map
    <<class var>> _initialize: boolean
    _map = char [][]
    _revealed: boolean [][]"""

    _instance = None
    _initialized = False
    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self):
        if not Map._initialized:
            self._map = []
            self._revealed = [[False for _ in range(5)] for _ in range(5)]
            with open("map.txt") as file:
                while True:
                    line = file.readline().strip()
                    if(len(line) == 0):
                        break
                    letters = []
                    for letter in line:
                        letters.append(letter)
                    self._map.append(letters)
            Map._initialized = True

    def __getitem__(self,row):
        return self._map[row]

    def __len__(self):
        return len(self._map)
    
    def reveal(self,loc):
        self._revealed[loc[0]][loc[1]] = True
    
    def show_map(self,loc):
        str = ""
        for row in range(len(self._map)):  
            for col in range(len(self._map[0])):
                if (loc[0] == row and loc[1] == col):
                    str+= '*'
                elif(not self._revealed[row][col]):
                    str += 'x'
                else:
                    str += self._map[row][col]
            str+= '\n'
        return str
    
    def remove_at_loc(self,loc):
        self._map[loc[0]][loc[1]] = 'n'