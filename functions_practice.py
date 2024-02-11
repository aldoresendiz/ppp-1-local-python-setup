def hello():
    print("Hello World!")

def pack(arg1, arg2, arg3):
    lista = [arg1, arg2, arg3]
    return(lista)

def eat_lunch(my_list):
    if not my_list:
        print("My luchbox is empty!")
    else:
        for i in range(len(my_list)):
            if i == 0: 
                salida = "First "
            else:
                salida = "Next "
            salida += "I eat " + my_list[i]
            print(salida)

print(hello())
print("\n")
print(pack("1","2","3"))
print("\n")
print(eat_lunch([]))
print("\n")
print(eat_lunch(["Ham", "Bacon", "Chorizo"]))