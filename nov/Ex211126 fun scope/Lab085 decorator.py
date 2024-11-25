def add_before_UI_after_UI(func):
    def wrapper():
        print("1. Before the running UI")
        print("2. Start the browser")
        func()#call main fun
        print("3.Fter the running Ui")
        print("4. Quit the browser")
    return wrapper()
@add_before_UI_after_UI#call decorator
def test_ui():
        print("i will test the ui")
