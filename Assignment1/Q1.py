
# 1. Take inputs
name = input("Enter student name: ")
age = int(input("Enter age: "))
percentage = float(input("Enter percentage: "))
income = float(input("Enter family income: "))
rural = input("Is the student from a rural area? (True/False): ").strip().lower() == "true"

# Checking eligiblity
eligible = (percentage > 90) or (percentage > 85 and income < 300000)

if eligible:
    result = "Eligible for scholarship"
else:
    result = "Not eligible"

print("\n--- Student Details ---")
print(f"Name: {name}")
print(f"Age: {age}")
print(f"Percentage: {percentage}")
print(f"Family Income: {income}")
print(f"Rural Area: {rural}")
print(f"Result: {result}")
