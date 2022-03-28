import readline     # noqa: F401
import shlex
import cmd

FIELD_SIZE = 10
field = [[[] for i in range(FIELD_SIZE)] for j in range(FIELD_SIZE)]


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
            for i in range(len(field[x][y])):
                if field[x][y][i].name == args[2]:
                    field[x][y][i].hp = hp
                    break
            else:
                field[x][y].append(Monster(args[2], hp))
        else:
            print("Command pattern: add monster name <monster_name> hp <number_of_health_points> coords <X> <Y>")

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
                    if len(ej) > 1:
                        for monster in ej:
                            print(f"{monster.name} at ({i} {j}) hp {monster.hp}")
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
                if len(field[pl.x][pl.y]) > 0:
                    out = []
                    for monster in field[pl.x][pl.y]:
                        out.append(f'{monster.name} {monster.hp} hp')
                    print(f'encountered: {", ".join(out)}')
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

    def do_attack(self, arg):
        args = shlex.split(arg, comments=True)
        if len(args) >= 1:
            for i, monster in enumerate(field[pl.x][pl.y]):
                if monster.name == args[0]:
                    if monster.hp - 10 > 0:
                        field[pl.x][pl.y][i].hp -= 10
                        print(f"{monster.name} lost 10 hp, now has {field[pl.x][pl.y][i].hp} hp")
                    else:
                        print(f"{monster.name} dies")
                        field[pl.x][pl.y].remove(monster)
                    break
            else:
                print(f'no {args[0]} here')
        else:
            print('Command pattern: attack <monster_name>')

    def complete_attack(self, prefix, line, beg, end):
        ret = [s.name for s in field[pl.x][pl.y] if s.name.startswith(prefix)]
        for i in range(len(ret)):
            if len(ret[i].split()) > 1:
                ret[i] = '"' + ret[i] + '"'
        return ret

    def do_exit(self, arg):
        """Exit command line"""
        return True


pl = Player()
repl().cmdloop()
