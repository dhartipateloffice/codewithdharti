#  location where we can find a variable and also access it if required is called the scope of a variable
# Local: Variables you only need within a function.
# Global: Variables that need to be accessible across different functions.
# Nonlocal: Modifies variables in the nearest enclosing function, ideal for nested functions.
    
def outer_function():
    x = 10

    def inner_function():
        # Without nonlocal, this would create a new local variable x
        x = 20
        print("Inner function:", x)  # Output: Inner function: 20

    inner_function()
    print("Outer function:", x)  # Output: Outer function: 10

    def inner_function_with_nonlocal():
        nonlocal x
        x = 30
        print("Inner function with nonlocal:", x)  # Output: Inner function with nonlocal: 30

    inner_function_with_nonlocal()
    print("Outer function:", x)  # Output: Outer function: 30

outer_function()