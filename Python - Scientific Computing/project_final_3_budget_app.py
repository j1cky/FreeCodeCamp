### Budget App Project


"""
Build a Budget App Project

Complete the Category class. It should be able to instantiate objects based
on differentbudget categories like food, clothing, and entertainment.
When objects are created, they are passed in the name of the category.
The class should have an instance variable called ledger that is a list.
The class should also contain the following methods:

      o A deposit method that accepts an amount and description. If no description is given,
	it should default to an empty string. The method should append an object to the
	ledger list in the form of {'amount': amount, 'description': description}.
      o A withdraw method that is similar to the deposit method, but the amount passed in
	should be stored in the ledger as a negative number. If there are not enough funds,
	nothing should be added to the ledger. This method should return True if the
	withdrawal took place, and False otherwise.
      o A get_balance method that returns the current balance of the budget category based on
	the deposits and withdrawals that have occurred.
      o A transfer method that accepts an amount and another budget category as arguments.
	The method should add a withdrawal with the amount and the description
	'Transfer to [Destination Budget Category]'. The method should then add a
	deposit to the other budget category with the amount and the description
	'Transfer from [Source Budget Category]'. If there are not enough funds,
	nothing should be added to either ledgers. This method should return True
	if the transfer took place, and False otherwise.
      o A check_funds method that accepts an amount as an argument. It returns False
	if the amount is greater than the balance of the budget category and returns
	True otherwise. This method should be used by both the withdraw method and
	transfer method.

When the budget object is printed it should display:

    A title line of 30 characters where the name of the category is centered in a line of * characters.
    A list of the items in the ledger. Each line should show the description and amount. The first 23 characters of the description should be displayed, then the amount. The amount should be right aligned, contain two decimal places, and display a maximum of 7 characters.
    A line displaying the category total.

Here is an example usage:
Example Code

food = Category('Food')
food.deposit(1000, 'deposit')
food.withdraw(10.15, 'groceries')
food.withdraw(15.89, 'restaurant and more food for dessert')
clothing = Category('Clothing')
food.transfer(50, clothing)
print(food)

And here is an example of the output:
Example Code

*************Food*************
initial deposit        1000.00
groceries               -10.15
restaurant and more foo -15.89
Transfer to Clothing    -50.00
Total: 923.96

Besides the Category class, create a function (outside of the class) called create_spend_chart that takes a list of categories as an argument. It should return a string that is a bar chart.

The chart should show the percentage spent in each category passed in to the function. The percentage spent should be calculated only with withdrawals and not with deposits. Down the left side of the chart should be labels 0 - 100. The 'bars' in the bar chart should be made out of the 'o' character. The height of each bar should be rounded down to the nearest 10. The horizontal line below the bars should go two spaces past the final bar. Each category name should be written vertically below the bar. There should be a title at the top that says 'Percentage spent by category'.

This function will be tested with up to four categories.

Look at the example output below very closely and make sure the spacing of the output matches the example exactly.
Example Code

Percentage spent by category
100|          
 90|          
 80|          
 70|          
 60| o        
 50| o        
 40| o        
 30| o        
 20| o  o     
 10| o  o  o  
  0| o  o  o  
    ----------
     F  C  A  
     o  l  u  
     o  o  t  
     d  t  o  
        h     
        i     
        n     
        g     

Note: open the browser console with F12 to see a more verbose output of the tests.


"""



class Category:
    
    def __init__(self, category):
        self.category = category
        self.ledger = []

    def deposit(self, amount, description=''):
        self.ledger.append({'amount': amount, 'description': description})

    def withdraw(self, amount, description=''):
        if self.check_funds(amount):
            self.ledger.append({'amount': -amount, 'description': description})
            return True
        else:
            return False
    
    def get_balance(self):
        balance = 0
        for transaction in self.ledger:
            balance += transaction['amount']
        return balance

    def check_funds(self, amount):
        balance = self.get_balance()
        if amount > balance :
            return False
        else:
            return True
    
    def transfer(self, amount, transfer_to):
        if self.check_funds(amount):  # Ensure there are enough funds
            self.withdraw(amount, f'Transfer to {transfer_to.category}')  # Withdraw from current category
            transfer_to.deposit(amount, f'Transfer from {self.category}')  # Deposit into the target category
            return True
        else:
            return False
    
    def __str__(self):
        title = f"{self.category:*^30}\n"
        items = ""
        for transaction in self.ledger:
            description = transaction["description"][:23]  # Truncate to 23 characters
            amount = f"{transaction['amount']:.2f}"[:7]  # Format to 2 decimal places, max 7 characters
            items += f"{description:<23}{amount:>7}\n"
        
        # Total balance
        total = f"Total: {self.get_balance():.2f}"
        
        return title + items + total




def create_spend_chart(categories):
    # Step 1: Calculate the percentage spent per category
    total_spent = 0
    category_spent = []
    for category in categories:
        spent = sum(transaction['amount'] for transaction in category.ledger if transaction['amount']<0 )
        total_spent+= spent
        category_spent.append(spent)

    percentages = [ int((spent / total_spent)*100) //10 * 10 for spent in category_spent]

    # Step 2: Build the bar chart
    chart = 'Percentage spent by category\n'
    for i in range (100, -1, -10):
        chart += f'{i:>3}|'
        for percent in percentages :
            chart += ' o ' if percent >= i else '   '
        chart +=' \n'
    
    # Step 3: Add the horizontal line
    chart += '    ' + '-'*3*len(category_spent) + '-\n'

    # Step 4: Write category names vertically
    max_len = max(len(category.category) for category in categories)
    names = [ category.category.ljust(max_len) for category in categories]
    for i in range(max_len):
        chart += '     '
        for name in names :
            chart += name[i] + '  '  
        chart += "\n"
    
     

    return   chart.rstrip("\n") 







food = Category('Food')
food.deposit(1000, 'deposit')
food.withdraw(10.15, 'groceries')
food.withdraw(20.15, 'groceries')
clothing = Category('Clothing')
food.transfer(50, clothing)
print(food)


categories = [food, clothing]

print(create_spend_chart(categories))
