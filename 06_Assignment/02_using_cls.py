class Counter:
    count = 0

    def __init__ (self):
        Counter.count += 1

    @classmethod

    def show_count(cls):
            print(f"Total objects counted {Counter.count}")
c1= Counter()
c2= Counter()
c3= Counter()
Counter.show_count()
