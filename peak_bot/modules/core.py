class Core:
    def copy(self, *args):

    def move(self, *args):
        if args[0] and args[1]:
            answer = (' '.join(args[0]), 100)
        else:
            answer = ('Arguments error', 90)
        return(answer)

    def try_printing(self, *args):
        if args[0]:
            answer = (' '.join(args[0]), 100)
        else:
            answer = ('Arguments error', 90)
        return(answer)

    def __init__(self):
        self.try_printing
