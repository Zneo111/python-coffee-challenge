class Customer:
    all_customers = []

    def __init__(self, name):
        self._name = None
        self.name = name
        self._orders = []
        Customer.all_customers.append(self)

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if not isinstance(value, str):
            raise ValueError("Name must be a string")
        if not 1 <= len(value) <= 15:
            raise ValueError("Name must be 1-15 characters")
        self._name = value

    def create_order(self, coffee, price):
        from order import Order  # moved import here to avoid circular import
        order = Order(self, coffee, price)
        self._orders.append(order)
        return order

    def orders(self):
        return self._orders.copy()

    def coffees(self):
        return list({order.coffee for order in self._orders})

    @classmethod
    def most_aficionado(cls, coffee):
        if not coffee.orders():
            return None
            
        spenders = {}
        for order in coffee.orders():
            customer = order.customer
            spenders[customer] = spenders.get(customer, 0) + order.price
                
        return max(spenders.items(), key=lambda x: x[1])[0]