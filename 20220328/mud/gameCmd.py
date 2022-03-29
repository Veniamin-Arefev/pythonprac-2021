"""Main cmd logic."""
import cmd
from shlex import split
from sys import platform

from mud.gameObjects import GameObjects

if platform.startswith('linux'):
    import readline # noqaF401
elif platform.startswith('win'):
    import pyreadline3 # noqaF401


class GameCmd(cmd.Cmd):
    """Main cmd class."""

    intro = "Welcome to multi-user dungeon. Type 'help' for quick start."
    prompt = '=>'

    gameObject = GameObjects()

    def do_add(self, arg):
        """Create new mob."""
        args = split(arg)
        if len(args) != 8:
            print('Wrong number of arguments')
        else:
            args[6:] = map(int, args[6:])
            if args[0] == 'monster' and args[1] == 'name' \
                    and args[3] == 'hp' and args[5] == 'coords':
                self.gameObject.monsters[(args[6], args[7])][args[2]] = int(args[4])
            else:
                print('Wrong command syntax')

    def do_show(self, arg):
        """Show ALL the mobs."""
        args = split(arg)
        if len(args) != 1:
            print('Wrong number of arguments')
        else:
            if args[0] != 'monsters':
                print('Wrong command syntax')
            else:
                for coords, monsters in self.gameObject.monsters.items():
                    for monster_name, monster_hp in monsters.items():
                        print(f'{monster_name} at ({coords[0]} {coords[1]}) hp {monster_hp}')

    def do_move(self, arg):
        """Move to another stop."""
        args = split(arg)
        if len(args) != 1:
            print('Wrong number of arguments')
        else:
            if args[0] not in self.gameObject.directions:
                print('Wrong command syntax')
            else:
                if self.gameObject.player_coords.imag == 0 and args[0] == 'up' or \
                        self.gameObject.player_coords.imag == 9 and args[0] == 'down' or \
                        self.gameObject.player_coords.real == 0 and args[0] == 'left' or \
                        self.gameObject.player_coords.real == 9 and args[0] == 'right':
                    print('Cannot move like that')
                else:
                    self.gameObject.player_coords += self.gameObject.directions[args[0]]
                    print(f'Now player at ({self.gameObject.player_coords.real} {self.gameObject.player_coords.imag})')
                    if (mobs := self.gameObject.monsters[self.gameObject.player_coords.real,
                                                         self.gameObject.player_coords.imag]):
                        mobs = [f'{monster_name} {monster_hp} hp' for monster_name, monster_hp in mobs.items()]
                        print('Encountered:\n', "\n  ".join(mobs), sep='  ')

    def do_attack(self, arg):
        """Attack mob in current stop."""
        args = split(arg)
        if len(args) != 1:
            print('Wrong number of arguments')
        else:
            if args[0] in (mobs := self.gameObject.monsters[self.gameObject.player_coords.real,
                                                            self.gameObject.player_coords.imag]):
                mobs[args[0]] -= 10
                if mobs[args[0]] <= 0:
                    del mobs[args[0]]
                    print(f'{args[0]} dies')
                else:
                    print(f'{args[0]} lost 10 hp, now has {mobs[args[0]]} hp')
            else:
                print(f'No {args[0]} here')

    def do_exit(self, arg):
        """Stop."""
        return True

    def do_EOF(self, arg):
        """Just exit by ^D."""
        self.do_exit(arg)
        return True

    def complete_add(self, text: str, line: str, begidx, endidx):
        """Add completion for add."""
        args = split(line)
        arg_count = len(args)
        if arg_count == 1 or len(split(line)) == 2 and text != '':
            return list(filter(lambda x: x.startswith(text), ['monster']))
        elif arg_count == 2 or len(split(line)) == 3 and text != '':
            return list(filter(lambda x: x.startswith(text), ['name']))
        elif arg_count == 4 or len(split(line)) == 5 and text != '':
            return list(filter(lambda x: x.startswith(text), ['hp']))
        elif arg_count == 6 or len(split(line)) == 7 and text != '':
            return list(filter(lambda x: x.startswith(text), ['coords']))
        else:
            return []

    def complete_show(self, text: str, line: str, begidx, endidx):
        """Add completion for show."""
        arg_count = len(split(line))
        if arg_count == 1 or len(split(line)) == 2 and text != '':
            return list(filter(lambda x: x.startswith(text), ['monsters']))

    def complete_move(self, text: str, line: str, begidx, endidx):
        """Add completion for move."""
        return list(filter(lambda x: x.startswith(text), self.gameObject.directions))

    def complete_attack(self, text: str, line: str, begidx, endidx):
        """Add completion for attack."""
        return list(
            filter(lambda x: x.startswith(text), self.gameObject.monsters[self.gameObject.player_coords.real,
                                                                          self.gameObject.player_coords.imag]))


if __name__ == '__main__':
    GameCmd().cmdloop()
