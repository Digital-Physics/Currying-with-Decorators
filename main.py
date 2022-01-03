# Decorators and Currying
# Decorators are "syntactic sugar" for creating "higher order functions" in Python
# Decorators can be helpful for doing things like timing functions or logging
# Here it used to implement "Currying"
# https://www.geeksforgeeks.org/decorators-in-python/
# https://www.themetabytes.com/2017/11/25/currying-in-python-with-decorators/

def curry(func):
    # unpack all arguments, whether an iterable list or arguments or a dictionary with key words and corresponding values
    def curried(*args, **kwargs):
        # if all arguments are passed check
        if len(args)+len(kwargs) >= func.__code__.co_argcount:
            # just return the final result, not an intermediate function
            return func(*args, **kwargs)
        # if only some arguments are passed
        return (lambda *args2, **kwargs2: curried(*(args+args2), **dict(kwargs, **kwargs2)))
    return curried

@curry
def simple_add_func(x,y,z):
    return x+y+z

# this function returns a function that still needs two arguments
partially_completed_function = simple_add_func(11)
print("type:", type(partially_completed_function))

# this function returns a function that still needs one argument
another_partially_completed_function = partially_completed_function(13)
print("type:", type(another_partially_completed_function))

# this function returns the final result
result = another_partially_completed_function(17)

# this wrapper function also allows you to pass more than one argument at a time
another_way_to_get_completed_result = partially_completed_function(13,17)

print("The same result:", result, another_way_to_get_completed_result)

