import pandas as pd

# Sample data
data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Emma'],
    'Age': [25, 30, 35, 28, 32],
    'City': ['London', 'New York', 'Paris', 'Paris', 'Sydney'],
    'Salary': [60000, 75000, 80000, 70000, 65000]
}

employees = pd.DataFrame(data)

print("task 1 label")
print(employees.loc[3:4, ["Name", "Salary"]])

print("task 1 index")
print(employees.iloc[3:5, [0, 3]])

print("task 2")
print(employees.iloc[0:3])

print("task 3")
print(employees[employees["Age"] >= 30])