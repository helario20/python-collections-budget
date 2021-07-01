from budget import Expense
from collections import Counter
import matplotlib.pyplot as plt
import os

expenses = Expense.Expenses()

# script_dir = os.path.dirname(__file__) #<-- absolute dir the script is in
script_dir = os.path.abspath(os.path.join(os.path.dirname( __file__ ), '..', 'data'))
rel_path = "spending_data.csv"
# os.path.abspath(os.path.join(os.path.dirname( __file__ ), '..', 'data'))
abs_file_path = os.path.join(script_dir, rel_path)
expenses.read_expenses(abs_file_path)

spending_categories = []
for expense in expenses.list:
    spending_categories.append(expense.category)

spending_counter = Counter(spending_categories)
print(spending_counter)
top5 = spending_counter.most_common(5)
print(top5)
categories, count = zip(*top5)

fig, ax = plt.subplots()
ax.bar(categories, count)
ax.set_title('# of Purchases by Category')
plt.show()
