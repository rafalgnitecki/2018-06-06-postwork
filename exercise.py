'''
Poniżej znajduje się implementacja CLI (command line interface) do modułu
turtle, czyli Pythonowego odpowiednika LOGO. Wykorzystano tutaj wzorzec Template
Method (metoda szablonowa).
W pierwszym, obowiązkowym zadaniu, należy dodać wsparcie dla makr, tak aby można
było nagrać ciąg komend, a następnie odtworzyć ten sam ciąg przy pomocy
komendy "playback". W tym celu, należy dodać następujące komendy:
- record -- rozpoczyna nagrywanie makra
- stop -- kończy nagrywanie makra
- playback -- wykonuje makro, tzn. wszystkie komendy po komendzie "record", aż
  do komendy "stop".
Podpowiedź: Użyj wzorca Command (polecenie).
W drugim, nieobowiązkowym zadaniu, zastanów się, jak można zastosować wzorzec
Composite (kompozyt) do tych makr i spróbuj zastosować go.
Rozwiązania wysyłamy tak samo, jak prework, tylko że w jednym Pull Requeście.
'''

import cmd, sys
import turtle


class Command:
    def execute(self): pass


class TurtleCommand(Command):
    def __init__(self, command, arg):
        self.command = command
        self.arg = arg

    def execute(self):
        if self.arg:
            self.command(self.arg)
        else:
            self.command()


class Macro:
    def __init__(self):
        self.commands = []

    def add(self, command):
        self.commands.append(command)

    def play(self):
        for command in self.commands:
            command.execute()


class TurtleShell(cmd.Cmd):
    intro = 'Welcome to the turtle shell.   Type help or ? to list commands.\n'
    prompt = '(turtle) '
    _macro = Macro()
    _record_commands = False

    # ----- basic turtle commands -----
    def do_forward(self, arg):
        'Move the turtle forward by the specified distance:  FORWARD 10'
        if self._record_commands:
            self._macro.add(TurtleCommand(turtle.forward, arg))
        else:
            turtle.forward(int(arg))
    def do_right(self, arg):
        'Turn turtle right by given number of degrees:  RIGHT 20'
        if self._record_commands:
            self._macro.add(TurtleCommand(turtle.right, arg))
        else:
            turtle.right(int(arg))
    def do_left(self, arg):
        'Turn turtle left by given number of degrees:  LEFT 90'
        if self._record_commands:
            self._macro.add(TurtleCommand(turtle.left, arg))
        else:
            turtle.left(int(arg))
    def do_home(self, arg):
        'Return turtle to the home position:  HOME'
        if self._record_commands:
            self._macro.add(TurtleCommand(turtle.home, arg))
        else:
            turtle.home()
    def do_circle(self, arg):
        'Draw circle with given radius an options extent and steps:  CIRCLE 50'
        if self._record_commands:
            self._macro.add(TurtleCommand(turtle.circle, arg))
        else:
            turtle.circle(int(arg))
    def do_position(self, arg):
        'Print the current turtle position:  POSITION'
        print('Current position is %d %d\n' % turtle.position())
    def do_heading(self, arg):
        'Print the current turtle heading in degrees:  HEADING'
        print('Current heading is %d\n' % (turtle.heading(),))
    def do_reset(self, arg):
        'Clear the screen and return turtle to center:  RESET'
        turtle.reset()
    def do_bye(self, arg):
        'Close the turtle window, and exit:  BYE'
        print('Thank you for using Turtle')
        turtle.bye()
        return True

    def do_record(self, arg):
        print('Recording commands')
        self._record_commands = True

    def do_stop(self, arg):
        print('Stopped recording commands')
        self._record_commands = False

    def do_playback(self, arg):
        self._macro.play()


if __name__ == '__main__':
    TurtleShell().cmdloop()
