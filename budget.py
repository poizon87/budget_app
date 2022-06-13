class Category:
    ledger = list('')
    total = 0.0

    def __init__(self, name):
        self.name = name

    def deposit(self, amount, description=''):
        self.amount = float(amount)
        self.description = description
        self.ledger.append(f"amount: {self.amount} description: {description}")
        self.total += float(amount)

    def withdraw(self, amount, description=''):
        self.amount = float(amount)
        self.description = description
        #self.max_withdraw = self.total
        if self.amount > self.total:
            return False
        else:
            self.ledger.append(f"amount: -{self.amount} description: {description}")
            self.total -= float(amount)
            return True

    def get_balance(self, name):
        return self.total

    def transfer(self, amount, name):
        pass

    #def get_ledger(self, name)

    def budget(self, name):
        print(f"{name:*^30}")
        for item in self.ledger:
            item = item.replace('amount: ','').replace('description: ',',').split(',')

            print(f"{item[1]:<23}{item[0]:>7}")
        print(f"Total: {self.total}")

food = Category('Food')
food.deposit(500, "groceries")
food.withdraw(10.50, "taco bell")
food.budget('Food')

