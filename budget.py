class Category:
    def __init__(self, name):
        self.name = name
        self.ledger = []
    
    def deposit(self, amount, description=""):
        self.ledger.append({"amount":amount, "description":description})

    def withdraw(self, amount, description=""):
        if not self.check_funds(amount):
            self.ledger.append({"amount":-amount, "description":description})
            return True
        return False

    def get_balance(self):
        balance = 0
        for trans in self.ledger:
            balance += trans["amount"]
        return balance

    def transfer(self, amount, category):
        if self.withdraw(amount, "Transfer to " + category.name):
            category.deposit(amount, "Transfer from " + self.name)
            return True
        return False

    def check_funds(self, amount):
        return amount > self.get_balance()

    def __str__(self):
        result = ""
        result += self.name.center(30, "*") + "\n"
        for trans in self.ledger:
            result += "{:<23}{:>7}".format(trans["description"][:23], ("%.2f" % trans["amount"])[:7]) + "\n"
        result += "Total: " + "{}".format("%.2f" % self.get_balance())
        return result
