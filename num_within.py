# Write a Python function called num_within() to check whether a number falls in a given range.
'''
Function works for Integer numbers only
'''

def num_within(x,a,b):
  return x in range(a,b+1) #<- We need to add 1 to the upper range else the function will not work when passing the same number as the upper limit
     
print(num_within(624,95,700))
