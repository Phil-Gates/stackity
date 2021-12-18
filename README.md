# stackity #
A stack based esoteric programming language (so original!)

# Commands #
`<`: pushes whatever comes after it to the stack

<br>

`>`: stops pushing whatver comes after `<` to the stack

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

`$`: start operation mode; will perform operation on top values of stack (+, -, *, /)

<br>

`*`: do a 'loud' pop; displays top val on stack

<br>

`.`: 'quiet' pop; pops stack

<br>

`?`: ask for input

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
python stackity.py -r "<'Hello, World&wow;'>*" -d "hellowrld.py"
```
(run "hellowrld.py" to use)

<br>

`truth-machine` in stackity:
```
python stackity.py -r "?%[%*%]*" -d "tm.py"
```
(run "tm.py" to use)

<br>

`99 bottles of beer` in stackity:
```
python stackity.py -f "99b.st" -d "99b.py"
```
(run "99b.py" to use)
