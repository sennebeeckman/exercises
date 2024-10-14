import pandas as pd

data = {
    'EmployeeID': [101, 102, 103, 104, 105],
    'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Emma'],
    'Department': ['HR', 'IT', 'Finance', 'Marketing', 'Sales'],
    'Salary': [60000, 75000, 80000, 70000, 65000]
}

employees = pd.DataFrame(data)

print(employees.head(3))

print(employees["Salary"].describe())

print(employees.groupby("Department")["EmployeeID"].count())

average_salary = employees["Salary"].mean()
print(average_salary)

print(employees[employees['Salary'] == employees['Salary'].max()])

print("hello")
lowest_average = employees.groupby("Department")["Salary"].mean().idxmin()
print(lowest_average)

employees["Salary Increase"] = employees['Salary'] * 1.1
print(employees)