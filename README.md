# stackity #
A stack based esoteric programming language (so original!)

# Commands #
`<`: pushes whatever comes after it to the stack; when using newlines, use a triple quoted string

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

`(`: start an `if` that pops the stack and if it is zero, execute code after it

<br>

`)`: stop executing code from `(` and start an else

<br>

`|`: stop the else block that `)` began

<br>

`_`: equivalent to `pass` in Python; use in `if-else` block where you don't need part of it eg. `($+)_|`

<br>

`#`: convert top value on stack to an ascii character if it is an int; if not, raise an error

<br>

`&`: convert top value on stack to an int if it is a char; if not, raise an error

<br>

`$`: start operation mode; will perform operation on top values of stack (+, -, *, /, %)

<br>

`*`: do a 'loud' pop; displays top val on stack

<br>

`.`: 'quiet' pop; pops stack

<br>

`?`: ask for input (then turns to int)

<br>

`~`: ask for input (stored as str)

<br>

`%`: copy the top value of the stack to the top

<br>

`@`: flip the stack

<br>

`x`: start defining a function called x (pops stack twice and stores in `a` and `b` can be pushed with `<a>` or `<b>`) / call a function (just type `x`)

<br>

`X`: stop defining a function; anything after is considered a call to the function

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

<br>

`FizzBuzz` in stackity:
```
python stackity.py -f "fizzbuzz.st" -d "fizzbuzz.py"
```
(run "fizzbuzz.py" to use)

<br>

`Calculator` in stackity: (first num, second num, operation)
```
python stackity.py -f "calc.st" -d "calc.py"
```
(run "calc.py" to use)
