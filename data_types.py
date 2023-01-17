''' Python: Variables and Data Types '''

# python is a dynamic language
# means you don't need to declare the variable type when assigning values

# int
x = 42
print(type(x), x)

#string
y = 'Hello World!'
print(type(y), y)

#No Value, None, or Null Value
no_value = None
print(type(no_value), no_value)

# Some helpful REPL methods: type, dir, help

num = 27
# prints out data type of value
print(type(num))


dir(str)
# shows all the methods of type

help(str.split())
# shows documentation for particular type
