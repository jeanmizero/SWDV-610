class Robot:
    """Represents a robot, with a name."""

    # A class variable, counting the number of robots
    population = 0

    def __init__(self, name):
        """Initializes the data."""
        self.name = name
        print("(Initializing {})".format(self.name))

        # When this person is created, the robot
        # adds to the population
        Robot.population += 1

    def die(self):
        """I am dying."""
        print("{} is being destroyed!".format(self.name))

        Robot.population -= 1

        if Robot.population == 0:
            print("{} was the last one.".format(self.name))
        else:
            print("There are still {:d} robots working.".format(
                Robot.population))

    def say_hi(self):
        """Greeting by the robot.

        Yeah, they can do that."""
        print("Greetings, my masters call me {}.".format(self.name))

    @classmethod
    def how_many(cls):
        """Prints the current population."""
        print("We have {:d} robots.".format(cls.population))


droid1 = Robot("R2-D2")
droid1.say_hi()
Robot.how_many()

droid2 = Robot("C-3PO")
droid2.say_hi()
Robot.how_many()

print("\nRobots can do some work here.\n")

print("Robots have finished their work. So let's destroy them.")
droid1.die()
droid2.die()

Robot.how_many()

# Credit card Class


class CreditCard:

    def __init__(self, customer, bank, acnt, limit, balance=0):
        """
        Create a new credit card instance. 
        The initial balance is zero.
        """
        self._customer = customer
        self._bank = bank
        self._account = acnt
        self._limit = limit
        self._balance = balance
        self._charge_count = 0

    def get_customer(self):
        """Return the name of the customer"""
        return self._customer

    def get_bank(self):
        """Return the bank's name"""
        return self._bank

    def get_account(self):
        """Return the card identifying number (typically a str)"""
        return self._account

    def get_limit(self):
        """Return current credit limit"""
        return self._limit

    def get_balance(self):
        """Return current balance"""
        return self._balance

    def charge(self, price):
        """
        Charge given price to the card, assuming sufficient credit limit.
        Return True if charge was processed, False if charge was denied
        """
        if not isinstance(price, (float, int)):
            raise ValueError('price must be a number.')
        if price + self._balance > self._limit:
            print(
                f"Credit card with account number {self._account} denied. Accrued balance over limit.")
            return False
        else:
            self._balance += price
            self._charge_count += 1
            if self._charge_count > 10:
                self._balance += 1  # $1 surcharge for all calls after 10 charges
            return True

    def make_payment(self, amount):
        if not isinstance(amount, (int, float)):
            raise ValueError('payment must be a number')
        elif amount < 0:
            raise ValueError('payment must be positive')
        """Process customer payment that reduces the balance"""
        self._balance -= amount
