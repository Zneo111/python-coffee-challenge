class Order:
    all_orders = []

    def __init__(self, customer, coffee, price):
        from customer import Customer
        from coffee import Coffee
        if not isinstance(customer, Customer):
            raise ValueError("Invalid customer")
        if not isinstance(coffee, Coffee):
            raise ValueError("Invalid coffee")
        if not isinstance(price, float) or not 1.0 <= price <= 10.0:
            raise ValueError("Price must be 1.0-10.0")

        self._customer = customer
        self._coffee = coffee
        self._price = price
        
        coffee._orders.append(self)
        customer._orders.append(self)
        Order.all_orders.append(self)

    @property
    def price(self):
        return self._price

    @property
    def customer(self):
        return self._customer

    @property
    def coffee(self):
        return self._coffee