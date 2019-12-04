# Basis of a test
# you'll be testing functions or methods, these need to be called or initilised
# having controlled inputs for known outputs
    # and testing for these


def make_dough(arg1, arg2):
    if (arg1 == 'water' or arg2 == 'water') and (arg2 == 'flour' or arg1 == 'flour'):
        return 'dough'
    else:
        return 'not dough'


def bake_dough (arg1):
    if arg1 == 'dough':
        return 'naan'
    else:
        return 'not naan'


# 1.) Make test for make_dough
# Using the ingredient 'water' and 'flour' to make dough.
print("1.) testing make_dough with 'water' and 'flour'. Expecting --> 'dough'")
print(' ',make_dough('flour','water') == 'dough')
print(' ','When calling make_dough, got:',make_dough('water','flour'))

# 2.) When I pass in cement and water, or anything else... I should get: 'not dough'
print("\n2.) testing make_dough with other ingredients other than the required. Expecting --> 'not dough'")
print(' ', make_dough('water','cement') == 'not dough')
print(' ','When calling make_dough, got:',make_dough('cement','water'))


# 3.) Make test for bake_dough
# Baking the 'dough' in the oven to produce 'naan'.
print("3.) testing bake_dough with 'dough'. Expecting --> 'naan'")
print(' ',bake_dough('dough') == 'naan')
print(' ','When calling bake_dough, got:',bake_dough('dough'))

# 4.) When bake_dough is passed something other than 'dough' it should output 'Not naan'
print("\n 4.) testing bake_dough with 'not dough'. Expecting --> 'not naan'")
print(' ',bake_dough('chicken') == 'not naan')
print(' ','When calling bake_dough, got:',bake_dough('chicken'))