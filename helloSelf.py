class Me:
    def __init__(self, name):
        self.name = name

    def sayHello(self):
        print(f"Hello, {self.name}!")


me = Me("Doraemon")
me.sayHello()
