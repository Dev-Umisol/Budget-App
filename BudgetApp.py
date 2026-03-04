# Building a Budget App
# Certification 2 of freeCodeCamp, a budget app that utilizes classes and objects, along with everything else learned previously

import math

class Category:
    def __init__(self, name):
        self.name = name
        self.ledger = []
    
    # creating a dictionary to add money into account
    def deposit(self, amount, description=''):
        self.ledger.append({
            "amount": amount,
            "description": description
        })
     
     # Passing in amount and updating dictionary to negative amount so that it takes out the money
    def withdraw(self, amount, description=''):
        if self.CheckFunds(amount):
            self.ledger.append({
                "amount": -amount,
                "description": description
            })
            return True
        else:
            return False
    
    # returns the total amount left in the account
    def GetBalance(self):
        total = 0
        
        for balance in self.ledger:
            total += balance["amount"]
        return total
    
    # Checks if truthy and withdraws/deposits into specific category, or self else False
    def transfer(self, amount, category):
        if self.CheckFunds(amount):
            self.withdraw(amount, f"Transfer to {category.name}")
            category.deposit(amount, f"Transfer from {self.name}")
            return True
        else:
            return False
    
    # String method for looping through each ledger entry and printing kinda like a receipt
    def __str__(self):
        output = self.name.center(30, "*")
        output += "\n"
        
        for i in self.ledger:
            output += f"{i['description'][:23]:<23}{i['amount']:>7.2f}\n"
            
        output += f"Total: {self.GetBalance()}"
        
        return output

    # Compares the amount of money in the account to the total, if amount is < total False, else True
    def CheckFunds(self, amount):
        total = 0
        
        for transaction in self.ledger:
            total += transaction["amount"]
        return amount <= total # <-- if amount < total Return False, else: True

def CreateSpendChart(categories):
    output = "Percentage spent by category"
    output += "\n"
    
    # Calculate total amount spent per category
    categoryTotal = []
    
    for category in categories:
        counter = 0
        
        for transaction in category.ledger:
            if transaction['amount'] < 0:
                counter += transaction["amount"]
            
        categoryTotal.append(counter)
        
    total = sum(categoryTotal) # Grand total across all categories
    percentages = [] # calculate each category percentage, rounded down to nearest 10
    
    for i in categoryTotal:
        percentage = (i / total) * 100
        percentage /= 10
        percentage = math.floor(percentage)
        percentage *= 10
        percentages.append(percentage)
    
    # Bar chart row 100 - 0
    for i in range(100, -10, -10):
        output += f"{i:>3}|"

        for j in percentages:
            if j >= i:
                output += " o "
            else:
                output += '   '
        output += " \n"
    
    output += "    " + "-" * len(categories) * 3 + "-" + "\n" # <-- Horizontal line below bars
    
    #Finding the length of the LONGEST category name for vertical label rows
    longestName = max(categories, key=lambda c: len(c.name))
    categoryName = len(longestName.name)
    
    # Vertical names
    for k in range(0, categoryName):
        output += "    "
        for l in categories:
            if k < len(l.name):
                output += " " + l.name[k] + " " # print character
            else:
                output += '   ' # Pad shorter names with spaces
        output += " "
        if k < categoryName - 1:    
            output += "\n"
            
    return output

food = Category('Food')
food.deposit(1000, 'initial deposit')
food.withdraw(10.15, 'groceries')
food.withdraw(15.89, 'restaurant and more food for dessert')
clothing = Category('Clothing')
food.transfer(50, clothing)
print(food)