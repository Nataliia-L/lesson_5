import string
t0 = dir(string)
t = t0 [-5:]
print ("This is TUPLE: ", tuple (t))
print ("This is LIST: ",list (t))
t.insert (2,"capwords")
print ("The result is: ", tuple (t))
