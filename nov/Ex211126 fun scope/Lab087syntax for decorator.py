def decorator_1(fun):
    def wrapper():
        print("this is code for start ")
        print("start")
        fun()
        print("this is for end")
        print("end")
        fun()
        print("this is for end ")
        print("end ")
    return wrapper
def decorator_2(fun):
    def wrapper():
        print("this is code for start 1")
        print("start 1")
        fun()
        print("this is for end 1")
        print("end 1")
    return wrapper
@decorator_1
@decorator_2
def test():
    print("hello i am tester")
test()


