class MoneyMachine:

    CURRENCY = "$"

    COIN_VALUES = {
        "quarters": 0.25,
        "dimes": 0.10,
        "nickles": 0.05,
        "pennies": 0.01
    }

    def __init__(self):
        self.profit = 0
        self.money_received = 0

    def report(self):
        """Prints the current profit"""
        print(f"Money: {self.CURRENCY}{self.profit}")

    def process_coins(self):
        """Returns the total calculated from coins inserted."""
        self.money_received = 0
        print("Please insert coins.")
        for coin in self.COIN_VALUES:
            count = self._get_coin_count(coin)
            self.money_received += count * self.COIN_VALUES[coin]
        print(f"Inserted total: {self.CURRENCY}{round(self.money_received, 2)}")
        return self.money_received

    def _get_coin_count(self, coin_name):
        """Gets a valid, non-negative integer count for a coin type."""
        while True:
            raw = input(f"How many {coin_name}?: ").strip()
            try:
                count = int(raw)
            except ValueError:
                print("Please enter a whole number.")
                continue
            if count < 0:
                print("Please enter a non-negative number.")
                continue
            return count

    def make_payment(self, cost):
        """Returns True when payment is accepted, or False if insufficient."""
        self.process_coins()
        if self.money_received >= cost:
            change = round(self.money_received - cost, 2)
            print(f"Here is {self.CURRENCY}{change} in change.")
            self.profit += cost
            self.money_received = 0
            return True
        else:
            print("Sorry that's not enough money. Money refunded.")
            self.money_received = 0
            return False
