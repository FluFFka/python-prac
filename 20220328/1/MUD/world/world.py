"""World for multi-user dungeon."""

directions = {'up': [0, 1], 'down': [0, -1], 'left': [-1, 0], 'right': [1, 0]}


class Monster:
    """Monster in the world."""

    def __init__(self, name, hp):
        """Initiate name and hp for monster."""
        self.name = name
        self.hp = hp


class Player:
    """Player in the world."""

    def __init__(self):
        """
        Initiate player in the world.

        Place him in (0, 0).
        """
        self.x = 0
        self.y = 0


class World:
    """Game world."""

    def __init__(self):
        """
        Initiate game world.

        Add player and field.
        """
        self.pl = Player()
        self.FIELD_SIZE = 10
        self.field = [[[] for i in range(self.FIELD_SIZE)] for j in range(self.FIELD_SIZE)]

    def add_monster(self, name, hp, x, y):
        """Add monster in field."""
        if not (0 <= x <= 9 or 0 <= y <= 9):
            raise IndexError
        for i in range(len(self.field[x][y])):
            if self.field[x][y][i].name == name:
                self.field[x][y][i].hp = hp
                break
        else:
            self.field[x][y].append(Monster(name, hp))

    def show_monsters(self):
        """Show all monster in the world."""
        for i, ei in enumerate(self.field):
            for j, ej in enumerate(ei):
                if len(ej) > 1:
                    for monster in ej:
                        print(f"{monster.name} at ({i} {j}) hp {monster.hp}")

    def move(self, direction):
        """Try to move player in suggested direction."""
        if not (direction in ('up', 'down', 'left', 'right')):
            raise AttributeError
        newx = self.pl.x + directions[direction][0]
        newy = self.pl.y + directions[direction][1]
        if not (0 <= newx <= 9 and 0 <= newy <= 9):
            raise IndexError
        self.pl.x = newx
        self.pl.y = newy
        print(f'player at {self.pl.x} {self.pl.y}')
        if len(self.field[self.pl.x][self.pl.y]) > 0:
            out = []
            for monster in self.field[self.pl.x][self.pl.y]:
                out.append(f'{monster.name} {monster.hp} hp')
            print(f'encountered: {", ".join(out)}')

    def attack(self, name):
        """Try to attack monster in player's cell."""
        for i, monster in enumerate(self.field[self.pl.x][self.pl.y]):
            if monster.name == name:
                if monster.hp - 10 > 0:
                    self.field[self.pl.x][self.pl.y][i].hp -= 10
                    print(f"{monster.name} lost 10 hp, now has {self.field[self.pl.x][self.pl.y][i].hp} hp")
                else:
                    print(f"{monster.name} dies")
                    self.field[self.pl.x][self.pl.y].remove(monster)
                break
        else:
            print(f'no {name} here')
