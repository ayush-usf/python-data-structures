# commas which tell Python something is a tuple
# brackets are added for readability
currencies = (1, 75)
currencies = 1, 75

# Adding brackets around a single number doesn't turn it into a tuple.
a = (20)
print(type(a))    # <class 'int'>