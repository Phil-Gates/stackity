import sys
import argparse
import logging
from typing import Any

logger = logging.getLogger(__name__)

logging.basicConfig(level=logging.ERROR)


class _ArgumentParser(argparse.ArgumentParser):
    """Custom error message."""

    def error(self, message):
        """Custom error message."""
        self.print_help()
        logger.exception(f"\n{message}\n")


Parser = _ArgumentParser(
    description="stackity: stack based esoteric programming language."
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
    """Storage for the program."""

    def __init__(self) -> None:
        """
        Initialize variables.
        self.items: list version of stack
        """
        self.items = []

    def push(self, item: Any) -> None:
        """Push an item to the stack."""
        try:
            self.items.append(item.replace("&gt;", ">"))
        except AttributeError:
            self.items.append(item)

    def pop(self) -> Any:
        """Take an item from the stack and return it."""
        try:
            return self.items.pop()
        except IndexError:
            logger.exception("cannot pop from empty list")

    def copy(self) -> None:
        """Copy the current top of stack on top of itself."""
        top_val = self.pop()
        self.push(top_val)
        self.push(top_val)

    def flip(self) -> None:
        """Flip the stack."""
        self.items = self.items[::-1]

    def move(self, index: int) -> None:
        """Move index specified to top of stack. (index starts from bottom [0])"""
        try:
            self.push(self.items.pop(index))
        except ValueError:
            logger.exception(f"invalid index for move: {index}")

    def toascii(self) -> None:
        """Converts top value of stack to a character."""
        try:
            using = self.pop()
            self.push(chr(using))
        except TypeError:
            logger.exception(f"invalid type for converting to char: {using}")

    def operation(self, _type: str) -> None:
        """Preform an operation on first two items on stack. (+, -, *, /)"""
        try:
            if _type in ["+", "-", "*", "/"]:
                first = self.pop()
                second = self.pop()
                if isinstance(first, str) and isinstance(second, str):
                    self.push(eval(f"'{first}'{_type}'{second}'"))
                else:
                    self.push(eval(f"{first}{_type}{second}"))
            else:
                logger.exception(f"invalid operation: {_type}")
        except SyntaxError:
            logger.exception(f"cannot preform operation '{_type}'")


class Compiler:
    """Store dump for compilation and compile."""

    def __init__(self, dump: str) -> None:
        """
        Get dump loc..
        self.dump: dump loc.
        """
        self.dump = dump

    def compile(self, script: str) -> None:
        """Compile a stackity script to the dump."""
        tabs = ""
        push_mode = False
        op_mode = False
        mv_mode = False
        with open(self.dump, "w") as file:
            file.write("from stackity import Stack\n")
            file.write("S = Stack()\n")
            for cmd in script:
                if (not push_mode) and (not op_mode) and (not mv_mode):
                    if cmd == "<":
                        file.write(tabs + "S.push(")
                        push_mode = True
                    elif cmd == "{":
                        file.write(tabs + "S.move(")
                        mv_mode = True
                    elif cmd == "[":
                        file.write(tabs + "while S.pop() != 0:\n")
                        tabs += "\t"
                    elif cmd == "]":
                        tabs = tabs[:-1]
                    elif cmd == "#":
                        file.write(tabs + "S.toascii()\n")
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
                    file.write("'" + cmd + "'")
                    file.write(")\n")
                    op_mode = False
                elif mv_mode:
                    if cmd == "}":
                        mv_mode = False
                        file.write(")\n")
                    else:
                        file.write(cmd)

    def compile_file(self, file_name: str) -> None:
        """Compile a file."""
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