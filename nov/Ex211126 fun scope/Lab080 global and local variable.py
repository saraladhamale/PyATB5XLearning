sd_global_a = 10 #global variable
#print(sd_global_a)
def my_fun():
    sd_local_b = 20# local variable
    print(sd_global_a)
    print(sd_local_b)
my_fun()
print(sd_global_a) #global variable u can call anywhere
#print(sd_local_b) , local variable u can call only within fun