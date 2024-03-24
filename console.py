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

        def do_create(self, line):
            """Creates a new instance of BaseModel, saves it (to the JSON file)"""
            args = line.split()
            if not args:
                print("** class name missing **")
                return

            try:
                class_name = args[0]
                item = self.CLASSES[class_name]()
                item.save()
                print(item.id)

            except ImportError:
                print("** class doesn't exist **")

        def do_show(self, line):
            """Prints the string representation of an instance based on the class name and id."""
            args = line.split()
            if not args:
                print("** class name missing **")
            
            elif args[0] not in self.CLASSES:
                print("** class doesn't exist **")
            
            elif len(args) < 2:
                print("** instance id missing **")
            
            else:
                key = "{}.{}".format(args[0], args[1])
                if key not in storage.all():
                    print("** no instance found **")
                else:
                    print(storage.all()[key])


if __name__ == '__main__':
    HBNBCommand().cmdloop()
