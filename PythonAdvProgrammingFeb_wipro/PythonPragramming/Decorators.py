#wrapper fun around the functions are called decorators

def make_pretty(fun):
    def inner():
        print("I got decorated")
        fun()
    return inner

@make_pretty
def vanillacake():
    print("I am the vanilla cale")

@make_pretty
def staraberrcake():
    print("Ian the starberry cake")

vanillacake()
staraberrcake()