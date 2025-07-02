#@property, @settter and @deleter (Private variables)
# @property privae variable ko class ke bahar access krne me help krta he
# @setter private veriabale ki value ko update krta he
#  @deleter ye private veriable ki value ko delete kr de ga
#  getter veriable ko ham class k andar hi access kr sakte hen bahar nhi
# agr hame getter ki value ko update ya set karna he to ham setter ka use kren ge

class Product:
    def __init__(self, price):
        self._price = price
    @property
    def price(self):
        return self._price
    @price.setter
    def price(self, value):
        self._price = value

    @price.deleter
    def price (self):
        del self._price  
    
if __name__ == "__main__":
    p= Product(400)
    print (p.price)
    p.price = 300
    print(p.price)
    del p.price
    print(p.price)








