import sys


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
            sys.stderr("cannot pop from enpty list")

    def flip(self):
        self.items = self.items[::-1]

    def operation(self, _type):
        if _type in ["+", "-", "*", "/"]:
            self.push(eval(f"{self.pop()}{_type}{self.pop()}"))
        else:
            sys.stderr(f"invalid operation: {_type}")

    def notequalpush(self, item):
        if self.pop() != self.pop():
            self.push(item)


class Compiler:
    def __init__(self, dump) -> None:
        self.dump = dump

    def compile_file(self, file_name):
        push_mode = False
        op_mode = False
        if_mode = False
        with open(file_name, "r") as file:
            script = file.read()
        with open(self.dump, "w") as file:
            file.write("from brainstack import Stack\n")
            file.write("S = Stack()\n")
            for cmd in script:
                if (not push_mode) and (not op_mode) and (not if_mode):
                    if cmd == "&":
                        file.write("S.push(")
                    elif cmd == "<":
                        push_mode = True
                    elif cmd == "!":
                        file.write("S.notequalpush(")
                    elif cmd == "[":
                        if_mode = True
                    elif cmd == "$":
                        file.write("S.operation(")
                        op_mode = True
                    elif cmd == "*":
                        file.write("print(S.pop())")
                    elif cmd == "?":
                        file.write("S.push(input('>'))")
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
                elif if_mode:
                    if cmd == "]":
                        if_mode = False
                        file.write(")\n")
                    else:
                        file.write(cmd)
