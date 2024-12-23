class Bird:

    def __init__(self):
        print("bird is ready")

    def __whoisThis__(self):
        print("bird")

    def swim(self):
         print("swim faster")

class penguin(Bird):

    def __init__(self):
        super().__init__()
        print("penguin is ready")

    def whoisThis(self):
        print("penguin")

    def run(self):
         print("run faster")

peggy = penguin()
peggy.whoisThis()
peggy.swim()
peggy.run()          