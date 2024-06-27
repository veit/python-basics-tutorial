from collections import namedtuple

Customer = namedtuple("Customer", "name loyalty")


class Product:
    def __init__(self, product, quantity, price):
        self.product = product
        self.quantity = quantity
        self.price = price

    def total(self):
        return self.price * self.quantity


class Order:
    """The context class."""

    def __init__(self, customer, cart, promotion=None):
        self.customer = customer
        self.cart = list(cart)
        self.promotion = promotion

    def total(self):
        if not hasattr(self, "__total"):
            self.__total = sum(item.total() for item in self.cart)
        return self.__total

    def due(self):
        if self.promotion is None:
            discount = 0
        else:
            discount = self.promotion(self)
        return self.total() - discount

    def __repr__(self):
        fmt = "<Order total: {:.2f} due: {:.2f}>"
        return fmt.format(self.total(), self.due())

    def loyalty_promo(order):
        """5% discount for customers with 1000 or more loyalty points."""
        return order.total() * 0.05 if order.customer.fidelity >= 1000 else 0

    def quantity_item_promo(order):
        """10% discount for each LineItem with 10 or more units."""
        discount = 0
        for item in order.cart:
            if item.quantity >= 10:
                discount += item.total() * 0.1
        return discount

    def bulk_promo(order):
        """7% discount for orders with 10 or more distinct items."""
        distinct_items = {item.product for item in order.cart}
        if len(distinct_items) >= 10:
            return order.total() * 0.07
        return 0


promos = [globals()[name] for name in globals() if name.endswith("_promo")]
