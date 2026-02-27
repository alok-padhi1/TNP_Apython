# Python Homework Solutions

## Theory Questions (1-27, 38-41)

### 1. What do you mean by Indentation?
Indentation refers to the spaces or tabs at the beginning of a code line. In Python, it is used to define a block of code (like loops, functions, or classes).

### 2. Why is indentation required?
Python uses indentation to indicate which statements belong to a specific block of code. Improper indentation will result in an `IndentationError`.

### 3. What do you mean by Control statements?
Control statements are used to control the flow of execution of a program based on certain conditions or logic. Examples include `if`, `for`, `while`, `break`, and `continue`.

### 4. What do you mean by Decision making statement?
Decision-making statements allow the program to choose different paths of execution based on whether a condition is `True` or `False`.

### 5. Explain different type of decision making statements?
- `if`: Executes a block if the condition is true.
- `if-else`: Executes one block if true, another if false.
- `if-elif-else`: Checks multiple conditions in sequence.
- `nested if`: An `if` statement inside another `if` statement.

### 6. Explain If statement, syntax with example?
**Syntax:**
```python
if condition:
    # code
```
**Example:**
```python
x = 10
if x > 5:
    print("Greater than 5")
```

### 7. Explain If-else statement, syntax with example?
**Syntax:**
```python
if condition:
    # true block
else:
    # false block
```
**Example:**
```python
x = 3
if x > 5:
    print("Greater than 5")
else:
    print("5 or less")
```

### 8. Explain If-elif-else statement, syntax with example?
**Syntax:**
```python
if cond1:
    # block 1
elif cond2:
    # block 2
else:
    # block 3
```
**Example:**
```python
score = 85
if score >= 90:
    print("A")
elif score >= 80:
    print("B")
else:
    print("C")
```

### 9. Explain nested If-else statement, syntax with example?
**Example:**
```python
num = 10
if num >= 0:
    if num == 0:
        print("Zero")
    else:
        print("Positive")
else:
    print("Negative")
```

### 10. What do you mean by Iteration statements?
Iteration statements (loops) are used to execute a block of code repeatedly as long as a condition is met.

### 11. Loop Explanations
- **While loop**: Repeats as long as a condition is True.
- **While loop with else**: The `else` block runs when the loop condition becomes False.
- **For loop**: Iterates over a sequence (list, tuple, string).
- **range()**: Generates a sequence of numbers.
- **For loop with else**: The `else` block runs after the loop finishes naturally (not via `break`).
- **Nested loops**: A loop inside another loop.

### 12. Break and Continue
- **Break**: Terminates the loop immediately.
- **Continue**: Skips the current iteration and jumps to the next one.

### 13. What do you mean by Functions?
A function is a reusable block of code that performs a specific task.

### 14. Why do we need functions?
Functions help in code reusability, modularity, and making the code easier to read and maintain.

### 15. Types of Functions
- **Built-in**: Already provided by Python (e.g., `print()`, `len()`).
- **User-defined**: Created by the programmer using `def`.

### 16. How we declare a function?
Using the `def` keyword:
```python
def my_function():
    print("Hello")
```

### 17. How we Call a function?
By using its name followed by parentheses:
```python
my_function()
```

### 18. Returning a value
Using the `return` keyword:
```python
def add(a, b):
    return a + b
```

### 19. Scope or lifetime of variables
- **Local scope**: Variables defined inside a function (only accessible there).
- **Global scope**: Variables defined outside functions (accessible everywhere).

### 20. Global variables
Created outside functions. To modify them inside a function, use the `global` keyword.

### 21. Nonlocal variables
Used in nested functions to refer to variables in the outer (non-global) scope. Use the `nonlocal` keyword.

### 22. Passing collections
You can pass lists, dictionaries, etc., as arguments to functions.

### 23. Types of arguments
- **Positional**: order matters.
- **Keyword**: identified by name.
- **Default**: have a fallback value.
- **Variable-length**: `*args` (tuple) and `**kwargs` (dictionary).

### 24. Variable length argument
```python
def show_args(*args):
    for arg in args:
        print(arg)
```

### 25. Nested functions
A function defined inside another function.
```python
def outer():
    def inner():
        print("Inner")
    inner()
```

### 26. Recursive functions
A function that calls itself. 
- **Adv**: Clean code for math problems. 
- **Disadv**: High memory usage, risk of stack overflow.

### 27. Pass functions to a function
Functions are first-class objects in Python, so they can be passed as arguments.

---

### 38. Local vs Global variable
Local variables exist only inside the function they are defined in. Global variables exist throughout the program.

### 39. Parameter vs Argument
A **parameter** is the variable listed in the function definition. An **argument** is the actual value passed to the function when calling it.

### 40. Three iterable objects
List, Tuple, String.

### 41. What does function return by default?
`None`.

---

## Programming Tasks (30-37, 42-50)

```python
# 30. Sum, sub and multiplication
def calc(a, b):
    return a + b, a - b, a * b

# 31. Roll number presence
present_students = [1, 5, 10, 15]
def check_presence(roll):
    return "Present" if roll in present_students else "Absent"

# 32. Max of three
def max_of_three(a, b, c):
    return max(a, b, c)

# 33. Even or Odd
def even_odd(n):
    return "Even" if n % 2 == 0 else "Odd"

# 34. Vowels and Consonants
def count_v_c(word):
    vowels = "aeiouAEIOU"
    v = sum(1 for char in word if char in vowels and char.isalpha())
    c = sum(1 for char in word if char not in vowels and char.isalpha())
    return v, c

# 35. Factorial
def factorial(n):
    if n == 0 or n == 1: return 1
    return n * factorial(n - 1)

# 36. Lower to Upper
def to_upper(word):
    return word.upper()

# 37. Area of Circle
import math
def circle_area(radius):
    return math.pi * (radius ** 2)

# 42. Factorial using if-else
def fact_if_else(n):
    res = 1
    if n < 0: return "Error"
    elif n == 0: return 1
    else:
        for i in range(1, n + 1):
            res *= i
        return res

# 43. Reverse a number
def reverse_num(n):
    return int(str(n)[::-1])

# 44. N natural numbers descending
def print_descending(n):
    while n > 0:
        print(n, end=" ")
        n -= 1

# 45. First 7 multiples of 7
def mult_7():
    for i in range(1, 8):
        print(i * 7, end=" ")

# 46. Square list
def square_list(nums):
    squares = []
    for n in nums:
        squares.append(n**2)
    return squares

# 47. Separate pos and neg
def separate_pos_neg(nums):
    pos = [n for n in nums if n >= 0]
    neg = [n for n in nums if n < 0]
    return pos, neg

# 48. Filter even and odd
def filter_even_odd(nums):
    evens = [n for n in nums if n % 2 == 0]
    odds = [n for n in nums if n % 2 != 0]
    return evens, odds

# 49. Prime check
def is_prime(n):
    if n < 2: return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0: return False
    return True

# 50. Pythagorean Triplets
def pythagorean_triplets(limit):
    triplets = []
    for a in range(1, limit):
        for b in range(a, limit):
            c_sq = a**2 + b**2
            c = int(c_sq**0.5)
            if c**2 == c_sq and c <= limit:
                triplets.append((a, b, c))
    return triplets
```
