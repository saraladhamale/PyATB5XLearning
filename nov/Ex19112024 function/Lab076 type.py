from email.policy import default


def type_fun():#no argument fun
    print('hello')
type_fun()


def type1_fun(name):
    print("hello",name)
type1_fun("sarala")#with argument fun




def type2_fun(name="sarala"):#positional arg and default
    print("helle",name.upper())
type2_fun("dhamale") #it is default value difine by user



def multi_arg(name1="A",name2="B"):#multiple arguments with no return
    print("hello",name1,name2)
multi_arg("Dhamale")
multi_arg("lucky","sharma")#it is by default
multi_arg(name2="sarala")


#arg with return type
def arg_return(a,b):
    return a+b
    sum= arg_return(40,50)
print(sum)





