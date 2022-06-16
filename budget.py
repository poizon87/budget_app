class Category:
    
    def __init__(self, name):
        self.name = name
        self.ledger = []
        self.total = 0

    def deposit(self, amount, description=''):
        self.amount = amount
        self.description = description
        self.ledger.append({"amount": amount, "description": description})
        self.total += amount

    def withdraw(self, amount, description=''):
        self.amount = amount
        self.description = description
        if self.total < amount:
            return False
        else:
            self.ledger.append({"amount": -amount, "description": description})
            self.total -= amount
            return True

    def get_balance(self):
        return self.total

    def transfer(self, amount, category):

        if (self.check_funds(amount)):
            self.withdraw(amount, ('Transfer to ' + category.name))
            category.deposit(amount, ('Transfer from ' + self.name))


    def check_funds(self, amount):
        self.amount = amount
        if self.amount <= self.get_balance():
            return True
        else:
            return False

    def budget(self, name):
        print(f"{name:*^30}")
        for item in self.ledger:
            print(f"{item['description'][0:23]:<23}{item['amount']:>7.2f}")
        print(f"Total: {self.total:.2f}")

categories = ['Food','Games','Auto']
items = str(categories).split()
#items = str(items).replace(',','').replace('[','').replace(']','').replace('"','').replace("'",'')
title = "Percentage spent by category"
x = 0
print(title)
for nums in reversed(range(0,110,10)):
    print(f"{str(nums) + '|':>4}")
for item in items:
    print(item)
#print(items)


















auto = Category('Auto')
games = Category('Games')
food = Category('Food')
food.deposit(500, "initial deposit")
food.withdraw(10.50, "taco bell")
food.withdraw(40.15, "red beans and rice bigbowl")
games.deposit(200, "fun deposit")
games.withdraw(49.99, "pokemon")
auto.deposit(500, "car fund")
auto.withdraw(100, "gas")
food.transfer(50, games)



#food.transfer(49.35, 'Games')
#print(food.budget('Food'))

#games.budget('Games')

#games.budget('Games')
#print(food.get_balance())
#print(games.check_funds(200))

