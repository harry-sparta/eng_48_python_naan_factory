# Here we run the factory functions
from naan_factory_functions import *

# Call the functions of the naan factory
print('########## Welcome to the naan factory ##########')

produce_1 = input('What is the first produce?')
produce_2 = input('Second produce?')

output_1 = make_dough(produce_1,produce_2)
final_output = bake_dough(output_1)

print('########## Well done! You made some: ', final_output, '##########')
