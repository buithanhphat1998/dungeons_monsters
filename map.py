class Map:
    """
    Singleton class representing the dungeon map.
    
    Attributes: 
    <<class var>> _instance: Map
        The single instance of the Map class (Singleton pattern).
    <<class var>> _initialized: boolean
        Tracks whether the Map instance has been initialized.
    _map: char[][]
        2D list representing the dungeon layout, where each character represents a specific tile.
    _revealed: boolean[][]
        2D list tracking which tiles have been revealed to the player.
    """

    _instance = None
    _initialized = False
    def __new__(cls):
        """
        Ensures only one instance of the Map class is created (Singleton pattern).
        """
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self):
        """
        Initializes the Map instance by loading the dungeon layout from a file and setting up the revealed tiles.
        """
        if not Map._initialized:
            self._map = []  # 2D list to store the dungeon layout
            # Initialize the revealed tiles as a 5x5 grid
            self._revealed = [[False for _ in range(5)] for _ in range(5)]
            # Load the dungeon layout from "map.txt"
            with open("map.txt") as file:
                while True:
                    line = file.readline().strip() # Read each line and strip whitespace
                    if(len(line) == 0):  # Stop reading if an empty line is encountered
                        break
                    letters = [] # Temporary list to store characters in the line
                    for letter in line:
                        letters.append(letter) # Add each character to the list
                    self._map.append(letters) # Add the list of characters as a new row in the map
            Map._initialized = True # Mark the instance as initialized

    def __getitem__(self,row):
        """
        Allows indexing into the map to retrieve a specific row.

        Args:
            row (int): The index of the row to retrieve.

        Returns:
            list: The row at the specified index.
        """
        return self._map[row]

    def __len__(self):
        """
        Returns the number of rows in the map.

        Returns:
            int: The number of rows in the map.
        """
        return len(self._map)
    
    def reveal(self,loc):
        """
        Marks a specific location on the map as revealed.

        Args:
            loc (tuple): A tuple (row, col) representing the location to reveal.
        """
        self._revealed[loc[0]][loc[1]] = True
    
    def show_map(self,loc):
        """
        Generates a string representation of the map, showing revealed tiles and the hero's current location.

        Args:
            loc (tuple): A tuple (row, col) representing the hero's current location.

        Returns:
            str: The string representation of the map.
        """
        str = ""  # Initialize an empty string
        for row in range(len(self._map)):  # Iterate through each row in the map
            for col in range(len(self._map[0])): # Iterate through each column in the row
                if (loc[0] == row and loc[1] == col): # Mark the hero's current location
                    str+= '*'
                elif(not self._revealed[row][col]): # Unrevealed tiles are shown as 'x'
                    str += 'x'
                else:
                    str += self._map[row][col]
            str+= '\n' # Add a newline after each row
        return str
    
    def remove_at_loc(self,loc):
        """
        Removes an item or entity at a specific location by setting the tile to 'n' (empty).

        Args:
            loc (tuple): A tuple (row, col) representing the location to modify.
        """
        self._map[loc[0]][loc[1]] = 'n'