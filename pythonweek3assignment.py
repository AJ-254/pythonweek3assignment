def calculate_discount(price, discount_percent):
    # Apply discount if 20% or more
    if discount_percent >= 20:
        final_price = price - (price * discount_percent / 100)
        return final_price
    else:
        return price
    
# Prompt user for input   
original_price = float(input("Enter the originsl price of the item: "))
discount = float(input("Enter the discount percentage: "))

# Calculate final price
final_price = calculate_discount(original_price, discount)

# Print results
if discount >= 20:
    print(f"Discount applied. Final price: ${final_price:.2f}")
else:
    print(f"No discount applie. Original price: ${final_price:.2f}")