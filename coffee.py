class Coffee:
    all_coffees = []

    def __init__(self, name):
        self._name = None
        self.name = name
        self._orders = []
        Coffee.all_coffees.append(self)

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if not isinstance(value, str):
            raise ValueError("Name must be a string")
        if len(value) < 3:
            raise ValueError("Name must be ≥3 characters")
        if self._name is not None:
            raise AttributeError("Coffee name is immutable")
        self._name = value

    def orders(self):
        return self._orders.copy()

    def customers(self):
        return list({order.customer for order in self._orders})

    def num_orders(self):
        return len(self._orders)

    def average_price(self):
        if not self._orders:
            return 0.0
        return sum(order.price for order in self._orders) / len(self._orders)