import random
import string
num = random.randint(10,20)
a = (random.sample(string.hexdigits,num))
b = ("".join (a))
print ("Password:  ", b)
