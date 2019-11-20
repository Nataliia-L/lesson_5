import random
val = ([random.randint (0,9)]*30)
print (val)
print (len (val [::3]))
print ((val [::3]))
val [2::3] = [1000]*10
print (val)
del val[0]
print (val)
