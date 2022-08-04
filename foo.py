class Foo:

    def __init__(self):
        self.__bar = 42

def public_method():
    print("I'm public")

def _private_method():
    print("I'm private")