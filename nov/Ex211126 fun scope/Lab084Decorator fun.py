def essential_items(items):
    def wrapper():
        print("1.Before the fun add")
        print("2.Helmet,gloves,n=knee cap,driving Licens,all doc of scooty")
        items()
        print("3.Call After the fun ")
        print("4 Leav all things to its place")
    return wrapper()
@essential_items
def scooty_new():
    print("my scooty")


@essential_items
def scooty_driving():
     print("normalFunction")
     print("I am driving a scooty")
