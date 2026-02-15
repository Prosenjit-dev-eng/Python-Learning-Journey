# Object types / Data Types
- Number : 1234, 3.14, 3+4j, 0b111, Decimal(),Fraction()
- String : 'spam', "Bob's", b'a\x01c', u'sp\xc4m'
  python treats "" or '' as string
- List : [1, 2, 3], ['spam', 'eggs'], [1, 'two', 3.0],
  [1, [2, 3], 4]
  In list we use square brackets []
- Tuple : (1, 2, 3), ('spam', 'eggs'), (1, 'two', 3.0),
  (1, (2, 3), 4), namedtuple
  In tuple we use round brackets ()
- Dictionary : {'name': 'Bob', 'age': 40}, {1: 'one', 2: 'two'}, dict(name='Bob', age=40)
  - Dictionary is a mutable mapping type
  - It is an unordered collection of key-value pairs
  - Keys are unique and immutable, while values can be of any type
  - Example: {'name': 'Bob', 'age': 40},here key = 'name' and value = 'Bob'
In dictionary we use curly brackets {}
  - Dictionary is a collection of key-value pairs
  - Keys must be unique and immutable (e.g., strings, numbers, tuples)
  - Values can be of any type and can be duplicated
- Set : {1, 2, 3}, {'spam', 'eggs'}, {1, 'two', 3.0},
  {1, (2, 3), 4}
  In set we use curly brackets {}
  - Set is an unordered collection of unique elements
    - It does not allow duplicate values

-file : 'file.txt', open('file.txt', 'r')
  - File is a special type that represents an open file
  - It allows reading from and writing to files on disk
  - Example: open('file.txt', 'r') opens a file for reading

-boolean : True, False
  - Boolean is a data type that can have one of two values: True or False
  - It is often used in conditional statements and logical operations
  - Example: True, False
- None : None
  - None is a special constant that represents the absence of a value or a null value
  - It is often used to indicate that a variable has no value assigned
  - Example: None
- Function : def my_function(): pass, lambda x: x + 1
  - Function is a callable object that can be defined using the def keyword or as a lambda expression
  - It can take parameters and return a value
  - Example: def my_function(): pass, lambda x: x + 1

  -Module : import math, from datetime import datetime
  - Module is a file containing Python code that can be imported and used in other Python programs
  - It can contain functions, classes, and variables
  - Example: import math, from datetime import datetime 

- Class : class MyClass: pass
  - Class is a blueprint for creating objects in Python
  - It can contain attributes (variables) and methods (functions)
  - Example: class MyClass: pass

  -Advance: Decorator, Generator, Iterator, Meta Programming
