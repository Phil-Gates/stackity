import sys
import argparse
import logging

logger = logging.getLogger(__name__)

logging.basicConfig(level=logging.ERROR)


class _ArgumentParser(argparse.ArgumentParser):
    """Custom error message."""

    def error(self, message):
        """Custom error message."""
        self.print_help()
        logger.exception(f"\n{message}\n")


Parser = _ArgumentParser(
    description="Brainstack: stack based esoteric programming language."
)


def _parse_args():
    """Nicer than doing it at start of code."""
    Parser.add_argument("-r", "--run", type=str, help="code to run")
    Parser.add_argument(
        "-d", "--dump", required=True, help="place to dump compiled code (required)"
    )
    Parser.add_argument("-f", "--file", type=str, help="filename to run")
    return Parser.parse_args()


class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        try:
            self.items.append(item.replace("&gt;", ">"))
        except AttributeError:
            self.items.append(item)

    def pop(self):
        try:
            return self.items.pop()
        except IndexError:
            pass

    def copy(self):
        top_val = self.pop()
        self.push(top_val)
        self.push(top_val)

    def flip(self):
        self.items = self.items[::-1]

    def move(self, index):
        self.push(self.items.pop(index))

    def operation(self, _type):
        if _type in ["+", "-", "*", "/"]:
            self.push(eval(f"{self.pop()}{_type}{self.pop()}"))
        else:
            logger.exception(f"invalid operation: {_type}")


class Compiler:
    def __init__(self, dump) -> None:
        self.dump = dump

    def compile(self, script):
        tabs = ""
        push_mode = False
        op_mode = False
        mv_mode = False
        with open(self.dump, "w") as file:
            file.write("from brainstack import Stack\n")
            file.write("S = Stack()\n")
            for cmd in script:
                if (not push_mode) and (not op_mode) and (not mv_mode):
                    if cmd == "&":
                        file.write(tabs + "S.push(")
                    elif cmd == "<":
                        push_mode = True
                    elif cmd == "#":
                        file.write(tabs + "S.move(")
                    elif cmd == "{":
                        mv_mode = True
                    elif cmd == "!":
                        file.write(tabs + "while S.pop() != 0:\n")
                    elif cmd == "[":
                        tabs += "\t"
                    elif cmd == "]":
                        tabs = tabs[:-1]
                    elif cmd == "$":
                        file.write(tabs + "S.operation(")
                        op_mode = True
                    elif cmd == "*":
                        file.write(tabs + "print(S.pop(), end='')\n")
                    elif cmd == ".":
                        file.write("S.pop()\n")
                    elif cmd == "?":
                        file.write(tabs + "while True:\n")
                        file.write(tabs + "\t" + "try:\n")
                        file.write(tabs + "\t\t" + "S.push(int(input('>')))\n")
                        file.write(tabs + "\t\t" + "break\n")
                        file.write(tabs + "\t" + "except ValueError:\n")
                        file.write(tabs + "\t\t" + "print('Invalid input.')\n")
                    elif cmd == "%":
                        file.write(tabs + "S.copy()\n")
                    elif cmd == "@":
                        file.write(tabs + "S.flip()\n")
                elif push_mode:
                    if cmd == ">":
                        push_mode = False
                        file.write(")\n")
                    else:
                        file.write(cmd)
                elif op_mode:
                    file.write('"' + cmd + '"')
                    file.write(")\n")
                    op_mode = False
                elif mv_mode:
                    if cmd == "}":
                        mv_mode = False
                        file.write(")\n")
                    else:
                        file.write(cmd)

    def compile_file(self, file_name):
        with open(file_name, "r") as file:
            script = file.read()
        self.compile(script)


if __name__ == "__main__":
    args = _parse_args()
    if len(sys.argv) > 1:
        C = Compiler(args.dump)
        if args.file:
            C.compile_file(args.file)
        elif args.run:
            C.compile(args.run)
    else:
        Parser.error("no flags provided")
