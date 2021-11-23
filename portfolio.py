class Portfolio:
    def __init__(self):
        self._stocks=[]
    def buy (self, name, shares, price):
        self._stocks.append(name, shares, price) # store info in this list

    def cost(self):
        return sum( shares * price for _, shares, price in self._stocks)
        # _ represents name, which is not used in our calculation