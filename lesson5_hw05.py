import random
val1 = random.randint (100,999)
val2 = random.randint (100,999)
val3 = random.randint (100,999)
l = ([val1,val2,val3])
print ("Your list is: ", sorted(l))
print ("Your reversed list is: ", sorted(l, reverse = True))
