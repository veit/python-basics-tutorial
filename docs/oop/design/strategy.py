from abc import ABC, abstractmethod
from collections import namedtuple

Customer = namedtuple("Customer", "loyalty")


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
            discount = self.promotion.discount(self)
        return self.total() - discount

    def __repr__(self):
        fmt = "<Order total: {:.2f} due: {:.2f}>"
        return fmt.format(self.total(), self.due())


class Promotion(ABC):
    """The abstract strategy class."""

    @abstractmethod
    def discount(self, order):
        """Return discount"""


class LoyaltyPromo(Promotion):
    """First concrete Strategy

    5% discount for customers with 1000 or more loyalty points.
    """

    def discount(self, order):
        return order.total() * 0.05 if order.customer.loyalty >= 1000 else 0


class QuantityItemPromo(Promotion):
    """Second concrete Strategy.

    10% discount for each Product with 10 or more units.
    """

    def discount(self, order):
        discount = 0
        for item in order.cart:
            if item.quantity >= 10:
                discount += item.total() * 0.1
        return discount


class BulkPromo(Promotion):
    """Third concrete Strategy

    7% discount for orders with 10 or more distinct items.
    """

    def discount(self, order):
        distinct_items = {item.product for item in order.cart}
        if len(distinct_items) >= 10:
            return order.total() * 0.07
        return 0


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
            discount = self.promotion.discount(self)
        return self.total() - discount

    def __repr__(self):
        fmt = "<Order total: {:.2f} due: {:.2f}>"
        return fmt.format(self.total(), self.due())


class Promotion(ABC):
    """The abstract strategy class."""

    @abstractmethod
    def discount(self, order):
        """Return discount"""


class LoyaltyPromo(Promotion):
    """First concrete Strategy

    5% discount for customers with 1000 or more loyalty points.
    """

    def discount(self, order):
        return order.total() * 0.05 if order.customer.loyalty >= 1000 else 0


class QuantityItemPromo(Promotion):
    """Second concrete Strategy.

    10% discount for each Product with 10 or more units.
    """

    def discount(self, order):
        discount = 0
        for item in order.cart:
            if item.quantity >= 10:
                discount += item.total() * 0.1
        return discount


class BulkPromo(Promotion):
    """Third concrete Strategy

    7% discount for orders with 10 or more distinct items.
    """

    def discount(self, order):
        distinct_items = {item.product for item in order.cart}
        if len(distinct_items) >= 10:
            return order.total() * 0.07
        return 0


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
            discount = self.promotion.discount(self)
        return self.total() - discount

    def __repr__(self):
        fmt = "<Order total: {:.2f} due: {:.2f}>"
        return fmt.format(self.total(), self.due())
