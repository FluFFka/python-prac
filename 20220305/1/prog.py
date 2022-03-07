import readline
import shlex
import cmd

FIELD_SIZE = 10
field = [[0 for i in range(FIELD_SIZE)] for j in range(FIELD_SIZE)]


class Monster:
    def __init__(self, name, hp):
        self.name = name
        self.hp = hp

class Player:
    def __init__(self):
        self.x = 0
        self.y = 0


directions = {'up': [0, 1], 'down': [0, -1], 'left': [-1, 0], 'right': [1, 0]}


class repl(cmd.Cmd):
    prompt = '> '
    def do_add(self, arg):
        args = shlex.split(arg, comments=True)
        if len(args) >= 8 and args[0] == 'monster' and args[1] == 'name' \
                and args[3] == 'hp' and args[5] == 'coords':
            try:
                hp = int(args[4])
                if hp <= 0:
                    raise ValueError
            except Exception:
                print('Number of health points must be a positive integer')
                return
            try:
                x = int(args[6])
                y = int(args[7])
                if not (0 <= x <= 9 and 0 <= y <= 9):
                    raise IndexError
            except Exception:
                print('X and Y must be integer from 0 to 9 (included)')
                return 
            field[x][y] = Monster(args[2], hp)
        else:
            print("Command pattern: add monster name <monster_name> hp <number of health points> coords <X> <Y>")
    
    def complete_add(self, prefix, linef, beg, end):
        line = shlex.split(linef)
        if len(line) == 1:
            return ['monster']
        if not 'monster'.startswith(line[1]):
            return []
        if len(line) <= 2:
            if line[1] == 'monster':
                return ['monster name']
            return ['monster']
        if not 'name'.startswith(line[2]):
            return []
        if len(line) <= 3:
            if line[2] == 'name':
                return []
            return ['name']
        if len(line) <= 4:
            if linef[-1] != ' ':
                return []
            return ['hp']
        if not 'hp'.startswith(line[4]):
            return []
        if len(line) <= 5:
            if line[4] == 'hp':
                return []
            return ['hp']

        if len(line) <= 6:
            if linef[-1] != ' ':
                return []
            return ['coords']
        if not 'coords'.startswith(line[4]):
            return []
        if len(line) <= 5:
            if line[4] == 'coords':
                return []
            return ['coords']
        return []

    def do_show(self, arg):
        args = shlex.split(arg, comments=True)
        if len(args) >= 1 and args[0] == 'monsters':
            for i, ei in enumerate(field):
                for j, ej in enumerate(ei):
                    if type(ej) is Monster:
                        print(f"{ej.name} at ({i} {j}) hp {ej.hp}")
        else:
            print('Command pattern: show monsters')
    def complete_show(self, prefix, line, beg, end):
        if 'monsters'.startswith(prefix):
            return ['monsters']
        print('qwe')
        return []

    def do_move(self, arg):
        args = shlex.split(arg, comments=True)
        if len(args) >= 1 and args[0] in ('up', 'down', 'left', 'right'):
            newx = pl.x + directions[args[0]][0]
            newy = pl.y + directions[args[0]][1]
            if 0 <= newx <= 9 and 0 <= newy <= 9:
                pl.x = newx
                pl.y = newy
                print(f'player at {pl.x} {pl.y}')
            else:
                print('cannot move')
        else:
            print('Command pattern: move <direction>\nDirection must be up, down, left or right')

    def complete_move(self, prefix, line, beg, end):
        available = []
        for dir_name, dirr in directions.items():
            newx = pl.x + dirr[0]
            newy = pl.y + dirr[1]
            if 0 <= newx <= 9 and 0 <= newy <= 9:
                available.append(dir_name)
        return [s for s in available if s.startswith(prefix)]

    def do_exit(self, arg):
        """Exit command line"""
        return True

pl = Player()
repl().cmdloop()