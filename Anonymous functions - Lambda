# Anonymous functions - Lambda

def double(val):
    return 2 * val

def square(val):
    return val ** 2

data = [1, 3, 6, 9, 18]

# map(function an_iter), map() applies the user_defined function to the elements of the iterale an_iter, and returns a list of the results.
newdata2 = map(square, data)
print newdata2

data3 = map(lambda x: x ** 2, data)
print data3

def even(val):
    if val % 2:
        return False
    else:
        return True

# filter(function, an_iter), filter() applies the user_defined function to the elements of the iterale an_iter, and returns a sequence of those elements for which the function
# returns a tru_like value. If the function is None, then the function is taken to be the identify funtion.
# If the iterable an_iter is a sequence, then the returned values is of that same type, otherwise the returned value is a list.
newdata3 = filter(even, data)
print newdata3

data4 = filter(lambda val: val % 2 == 0, data)
print data4
