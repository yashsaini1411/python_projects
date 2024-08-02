import json
import os
class ExpenseTracker:
    def __init__(self, data_file="expense.json"):
        self.data_file = data_file
        self.expenses = self.load_data()
        
    def load_data(self):
        if os.path.exists(self.data_file):
            with open(self.data_file, 'r') as file:
                return json.load(file)
        return {"expenses": []}
    
    def save_data(self):
        with open(self.data_file, 'w') as file:
            json.dump(self.expenses, file, indent=2)
            
    def add_expenses(self, amount, description, category):
        expense = {"amount": amount, "description": description, "category": category}
        self.expenses["expenses"].append(expense)
        self.save_data()
        
    def get_monthly_summary(self):
        monthly_summary = {}
        for expense in self.expenses["expenses"]:
            month_year = expense.get("date", "unknown")
            if month_year not in monthly_summary:
                monthly_summary[month_year] = 0
            monthly_summary[month_year] += expense["amount"]
        return monthly_summary
    
    def get_category_summary(self):
        category_summary = {}
        for expense in self.expenses["expenses"]:
            category = expense["category"]
            if category not in category_summary:
                category_summary[category] = 0
            category_summary[category] += expense["amount"]
        return category_summary
    
    def show_expenses(self):
        for expense in self.expenses["expenses"]:
            print(f"Amount: \u20B9{expense['amount']} | Description: {expense['description']} | Category: {expense['category']}")
        
        
# User Interface

def main():
    tracker = ExpenseTracker()
    
    while True:
        print("\nExpense Tracker Menu:")
        print("1. Add Expense")
        print("2. View Monthly Summary")
        print("3. View Category-Wise Expenditure")
        print("4. View All Expenses")
        print("5. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == "1":
            amount = float(input("Enter the amount spent: "))
            description = input("Enter a brief description: ")
            category = input("Enter the expense category: ")
            tracker.add_expenses(amount, description, category)
            print("Expense added successfully.")
            
        elif choice == "2":
            monthly_summary = tracker.get_monthly_summary()
            print("\nMonthly Summary:")
            for month_year, total_amount in monthly_summary.items():
                print(f"{month_year}: \u20B9{total_amount}")
                
        elif choice == "3":
            category_summary = tracker.get_category_summary()
            print("\nCategory-Wise Expenditure:")
            for category, total_amount in category_summary.items():
                print(f"{category}: \u20B9{total_amount}")
                
        elif choice == "4":
            tracker.show_expenses()
            
        elif choice == "5":
            print("Exiting Expense Tracker.")
            break
        
        else:
            print("Invalid choice. Please choose a correct option.")
            

if __name__ == "__main__":
    main()

