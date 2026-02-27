# ==============================================================================
# PYTHON HOMEWORK SOLUTIONS
# ==============================================================================

# ------------------------------------------------------------------------------
# SECTION 1: THEORY QUESTIONS (Answers in Comments)
# ------------------------------------------------------------------------------

# 1. What do you mean by Indention?
# Indentation refers to the spaces or tabs at the beginning of a code line. 
# In Python, it is used to define a block of code.

# 2. Why is indentation required?
# Python uses indentation to indicate which statements belong to a specific 
# block of code. Improper indentation results in an IndentationError.

# 3. What do you mean by Control statements?
# Control statements control the flow of execution of a program based on logic.
# Examples: if, for, while, break, continue.

# 4. What do you mean by Decision making statement?
# These statements allow the program to choose different paths of execution 
# based on whether a condition is True or False.

# 5. Explain different type of decision making statements?
# - if: Runs a block if true.
# - if-else: Runs one block if true, another if false.
# - if-elif-else: Checks multiple conditions.
# - nested if: An if inside another if.

# 6. Explain If statement, syntax with example?
# Syntax:
# if condition:
#     # code
# Example: x = 10; if x > 5: print("Big")

# 7. Explain If-else statement, syntax with example?
# Syntax: if condition: # code \n else: # code
# Example: if x > 5: print("Big") else: print("Small")

# 8. Explain If-elif-else statement, syntax with example?
# Example: if score >= 90: print("A") elif score >= 80: print("B") else: print("C")

# 9. Explain nested If-else statement, syntax with example?
# Example: if num >= 0: \n if num == 0: print("Zero") \n else: print("Pos") \n else: print("Neg")

# 10. What do you mean by Iteration statements?
# Loops used to execute a block of code repeatedly as long as a condition is met.

# 11. Loop Explanations
# - While loop: Repeats while condition is True.
# - For loop: Iterates over a sequence (list, range, etc.).
# - range(): Generates numbers (e.g., range(5) is 0,1,2,3,4).
# - else with loop: Runs after loop ends naturally.

# 12. Break and Continue
# - Break: Exits the loop completely.
# - Continue: Skips current iteration.

# 13. What do you mean by Functions?
# A reusable block of code that performs a specific task.

# 14. Why do we need functions?
# For code reusability and modularity.

# 15. Types of Functions
# - Built-in: (print, input). - User-defined: Created using 'def'.

# 16. How we declare a function?
# Using 'def function_name():'

# 17. How we Call a function?
# Using 'function_name()'

# 18. Returning a value
# Using the 'return' keyword.

# 19. Scope or lifetime of variables
# - Local: Inside function. - Global: Outside function.

# 20. Global variables
# Variables defined outside functions.

# 21. Nonlocal variables
# Used in nested functions to refer to outer scope variables.

# 22. Passing collections
# Passing list/dict to functions like: def func(data):

# 23. Types of arguments
# Positional, Keyword, Default, and Variable-length.

# 24. Variable length argument
# Uses *args or **kwargs.

# 25. Nested functions
# A function inside another function.

# 26. Recursive functions
# A function that calls itself.

# 27. Pass functions to a function
# Functions can be passed as arguments.

# 38. Local vs Global
# Local is internal to function; Global is external.

# 39. Parameter vs Argument
# Parameter is name in def; Argument is value passed.

# 40. Three iterable objects
# List, Tuple, String.

# 41. Default return
# None.

# ------------------------------------------------------------------------------
# SECTION 2: PROGRAMMING TASKS (Active Python Code)
# ------------------------------------------------------------------------------

import math

# 30. Return sum, sub, and multiplication
def calculate_all(a, b):
    return a + b, a - b, a * b

# 31. Student presence check
def check_presence(roll_number):
    # Mock database
    present_students = [10, 15, 20, 25]
    if roll_number in present_students:
        return "Student is Present"
    else:
        return "Student is Absent"

# 32. Max of three
def max_of_three(a, b, c):
    return max(a, b, c)

# 33. Even or Odd
def identify_even_odd(n):
    if n % 2 == 0:
        return "Even"
    else:
        return "Odd"

# 34. Count vowels and consonants
def word_stats(word):
    vowels = "aeiouAEIOU"
    v = 0
    c = 0
    for char in word:
        if char.isalpha():
            if char in vowels:
                v += 1
            else:
                c += 1
    return v, c

# 35. Factorial
def factorial(n):
    if n < 0: return "Not possible"
    if n == 0: return 1
    return n * factorial(n - 1)

# 36. Lower to Upper
def convert_to_upper(s):
    return s.upper()

# 37. Area of Circle
def circle_area(r):
    return math.pi * (r**2)

# 42. Factorial using if-else
def fact_if_else(n):
    if n < 0:
        return "Invalid"
    elif n == 0 or n == 1:
        return 1
    else:
        result = 1
        for i in range(1, n + 1):
            result *= i
        return result

# 43. Reverse a number
def reverse_digits(n):
    return int(str(n)[::-1])

# 44. N natural numbers descending
def print_descending(n):
    print(f"Descending from {n}: ", end="")
    while n > 0:
        print(n, end=" ")
        n -= 1
    print()

# 45. First 7 multiples of 7
def multiples_of_7():
    print("First 7 multiples of 7: ", end="")
    for i in range(1, 8):
        print(i * 7, end=" ")
    print()

# 46. Square list
def square_elements(nums):
    return [x**2 for x in nums]

# 47. Separate positive and negative
def separate_nums(nums):
    pos = [x for x in nums if x >= 0]
    neg = [x for x in nums if x < 0]
    return pos, neg

# 48. Filter even and odd
def filter_even_odd(nums):
    evens = [x for x in nums if x % 2 == 0]
    odds = [x for x in nums if x % 2 != 0]
    return evens, odds

# 49. Prime check
def is_prime(n):
    if n < 2: return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0: return False
    return True

# 50. Pythagorean Triplets
def find_triplets(limit):
    triplets = []
    for a in range(1, limit):
        for b in range(a, limit):
            c_sq = a**2 + b**2
            c = int(c_sq**0.5)
            if c**2 == c_sq and c <= limit:
                triplets.append((a, b, c))
    return triplets

# --- TESTING THE FUNCTIONS ---
if __name__ == "__main__":
    print("Testing Function 30 (Sum, Sub, Multi):", calculate_all(10, 5))
    print("Testing Function 35 (Factorial of 5):", factorial(5))
    print_descending(5)
    multiples_of_7()
