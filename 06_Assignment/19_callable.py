#  yeahan ham sekhen ge k object ko callable kese banate hen
# ia k lye method __call__ ka istemal krte hen jo object ko function ki tarha callable bana deta he

class Multiplier:
    def __init__(self, factor):
        self.factor = factor

    def __call__(self, value):
        return self.factor * value
    

if __name__ == "__main__":

    m = Multiplier(4)
    print("Result:  " , m(10))
