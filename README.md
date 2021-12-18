# stackity #
A stack based esoteric programming language (so original!)

# Commands #
`<`: pushes whatever comes after it to the stack
<br>
`>`: stops pushing whatver comes after `>` to the stack
<br>
`<`: pushes whatever comes after it to the stack
<br>
`{`: start collecting index to move to top of stack (indexes start at zero and work up from bottom)
<br>
`}`: stop collecting index
<br>
`[`: start a `while` loop that keeps going until the value popped from the stack is zero
<br>
`]`: end the contents inside the loop
<br>
`#`: convert top value on stack to an ascii character if it is an int; if not, raise an error
<br>
`$`: start operation mode. will preform operation on top values of stack (+, -, *, /)
<br>
`*`: do a 'loud' pop; displays top val on stack
<br>
`.`: 'quiet' pop; pops stack
<br>
`?`: ask for input. prompted by '>'
<br>
`%`: copy the top value of the stack to the top
<br>
`@`: flip the stack

# Compilation #
Use `-d` to specify dump file.
<br>
Use `-r` to run the code after the `-r`
<br>
Use `-f` to specify file to compile

# Examples #
`Hello, World!` in stackity:
```
python3 stackity.py -r "<'Hello, World!'>*" -d "dump.py"
```
(run "dump.py" to use)
<br>
`truth-machine` in stackity:
```
python3 stackity.py -r "?%[%*%]*" -d dump.py
```
(run "dump.py" to use)
