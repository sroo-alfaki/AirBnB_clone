#!/usr/bin/python3
"""The cmd Module
"""
import cmd

class HBNBCommand(cmd.Cmd):
    prompt = "(hbnb) "

    def emptyline(self):
        """Do nothing on an empty line or ENTER shouldn’t execute anything"""
    
    def do_EOF(self, line):
        """EOF to exit the program"""
        print()
        return True

    def do_quit(self, line):
        """quit to exit the program"""
        print()
        return True

    def help_quit(self):
        """Help message for the quit command."""
        print("Quit command to exit the program\n")

if __name__ == '__main__':
    HBNBCommand().cmdloop()



