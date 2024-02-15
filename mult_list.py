# Write a Python function called mult_list() to multiply all the numbers in a list.
def mult_list(my_list):
    if not len(my_list):
        return 0
    prod = my_list[0]
    if len(my_list) > 1:
        for i in my_list[1:]:
            prod = prod * i
    print(prod)

mult_list([1,2,3,4,5,6])
