
percentages = []


class Category:
    total_spent = 0
    categories = []
    
    def __init__(self, name):
        self.name = name
        self.ledger = []
        self.total = 0
        self.spent = 0
        Category.categories.append(self.name)

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
            Category.total_spent += amount
            self.spent += amount
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

    def percentage_spent(self):
        percentages.append(int((self.spent / Category.total_spent) * 100))


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
auto.percentage_spent()
games.percentage_spent()
food.percentage_spent()



longest = -1
new_cat = []
x = " "
dash = '---'

graph = "Percentage spent by category\n"
print(graph)

for nums in reversed(range(0,110,10)):
    side_bar = f"{str(nums) + '|':>4}"
    print(side_bar)

dashes = f"    {dash * len(Category.categories)}"
print(dashes)

for item in Category.categories:
    if len(item) > longest:
        longest = len(item)
        long_word = item
for item in Category.categories:
    if len(item) <= len(long_word):
        item = f"{(item + (x * (len(long_word) - len(item) + 1)))}"
    new_cat.append(item)
for word in zip(*new_cat):
    words = ('  '.join(word))
    cats = f"     {words:>6}"
    print(cats)

print(percentages)
#print(os)
#food.transfer(49.35, 'Games')
#print(food.budget('Food'))

#games.budget('Games')

#games.budget('Games')
#print(food.get_balance())
#print(games.check_funds(200))
#print(food.percentage_spent())
