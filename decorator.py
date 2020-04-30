def mydec(anyfunc):
    def inner(*val):
        print("This is pre task")
        anyfunc(*val)
        print("The argument values",val, "func name is",anyfunc.__name__)
        print("This is post task")
    return inner

@mydec  # This is linking to decorator so , first decorator will execute
def add(num1 , num2):
    print("This is add function", num1+num2)
    
@mydec
def login(username , password):
    print("login function")

add(10 , 20)
login("harshit", 1234)