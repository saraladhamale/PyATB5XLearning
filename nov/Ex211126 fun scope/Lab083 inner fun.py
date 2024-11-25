def outer_fun():
    var1=30
    print(var1)
    def inner_fun():
     print(var1)#outer fun variable use in inner

    def inner_fun2():
     print(var1)
     inner_fun()
     inner_fun2()
outer_fun()
#inner_fun can not out of fun
