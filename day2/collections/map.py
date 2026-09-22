# Map is not a collection its a python function
#lamba is an simple expression one line expression.
#custom variable is the variable name that is our choice
#and map iterates each values in the list and assigns the current iteration value to the customvariable and prefrom the operation
#after performing the operation it stores the result in the mapp variable given
#so in one line it just preform an operation with an iteratable set or list and stores it in the variable given
set1 = [10, 20, 30, 40]
mapp=map(lambda customvariable:customvariable+2, set1)
print(list(mapp))