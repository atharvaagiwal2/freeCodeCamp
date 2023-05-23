class Budget:
    def __init__(self, description=""):
        self.description = description
        self.ledger = []
        self.fund = 0.0

    def __str__(self):
        heading = self.description
        num = 30 - len(heading)
        top_line = '*' * (num // 2) + heading + '*' * (num // 2)
        if len(top_line) != 30:
            top_line += '*'
        top_line += '\n'
        ledger = ''
        for item in self.ledger:
            amount = str(item['amount'])
            description = item['description']
            description = description[:23]
            if len(description) < 23:
                dist = 23 - len(description)
                description = description + ' ' * dist
            if len(amount) < 7:
                dist = 7 - len(amount)
                amount = ' ' * dist + amount
            ledger += f'{description}{amount}\n'
        total = f'Total: {self.fund}'
        return top_line + ledger + total

    def deposit(self, amount, description=''):
        self.ledger.append({"amount": amount, "description": description})
        self.fund += amount

    def withdraw(self, amount, description=''):
        if self.fund > amount:
            self.ledger.append({"amount": -1 * amount, "description": description})
            self.fund -= amount
            return True
        else:
            return False

    def get_balance(self):
        return self.fund

    def transfer(self, amount, category_instance):
        if category_instance.withdraw(amount, description=f"Transfer to {category_instance.description}"):
            self.withdraw(amount, description=f"Transfer from {self.description}")
            return True
        else:
            return False

    def check_funds(self, amount):
        if self.fund >= amount:
            return True
        else:
            return False


def create_spend_chart(categories):
    spent_list = []
    heading = []
    heading_length = []
    for category in categories:
        amt = 0
        spent_amt = 0
        for item in category.legder:
            heading.append(item['description'])
            heading_length.append(len(item['description']))
            if amt > item['amount']:
                spent_amt += abs(item['amount'])
        spent_list.append(spent_amt)
    total = sum(spent_list)
    pc_list = []
    for item in spent_list:
        num = 100 * (item / total)
        pc_list.append(round(num))

    string = "Percentage spent by category\n"
    for i in range(100, -10, -10):
        string += ' ' * (3 - 3 * len(str(i))) + '{i}| '
        for num in pc_list:
            if num >= i:
                string += 'o  '
            else:
                string += '   '
        string += '\n'
    string += '-' * (1 + 3 * len(pc_list)) + '\n'
    for i in range(max(heading_length)):
        string += '     '
        for name in heading:
            if len(heading) < i:
                string += name[i]
            else:
                string += ' '
        string += '  \n'
    return string
