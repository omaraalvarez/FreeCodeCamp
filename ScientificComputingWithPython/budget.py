class Category:

    def __init__(self, cat):

        self.cat = cat
        self.ledger = []
        self.total = 0

    def __repr__(self):

        spacing = (30 - len(self.cat)) // 2

        string = spacing * '*' + self.cat + spacing * '*' + '\n'

        for e in self.ledger:

            description = e['description'][:23]
            amount = str(e['amount'])

            if e['amount'] % 1 == 0:

                amount += '.00'

            spacing = 30 - len(description) - len(amount)

            string += description + spacing * ' ' + amount + '\n'

        string += f'Total: {self.total}'

        return string

    def deposit(self, amount, description=''):

        self.total += amount

        self.ledger.append({'amount': amount, 'description': description})

    def withdraw(self, amount, description=''):

        if self.check_funds(amount):

            self.ledger.append({'amount': -amount, 'description': description})

            self.total -= amount

            return True

        else:

            return False

    def get_balance(self):

        return self.total

    def transfer(self, amount, new_cat):

        if self.check_funds(amount):

            self.withdraw(amount, f'Transfer to {new_cat.cat}')
            new_cat.deposit(amount, f'Transfer from {self.cat}')

            return True

        else:

            return False

    def check_funds(self, amount):

      if amount <= self.total:

          return True

      else:

          return False


def create_spend_chart(categories):

    n_cat = len(categories)

    string = 'Percentage spent by category' + '\n'

    spent = [sum([c['amount'] for c in cat.ledger if c['amount'] < 0]) for cat in categories]
    total_spent = sum(spent)

    spent = [10 * s / total_spent for s in spent]

    if len(categories) == 1:

        string += '100| o' + 3 * (n_cat - 1) * ' ' + 2 * ' ' + '\n'

    else:

        string += '100|  ' + 3 * (n_cat - 1) * ' ' + 2 * ' ' + '\n'

    for i in range(9, 0, -1):

        string += f' {str(10 * i)}| '

        for s in spent:

            if i <= s:

                string += 'o' + 2 * ' '

            else:

                string += 3 * ' '

        string += '\n'

    string += '  0| ' + n_cat * 'o  ' + '\n'

    string += 4 * ' ' + 2 * '-' + (n_cat - 1) * '---' + 2 * '-' + '\n'

    cat_names = [c.cat for c in categories]

    max_cat_name = max([len(cat) for cat in cat_names])

    for i in range(max_cat_name):

        string += 5 * ' ' + '  '.join([s[i] if i < len(s) else ' ' for s in cat_names]) + 2 * ' '

        if i < max_cat_name - 1:

            string += '\n'

    return string



