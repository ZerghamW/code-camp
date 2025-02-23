class Category:
    def __init__(self, name):
        self.name = name
        self.ledger = []

    def deposit(self, amount, description=""):
        self.ledger.append({"amount": amount, "description": description})

    def withdraw(self, amount, description=""):
        if self.check_funds(amount):
            self.ledger.append({"amount": -amount, "description": description})
            return True
        return False

    def get_balance(self):
        return sum(item["amount"] for item in self.ledger)

    def transfer(self, amount, category):
        if self.check_funds(amount):
            self.withdraw(amount, f"Transfer to {category.name}")
            category.deposit(amount, f"Transfer from {self.name}")
            return True
        return False

    def check_funds(self, amount):
        return self.get_balance() >= amount

    def __str__(self):
        title = f"{self.name.center(30, '*')}\n"
        items = "\n".join(
            f"{item['description'][:23]:23}{item['amount']:7.2f}"
            for item in self.ledger
        )
        return f"{title}{items}\nTotal: {self.get_balance():.2f}"


def create_spend_chart(categories):
    # Calculate withdrawals (excluding transfers)
    withdrawals = []
    for cat in categories:
        spent = sum(
            -item["amount"]
            for item in cat.ledger
            if item["amount"] < 0 and "Transfer" not in item["description"]
        )
        withdrawals.append(spent)
    
    total = sum(withdrawals)
    
    # Calculate percentages (floored to nearest 10)
    percentages = [
        int((w / total * 100) // 10 * 10) if total != 0 else 0
        for w in withdrawals
    ]
    
    # Build chart
    chart = ["Percentage spent by category"]
    
    # Percentage lines
    for i in range(100, -10, -10):
        line = f"{i:3}| "
        for p in percentages:
            line += "o" if p >= i else " "
            line += "  "  # 2 spaces between bars
        chart.append(line)
    
    # Horizontal line (exact length)
    horizontal_line = "    " + "-" * (3 * len(categories) + 1)
    chart.append(horizontal_line)
    
    # Vertical names (exact spacing)
    max_len = max(len(cat.name) for cat in categories)
    for i in range(max_len):
        line = "    "
        for cat in categories:
            line += f" {cat.name[i]} " if i < len(cat.name) else "   "
        line = line.ljust(len(horizontal_line))
        chart.append(line)
    
    return "\n".join(chart)