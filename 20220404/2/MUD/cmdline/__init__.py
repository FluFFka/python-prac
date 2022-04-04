"""Command line for multi-user dungeon."""

import readline     # noqa: F401
import shlex
import cmd
import MUD.world


class Repl(cmd.Cmd):
    """
    Command line.

    Support commands: add, show, move, attack, exit.
    """

    prompt = '> '

    def __init__(self):
        """Inititate command line and world inside."""
        super().__init__()
        self.world = MUD.world.world.World()

    def do_add(self, arg):
        """
        Command add.

        Parse arguments and add monster to world.
        """
        args = shlex.split(arg, comments=True)
        if len(args) >= 8 and args[0] == 'monster' and args[1] == 'name' \
                and args[3] == 'hp' and args[5] == 'coords':
            try:
                hp = int(args[4])
                if hp <= 0:
                    raise ValueError
            except Exception:
                print('qwe')
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
            self.world.add_monster(args[2], hp, x, y)
        else:
            print("Command pattern: add monster name <monster_name> hp <number_of_health_points> coords <X> <Y>")

    def complete_add(self, prefix, linef, beg, end):
        """Auto complete for command add."""
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
        """
        Command show.

        Parse arguments and show all monsters in the world.
        """
        args = shlex.split(arg, comments=True)
        if len(args) >= 1 and args[0] == 'monsters':
            self.world.show_monsters()
        else:
            print('Command pattern: show monsters')

    def complete_show(self, prefix, line, beg, end):
        """Auto complete for command show."""
        if 'monsters'.startswith(prefix):
            return ['monsters']
        return []

    def do_move(self, arg):
        """
        Command move.

        Parse arguments and move player in the world.
        """
        args = shlex.split(arg, comments=True)
        if len(args) >= 1 and args[0] in ('up', 'down', 'left', 'right'):
            try:
                self.world.move(args[0])
            except IndexError:
                print('cannot move')
        else:
            print('Command pattern: move <direction>\nDirection must be up, down, left or right')

    def complete_move(self, prefix, line, beg, end):
        """Auto complete for command move."""
        available = []
        for dir_name, dirr in MUD.world.world.directions.items():
            newx = self.world.pl.x + dirr[0]
            newy = self.world.pl.y + dirr[1]
            if 0 <= newx <= 9 and 0 <= newy <= 9:
                available.append(dir_name)
        return [s for s in available if s.startswith(prefix)]

    def do_attack(self, arg):
        """
        Command attack.

        Parse arguments and attack monster in player's cell.
        """
        args = shlex.split(arg, comments=True)
        if len(args) >= 1:
            self.world.attack(args[0])
        else:
            print('Command pattern: attack <monster_name>')

    def complete_attack(self, prefix, line, beg, end):
        """Auto complete for command attack."""
        ret = [s.name for s in self.world.field[self.world.pl.x][self.world.pl.y] if s.name.startswith(prefix)]
        for i in range(len(ret)):
            if len(ret[i].split()) > 1:
                ret[i] = '"' + ret[i] + '"'
        return ret

    def do_exit(self, arg):
        """Exit command line."""
        return True
