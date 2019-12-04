# Basis of a test
# you'll be testing functions or methods, these need to be called or initilised
# having controlled inputs for known outputs
    # and testing for these


def make_dough(arg1, arg2):
    pass

def bake_dough (arg1):
    pass


# Make test for make_dough
# Using the ingredient 'water' and 'flour' to make dough.
print("testing make_dough with 'water' and 'flour'. Expecting --> 'dough'")
print(make_dough('water','flour') == 'dough')
print('got:',make_dough('water','flour') == 'dough')


# Make test for bake_dough
# Baking the 'dough' in the oven to produce 'naan'.
print("testing bake_dough with 'dough'. Expecting --> 'naan'")
print(bake_dough('dough') == 'naan')
print('got:',bake_dough('dough') == 'naan')

