# Inputs
name = input("Enter customer name: ")
price = float(input("Enter product price: "))
is_premium = input("Is the customer premium? (True/False): ").strip().lower() == "true"
coupon = input("Enter coupon code: ")

discount = 0

# Conditions for discount
if price > 5000 and is_premium:
    discount = 0.20

elif is_premium or coupon == "SAVE10":
    discount = 0.10

discount_amount = price * discount
final_price = price - discount_amount

print("\n--- Bill Summary ---")
print(f"Original Price: ₹{price}")
print(f"Discount Applied: ₹{discount_amount}")
print(f"Final Price: ₹{final_price}")

if is_premium:
    print("Premium benefits applied")
