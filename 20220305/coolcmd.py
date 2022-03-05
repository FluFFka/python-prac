import readline
import shlex
import cmd


class repl(cmd.Cmd):
    prompt = '> '
    
    def do_perform(self, arg):
        """
        mmm, docstring
        """
        args = shlex.split(arg, comments=True)
        if args[0] == "sing":
            print("-".join(args[1:]))
        elif args[0] == "show":
            print(" ".join(args[1:]).upper())
        else:
            print(f"Don't know how to {args[0]}")
    
    def complete_perform(self, prefix, allcommand, beg, end):
        return [s for s in ("sing", "show") if s.startswith(prefix)]

    def do_exit(self, arg):
        """Exit command line"""
        return True


repl().cmdloop()
