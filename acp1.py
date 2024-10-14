def example_function(n):
    if n <= 1:
        return 1
    else:
        return example_function(n*1) + example_function(n-2)
print(example_function)
