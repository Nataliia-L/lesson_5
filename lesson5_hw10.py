import random
val = str (random.randint (0,9))
val2 = (list (val*30))
print ("Current list: ", "".join(val2)) 
val2[2] = str (1000)
print ("New list: ", "".join(val2))
