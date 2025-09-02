#Answer1
# Function to calculate discount
def calculate_discount(price, discount_percent):
    if discount_percent >= 20:
        discount_amount = price * (discount_percent / 100)
        final_price = price - discount_amount
        return final_price
    else:
        return price

# Prompt the user for input
price = float(input("Enter the original price of the item: "))
discount_percent = float(input("Enter the discount percentage: "))


#Answer2
# Use the function
final_price = calculate_discount(price, discount_percent)

# Print the result
print("Final price after discount: ", final_price)
