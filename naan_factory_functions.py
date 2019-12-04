# Naan factory functions

# 1.) Make dough function
def make_dough(arg1, arg2):
    if (arg1 == 'water' or arg2 == 'water') and (arg2 == 'flour' or arg1 == 'flour'):
        return 'dough'
    else:
        return 'not dough'


# 2.) Bake dough function
def bake_dough (arg1):
    if arg1 == 'dough':
        return 'naan'
    else:
        return 'not naan'


